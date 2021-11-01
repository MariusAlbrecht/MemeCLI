# dependencies

uses [Pillow](https://pillow.readthedocs.io/en/stable/index.html) for the image manipulation (aka text drawing) and [argparse](https://docs.python.org/3/library/argparse.html) for the cli interaction and parsing

# how it works

the tool is split into two parts:

- the `drawTextOnImage` class and function in the `editor.py` file, which handle the drawing itself and
- the `main.py` file which handles profiles and the actual meme creation

## drawTextOnImage

the `drawTextOnImage` class and function basically just use the Pillow `ImageFont` and `ImageDraw` modules to initiate a an object that can be used to draw in the given image and a font.

`imagePath` specifies the path to the image, the text is suppes to be added onto

`fontFolderPath` specifies the Folder, in which the font that is suppsed to be used is located in and is optional.

`fontName` specifies the font name (without file extension)

`fontExtension` specifies the file extension, as multiple different extensions can be used (see [here](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html) for more info on the options)

`fontSize` specifies the font size

`anchorposition` specifies the anchor position of the text that is beinfg edited onto the image (see [here](https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors) for the options and an explanation fo them)

all paramaters but the `imagePath` are optional and default to C:\Windows\Fonts\arial.ttf at size 15. Separating the parts of the font path can be useful, expecially because the folder probably stays the same, while font name and extension may change more often. This gets rid of redundancy.

