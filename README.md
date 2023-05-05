# GodEye
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/YoungIT/godeye-core">
    <img src="docs/images/godeye.jpg" alt="Logo" width="180" height="80">
  </a>

<h3 align="center">GodEye</h3>

  <p align="center">
    An open-source image OSINT tool
    <br />
    <a href="https://github.com/YoungIT/godeye-core"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/YoungIT/godeye-core">View Demo</a>
    ·
    <a href="https://github.com/YoungIT/godeye-core/issues">Report Bug</a>
    ·
    <a href="https://github.com/YoungIT/godeye-core/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `godeye-core`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

## Web demo
A demo of the app can be accessed at this url: https://godeye.yitec.net

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.8
* GPU with cuda support

### Installation


To run the project, please refer to the following steps

Clone the project and update the submodules
```
git clone https://github.com/YoungIT/godeye-core
cd godeye-core
git submodule update --init --remote
```

#### Pipeline selection
Depending on the pipeline that you select, you will need to install specific pretrained models and metadatas

##### TIBHannover (default)
To run the TIBHannover pipeline manually, you need to download the pretrained model.

```
mkdir -p resources/tibhannover/models
wget https://github.com/TIBHannover/GeoEstimation/releases/download/pytorch/epoch.014-val_loss.18.4833.ckpt -O resources/tibhannover/models/epoch=014-val_loss=18.4833.ckpt
```

#### Running with Docker
For simplicity, you can run the whole system with an interactive demo with a single Docker command

```
docker compose up -d
```

#### Running manually
If you want to run the whole system manually, you can refer to the following steps.

First, create a seperated conda environment

```
conda create -n py38_godeye python=3.8 -y
conda activate py38_godeye
```

Install the required dependencies

```
pip install -e .
```

To run the pipeline that will produce a prediction based on an image, run the following command

```
python src/core/core.py img=[YOUR IMAGE PATH]
```

For example, you could run with a sample image from the `assets` directory
```
python src/core/core.py img=assets/imgs/london.jpeg
```

The output contains a list of coordinates that are possibly the location where the image was taken. You can copy and paste one of the coordinate into [Google Maps](https://www.google.com/maps) to see the exact location.

### Change the type of pipeline

You can customize the pipeline that is used to predict the image location by overriding running parameters.  This section shows a list of supported pipeline and their corresponding command

| Pipeline   |      Description      |  Run command |
|----------|:-------------:|------:|
| [StreetClip](https://huggingface.co/geolocal/StreetCLIP) + city |  Use StreetClip with candidate classname set to cities | `python src/core/core.py candidate-generation=streetclip geo-estimation=city-to-coord location-ranking=random metadata-extractor=empty img=YOUR_IMAGE_PATH` |
| [StreetClip](https://huggingface.co/geolocal/StreetCLIP) + country |    with candidate classname set to country   |   `python src/core/core.py candidate-generation=streetclip geo-estimation=country-to-coord location-ranking=random metadata-extractor=empty img=YOUR_IMAGE_PATH` |
| [TIBHannover](https://github.com/TIBHannover/GeoEstimation) | Use TIBHannover to produce the coordinate |    `python src/core/core.py candidate-generation=streetclip geo-estimation=tibhannover location-ranking=random metadata-extractor=exif img=YOUR_IMAGE_PATH` |

<!-- ROADMAP -->
## Roadmap

- [x] Integrate [TIB Hannover geolocation](https://github.com/TIBHannover/GeoEstimation)
- [x] Integrate [Streetclip](https://github.com/TIBHannover/GeoEstimation)
- [ ] Intergrate google streetview with image comparison

See the [open issues](https://github.com/YoungIT/godeye-core/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

YITEC - contact@yitec.group

Project Link: [https://github.com/YoungIT/godeye-core](https://github.com/YoungIT/godeye-core)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/YoungIT/godeye-core.svg?style=for-the-badge
[contributors-url]: https://github.com/YoungIT/godeye-core/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YoungIT/godeye-core.svg?style=for-the-badge
[forks-url]: https://github.com/YoungIT/godeye-core/network/members
[stars-shield]: https://img.shields.io/github/stars/YoungIT/godeye-core.svg?style=for-the-badge
[stars-url]: https://github.com/YoungIT/godeye-core/stargazers
[issues-shield]: https://img.shields.io/github/issues/YoungIT/godeye-core.svg?style=for-the-badge
[issues-url]: https://github.com/YoungIT/godeye-core/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/yitec
[product-screenshot]: docs/images/web-demo.jpg

## License

GodEye has Apache 2.0 license, which can be found in the [LICENSE](docs/LICENSE.md) file