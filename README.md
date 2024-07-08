# PolarTransform

A program that allows you to convert ultrasound images into a human understandable format.

## Description

We we provided with ultrasound image data in a format not easily understandable by the human eye. Each ultrasound frame was formatted in the Cartesian coordinate system whereas the typical ultrasound image is in the form of a sector scan, a shape created through a polar transformation. As well as this, the untrasound was combined into one 416x3840 image contained 80 individual frames. Each frame had to be spliced out of this combined image and rotated before being warped using a polar transformation. 

As well as this, the original image and therefore the individual frames were not high enough in quality to produce a high resolution image. To resolve this, once the frames were split they had to be enlarged through interpolation to ensure that the final ultrasound images were of high enoguh quality without any missing pixels or noise. 
## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
