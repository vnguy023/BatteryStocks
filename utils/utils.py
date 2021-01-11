import os.path
from os import path

from utils.textColor import TextColor

TEMP_DIRECTORY_PATH = "temp"
TEMP_PATH = os.path.join("",TEMP_DIRECTORY_PATH)
EPOCH_FILENAME = "epochLastUpdated.txt"
EPOCH_FILE_PATH = os.path.join(TEMP_DIRECTORY_PATH,EPOCH_FILENAME)

os.makedirs(TEMP_PATH, exist_ok=True)

def getLastUpdateEpochTime():
    if ( not( os.path.isdir(TEMP_PATH) and os.path.isfile(EPOCH_FILE_PATH))):
        return 0

    epochFile = open(EPOCH_FILE_PATH)
    epochTime = epochFile.read()
    
    return int(epochTime)

def setLastUpdateEpochTime(value):
    epochFile = open(EPOCH_FILE_PATH, "w")
    epochFile.write(str(value))
    epochFile.close

def getFileData(filePath:str):
    fp = os.path.join("", filePath)

    if not os.path.isfile(fp):
        return ""

    file = open(fp)
    data = file.read()

    return data

def getStrValueOutput(value:str, defaultColor: TextColor = TextColor.CWHITE ,valueColor: TextColor = TextColor.CWHITE):
    output = defaultColor + "[" + valueColor +"{value}".format(value=value) + defaultColor + "]" + TextColor.CEND
    return output

def getStrKeyValueOutput(key:str, value:str, defaultColor: TextColor = TextColor.CWHITE ,valueColor: TextColor = TextColor.CWHITE):
    output = defaultColor + "[{key}:".format(key=key) + valueColor +"{value}".format(key=key, value=value) + defaultColor + "]" + TextColor.CEND
    return output

def getDecimalStr(number):
    return '{0:,.2f}'.format(number)