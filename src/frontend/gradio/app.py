import glob
import os
import pyrootutils
from loguru import logger
from omegaconf import DictConfig, OmegaConf

from hydra import compose, initialize
import gradio as gr
from PIL import Image
import numpy as np
import plotly.graph_objects as go

from src.core.core import init_pipeline

base_path = pyrootutils.find_root(search_from=__file__, indicator=[".git", "setup.cfg"])

def get_image_examples(path):
    logger.info("Get image examples")
    supported_formats = Image.registered_extensions()
    logger.debug(f"Supported image format {supported_formats}")
    
    pattern = "{}/**/*{}"

    imgs = []
    for img_format in supported_formats.keys():
        search_pattern = pattern.format(path, img_format)
        imgs.extend(glob.glob(search_pattern, recursive = True))
        
    logger.info(f"Get total of {len(imgs)} examples")
    return imgs

def filter_map(demo_image_input):
    lat, lon = 40.67, -73.90
    coords = [[40.67, -73.90]]

    if(demo_image_input is not None):
        output = {
            "image": demo_image_input
        }
        for module in pipeline:
            if type(output) != dict:
                output = module(output)
            else:
                output = module(**output)
            # print(module, output)

        coords = output["coordinates"]
        lat, lon = coords[0][0], coords[0][1]

    fig = go.Figure(go.Scattermapbox(
        lat=[f'{coord[0]}' for coord in coords],
        lon=[f'{coord[1]}' for coord in coords],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=25
        ),
        text=['Hi'],
    ))

    fig.update_layout(
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=lat,
                lon=lon
            ),
            pitch=0,
            zoom=9
        ),
    )
    
    return fig

# if __name__ == "__main__":
with initialize(version_base="1.1", config_path="../../../configs"):
    cfg = compose(config_name="pipeline-tibhannover.yaml", overrides=[])
    pipeline = init_pipeline(cfg)
    
    # get image examples
    img_examples = get_image_examples("./Tests") 

    with gr.Blocks() as demo:
        demo_image_input = gr.Image(label="Input image", image_mode="RGB", type="pil")
        example_slider = gr.Examples(examples=img_examples, 
                                     inputs=[demo_image_input], 
                                     label="Image Examples",
                                     examples_per_page=10)

        btn = gr.Button(value="Get location")
        map = gr.Plot()

        demo.load(filter_map, [demo_image_input], map)
        btn.click(filter_map, [demo_image_input], map)
    
    demo.launch(server_name="0.0.0.0", share=True)