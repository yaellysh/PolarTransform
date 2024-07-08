# PolarTransform

A program that allows you to convert ultrasound images into a human understandable format.

## Description

We we provided with ultrasound image data in a format not easily understandable by the human eye. Each ultrasound frame was formatted in the Cartesian coordinate system whereas the typical ultrasound image is in the form of a sector scan, a shape created through a polar transformation. As well as this, the untrasound was combined into one 416x3840 image contained 80 individual frames. Each frame had to be spliced out of this combined image and rotated before being warped using a polar transformation. 

As well as this, the original image and therefore the individual frames were not high enough in quality to produce a high resolution image. To resolve this, once the frames were split they had to be enlarged through interpolation to ensure that the final ultrasound images were of high enoguh quality without any missing pixels or noise. 
## Getting Started

### Dependencies

* [numpy](https://numpy.org) (used for converting image to array and manipulating)
* [OpenCV/ cV2](https://pypi.org/project/opencv-python/) (used for interpolation)
* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

### Installing

Files required:
   * main.py (original, without multiprocessing) or main2.py (with multiprocessing)
   * image_split.py
   * polar_transform.py

### Executing program

* Run either of the main programs with the following parameters:
  * The path to the .raw file containing the original 80 frames
  * The scale factor, an integer value that impacts how high-quality the resulting image is
       * A SF of around 10 will have a good amount of noise but the images will be outputted within 2 minutes
       * A SF in the 25-30 will have significantly less noise, even none but producing the images will take significantly longer (closer to 10 minutes)

e.g.
```
python3 main2 '/Users/username/folder/original_image.raw' 30
```

## Help

## Authors

Yael Lyshkow

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration
* [addisonElliott/polarTransform](https://github.com/addisonElliott/polarTransform/tree/master/polarTransform)
