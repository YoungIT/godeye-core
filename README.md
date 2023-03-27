# GodEye

## Run the pipelines

### TIBHannover
#### Setup

Download pretrained model
```
cd src/core/lib/GeoEstimation
mkdir -p tibhannover
wget https://github.com/TIBHannover/GeoEstimation/releases/download/pytorch/epoch.014-val_loss.18.4833.ckpt -O models/base_M/epoch=014-val_loss=18.4833.ckpt
wget https://github.com/TIBHannover/GeoEstimation/releases/download/pytorch/hparams.yaml -O models/base_M/hparams.yaml
```

Download grid data & model
```
mkdir resources
mkdir -p resources/tibhannover/s2_cells
mkdir -p resources/tibhannover/models
wget https://raw.githubusercontent.com/TIBHannover/GeoEstimation/original_tf/geo-cells/cells_50_5000.csv -O resources/tibhannover/s2_cells/cells_50_5000.csv
wget https://raw.githubusercontent.com/TIBHannover/GeoEstimation/original_tf/geo-cells/cells_50_2000.csv -O resources/tibhannover/s2_cells/cells_50_2000.csv
wget https://raw.githubusercontent.com/TIBHannover/GeoEstimation/original_tf/geo-cells/cells_50_1000.csv -O resources/tibhannover/s2_cells/cells_50_1000.csv

# Download the model params & weights
wget https://github.com/TIBHannover/GeoEstimation/releases/download/pytorch/epoch.014-val_loss.18.4833.ckpt -O resources/tibhannover/epoch=014-val_loss=18.4833.ckpt
wget https://github.com/TIBHannover/GeoEstimation/releases/download/pytorch/hparams.yaml -O resources/tibhannover/hparams.yaml
```