import os
import re
import urllib.request
import urllib.parse
import pandas as pd
import requests 
from PIL import Image
from bs4 import BeautifulSoup
from hydra import compose, initialize
from omegaconf import open_dict
import geopy.distance

from src.core.common.utils.geography import *
from src.core.core import init_pipeline

def download_img_from_url(url, save_path):
    urllib.request.urlretrieve(url, save_path)

# def get_coordinate_based_on_name(name):
#     print("Get coord: ", name)
#     return country_to_lat_long_geopy(name)

def get_coordinate_from_url(url):
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    a_tags = soup.find_all('a', attrs={'class': "external text"})
    
    lat, lng = None, None
    for tag in a_tags:
        content = tag.text 
        if(content.endswith("W") or content.endswith("E")):
            lat, lng = content.split(",")
        
    return lat, lng

def parse_coordinates(lat_dms, lng_dms):
    pattern = re.compile(r'(\d+)°\s(\d+)′\s([\d\.]+)″\s([NSWE])')
        
    # Extract the numeric values from the DMS format using the regular expression
    lat_deg, lat_min, lat_sec, lat_dir = pattern.search(lat_dms).groups()
    lng_deg, lng_min, lng_sec, lng_dir = pattern.search(lng_dms).groups()

    # Convert the DMS values to decimal degrees
    latitude = float(lat_deg) + float(lat_min) / 60 + float(lat_sec) / 3600
    if lat_dir == 'S':
        latitude *= -1
    longitude = float(lng_deg) + float(lng_min) / 60 + float(lng_sec) / 3600
    if lng_dir == 'W':
        longitude *= -1
        
    return latitude, longitude


def get_googlelandmark_data(filepath):    
    colnames=["img_url", "wiki_path"] 
    data = pd.read_csv(filepath, names=colnames)
    num_rows = data.shape[0]
    
    loc_names = [None] * num_rows
    loc_lat = [None] * num_rows
    loc_lng = [None] * num_rows 

    for index, row in data.iterrows():
        img_url = row["img_url"]
        wiki_path = row["wiki_path"]
        
        print(wiki_path)
        
        loc_name = wiki_path.split(":")[-1]
        loc_name = urllib.parse.unquote(loc_name).replace("/", "_")
        loc_names[index] = loc_name 
        
        save_path = os.path.join("../assets/imgs/google-landmark", f"{loc_name}.jpg")

        # download_img_from_url(img_url, save_path) 
        
        try:
            lat_deg, lng_deg = get_coordinate_from_url(wiki_path)
            lat, lng = parse_coordinates(lat_deg, lng_deg)
            print(lat, lng)
            
            loc_lat[index] = lat
            loc_lng[index] = lng
        except TypeError as e:
            print(e)
            continue

    data["name"] = loc_names
    data["lat"] = loc_lat
    data["lng"] = loc_lng
    
    data.to_csv("../assets/data/img2landmark_latlng.csv")
    print("Finished")
    
def infer(pipeline, image_path):
    output = {
        "image": Image.open(image_path).convert("RGB")
    }

    for module in pipeline:
        if type(output) != dict:
            output = module(output)
        else:
            output = module(**output)
            
    return output["coordinates"]
    
def benchmark_pipeline():
    with initialize(version_base="1.1", config_path="../configs"):
        cfg = compose(config_name="pipeline-tibhannover.yaml", overrides=[])
        pipeline = init_pipeline(cfg)

        # get data
        csv_data = pd.read_csv(cfg["google_landmark_data"])
        csv_data = csv_data[csv_data['lat'].notna()]

        images = os.listdir(cfg["google_landmark_images"])
        
        dists = []
        for image in images:
            print("Process: ", image)
            image_name = image.split(".")[0]
            # get groundtruth
            data = csv_data.loc[csv_data["name"] == image_name]
            if(data.empty):
                print("Skip")
                continue 
            
            gt_lat = data["lat"].values[0]
            gt_lng = data["lng"].values[0]
                                                
            image_path = os.path.join(cfg["google_landmark_images"], image) 
            coords = infer(pipeline, image_path)
            # select only first coordinates
            print("Coords: ", coords[0])

            dist = geopy.distance.geodesic(coords[0], (gt_lat, gt_lng)).km
            dists.append(dist)
            print("Distance: ", dist)
            
        print(f"Avg distance: {sum(dists) / len(images)} km")


if __name__ == "__main__":
    benchmark_pipeline()




