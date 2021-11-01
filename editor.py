from PIL import ImageFont, ImageDraw
import json

class drawTextOnImage():
    def __init__(self, imagePath, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontType = "Truetype", fontExtension = ".ttf", fontColor = "black", fontSize = 15, anchorposition = None):
        #optional parameters
        self.fontFolderPath = fontFolderPath
        self.fontName = fontName    
        self.fontExtension = fontExtension                                       #defaults to ttf arial
        self.fontSize = fontSize                                                 #defaults to 15
        self.fontColor = fontColor                                               #defaults to black

        self.imagePath = imagePath                                               #the path to the image to edit
        fontPathName = self.fontFolderPath + self.fontName + self.fontExtension  #creates the entire path to the font out of the different parts

        self.draw = ImageDraw.Draw(self.imagePath)

        if(fontType == "Truetype"):
            self.font = ImageFont.truetype(fontPathName, self.fontSize)
        elif(fontType == "Bitmap"):
            self.font = ImageFont.load(fontPathName, self.fontSize)

    def drawTextOnImage(self, textList, xPosList, yPosList, color):
        for text in textList:
            for xPos in xPosList:
                for yPos in yPosList:
                    self.draw.text((xPos, yPos), text, color, font=self.font)

class Profilehandler():
    def __init__(self, pathToJson = ""):
        self.pathToJson = pathToJson
        profiles = []

    def addProfile(imagePath, textList, xPosList, yPosList, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):
        newProfile = Profile(imagePath, textList, xPosList, yPosList, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None)

class Profile():
    def __init__(self, imagePath, xPosList, yPosList, fontFolderPath = "C:\Windows\Fonts\\", fontName = "arial", fontExtension = ".ttf", fontSize = 15, anchorposition = None):

        self.fontFolderPath = fontFolderPath
        self.fontName = fontName
        self.fontExtension = fontExtension          #font path defaults to "C:\Windows\Fonts\arial.ttf", where "C:\Windows\Fonts\" is the windows standrart directory for font files
        self.fontSize = fontSize                    #font size defaults to 15           
        self.imagePath = imagePath                  #image path has to be input
        self.xPosList = xPosList
        self.yPosList = yPosList                    #List of y Posititons, corresponding with the same indexes on xPosList and textList to essentially make a 3d array holding text and anchorpoint

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

