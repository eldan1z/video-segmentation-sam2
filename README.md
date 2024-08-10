# Vehicle Segmentation from Videos using SAM2 Model

This project uses the SAM2 model for vehicle segmentation from videos. It involves extracting frames from videos and detecting vehicles from these frames.
The SAM2 model provides state-of-the-art segmentation capabilities, making it ideal for tasks that require precise object segmentation.

## Features

- Frame Extraction: Extracts every frame from a video file and saves them as individual .jpg files.
- Vehicle Detection: Segments vehicles from multiple frames using the SAM2 model.

## Installation

First you have to build SAM2 from [source](https://github.com/facebookresearch/segment-anything-2.git)

```bash
  git clone git clone https://github.com/facebookresearch/segment-anything-2.git
  cd segment-anything-2
  pip install -e .
```

Second, install the required packages:

```bash
  pip install -r requirements.txt
```

## Usage

1. Install checkpoint file:

```bash
  wget https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_large.pt
```

2. Run the script for frame extraction:

```bash
  python main.py --video_path <path_to_video>
```

3. You can find notebooks for video segmentation in `src` folder.
