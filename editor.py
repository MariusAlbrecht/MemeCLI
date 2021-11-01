from PIL import ImageFont, ImageDraw
import json

class drawTextOnImage():
    def __init__(self, imagePath, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):
        #optional parameters
        self.fontFolderPath = fontFolderPath
        self.fontName = fontName
        self.fontExtension = fontExtension                                      #defaults to ttf arial
        self.fontSize = fontSize                                                # defaults to 15

        self.imagePath = imagePath                                              #the path to the image to edit
        fontPathName = self.fontFolderPath + self.fontName + self.fontExtension  #creates the entire path to the font out of the different paths

        self.draw = ImageDraw.Draw(self.imagePath)
        self.font = ImageFont.truetype(fontPathName, self.fontSize)

    def drawTextOnImage(self, x, y, text):
        self.draw.text((10, 25), "world", font=self.font)

class Profilehandler():
    def __init__(self, pathToJson = ""):
        self.pathToJson = pathToJson
        profiles = []

    def addProfile(imagePath, textXposYposArray, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):
        newProfile = Profile(imagePath, textXposYposArray, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None)

    def profileHandler(profileID = 0):
        a

class Profile():
    def __init__(self, imagePath, textXposYposArray, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):

        self.fontFolderPath = fontFolderPath
        self.fontName = fontName
        self.fontExtension = fontExtension          #font path defaults to "C:\Windows\Fonts\arial.ttf", where "C:\Windows\Fonts\" is the windows standrart directory for font files
        self.fontSize = fontSize                    #font size defaults to 15           
        self.imagePath = imagePath                  #image path has to be input
        self.textXposYposArray = textXposYposArray  #3D Aray that holds text, and corresponding anchorpoints (with x and y pos)

        profileArray = []

        jsonInput = {
            self.fontFolderPath,
            self.fontName,
            self.fontExtension,
            self.fontSize,         
            self.imagePath,
            self.textXposYposArray
        }
        profileArray.append(jsonInput)

        with open("profiles.json", "w") as jsonFile:
            json.dump(profileArray[len(profileArray)], jsonFile)
