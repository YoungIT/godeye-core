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
        text=['LMAO'],
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

    with gr.Blocks() as demo:
        demo_image_input = gr.Image(label="Input image", image_mode="RGB", type="pil")

        btn = gr.Button(value="Get location")
        map = gr.Plot()

        demo.load(filter_map, [demo_image_input], map)
        btn.click(filter_map, [demo_image_input], map)
    
    demo.launch(server_name="0.0.0.0", share=True)