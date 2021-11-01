from PIL import ImageFont, ImageDraw

class drawTextOnImage():
    def __init__(self, imagePath, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):
        #optional parameters
        self.fontFolderPath = fontFolderPath
        self.fontName = fontName
        self.fontExtension = fontExtension                                      #defaults to ttf arial
        self.fontSize = fontSize                                                # defaults to 15

        self.imagePath = imagePath                                              #the path to the image to edit
        self.fontPathName = self.fontFolderPath + self.fontName + self.fontExtension  #creates the entire path to the font out of the different paths

        self.draw = ImageDraw.Draw(self.imagePath)
        self.font = ImageFont.truetype(self.fontPathName, self.fontSize)

    def drawTextOnImage(self, x, y, text):
        self.draw.text((10, 25), "world", font=self.font)
