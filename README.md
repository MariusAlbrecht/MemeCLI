# dependencies

uses [Pillow](https://pillow.readthedocs.io/en/stable/index.html) for the image manipulation (aka text drawing) and [argparse](https://docs.python.org/3/library/argparse.html) for the cli interaction and parsing

# Features

- drawing text (one or multiple blocks), in different colours and positions
- profiles for saving fonts, positions for text to be added to and meme template path so that one only has to add the text to create a meme with that template path

## drawTextOnImage

the `drawTextOnImage` class and function basically just use the Pillow `ImageFont` and `ImageDraw` modules to initiate an object that can be used to draw in the given image and a font.

`imagePath` specifies the path to the image, the text is suppes to be added onto

`fontFolderPath` specifies the Folder, in which the font that is suppsed to be used is located in and is optional.

`fontName` specifies the font-File name (without file extension, e.g. if the font file is named "foo.ttf" the correct fontName would be "foo")

`fontExtension` specifies the file extension, as multiple different extensions can be used (see [here](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html) for more info on the options)

`fontColor` specifies color. Supports lots of formats, see [here](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names) for the options

`fontSize` specifies the font size

`anchorposition` specifies the anchor position of the text that is beinfg edited onto the image (see [here](https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors) for the options and an explanation fo them)

all paramaters but the `imagePath` are optional and default to C:\Windows\Fonts\arial.ttf at size 15. Separating the parts of the font path can be useful, expecially because the folder probably stays the same, while font name and extension may change more often. This gets rid of redundancy.

##Profiles

# NOTE THAT THIS DOES NOT AT ALL WORK YET