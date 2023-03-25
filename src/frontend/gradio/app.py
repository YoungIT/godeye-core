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
    print(demo_image_input)
    output = {
        "image": demo_image_input
    }
    for module in pipeline:
        if type(output) != dict:
            output = module(output)
        else:
            output = module(**output)
        # print(module, output)

    coords = output["scores"][0][0]

    lat = coords[0]
    lon = coords[1]

    fig = go.Figure(go.Scattermapbox(
        lat=[f'{lat}'],
        lon=[f'{lon}'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=40
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
    cfg = compose(config_name="pipeline-country.yaml", overrides=[])
    pipeline = init_pipeline(cfg)

    with gr.Blocks() as demo:
        demo_image_input = gr.Image(label="Input image", image_mode="RGB", type="numpy")

        btn = gr.Button(value="Get location")
        map = gr.Plot()

        demo.load(filter_map, [demo_image_input], map)
        btn.click(filter_map, [demo_image_input], map)
    
    demo.launch()