import os

path = os.path.dirname(__file__)


def UsePic(picName):
    picPath = path + "/" + picName
    return picPath

