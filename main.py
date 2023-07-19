import gui
from cam_ctrl import cam_ctrl
from scale_read import scale_read
import sys
import random
from API.API import API


class assistants():
    def __init__(self) -> None:
        self.api = API("https://j20200007.kotsf.com/asl/")
        self.pm = gui.models.photo_manager(r"../photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="../tmp/", debug=False)
        self.sr = None
        self.cp = 0  # current page. 0:login; 1:firstPage; ......
        self.fc = {'combo1': None, 'combo2': None, 'combo3': None, 'combo4': None}
        self.surprise = True
        self.bgColor = 'white'
        self.pic_taken = False
        self.colors = ['LightPink', 'Pink', 'Crimson', 'LavenderBlush', 'PaleVioletRed', 'HotPink', 'DeepPink', 'MediumVioletRed', 'Orchid', 'Thistle', 'Plum', 'Violet', 'Magenta', 'Fuchsia', 'DarkMagenta', 'Purple', 'MediumOrchid', 'DarkViolet', 'DarkOrchid', 'Indigo', 'BlueViolet', 'MediumPurple', 'MediumSlateBlue', 'SlateBlue', 'DarkSlateBlue', 'Lavender', 'GhostWhite', 'Blue', 'MediumBlue', 'MidnightBlue', 'DarkBlue', 'Navy', 'RoyalBlue', 'CornflowerBlue', 'LightSteelBlue', 'LightSlateGray', 'SlateGray', 'DodgerBlue', 'AliceBlue', 'SteelBlue', 'LightSkyBlue', 'SkyBlue', 'DeepSkyBlue', 'LightBlue', 'PowderBlue', 'CadetBlue', 'Azure', 'LightCyan', 'PaleTurquoise', 'Cyan', 'Aqua', 'DarkTurquoise', 'DarkSlateGray', 'DarkCyan', 'Teal', 'MediumTurquoise', 'LightSeaGreen', 'Turquoise', 'Aquamarine', 'MediumAquamarine', 'MediumSpringGreen', 'MintCream', 'SpringGreen', 'MediumSeaGreen', 'SeaGreen', 'Honeydew', 'LightGreen', 'PaleGreen', 'DarkSeaGreen', 'LimeGreen', 'Lime', 'ForestGreen', 'Green', 'DarkGreen', 'Chartreuse', 'LawnGreen', 'GreenYellow', 'DarkOliveGreen', 'YellowGreen', 'OliveDrab', 'Beige', 'LightGoldenrodYellow', 'Ivory', 'LightYellow', 'Yellow', 'Olive', 'DarkKhaki', 'LemonChiffon', 'PaleGoldenrod', 'Khaki', 'Gold', 'Cornsilk', 'Goldenrod', 'DarkGoldenrod', 'FloralWhite', 'OldLace', 'Wheat', 'Moccasin', 'Orange', 'PapayaWhip', 'BlanchedAlmond', 'NavajoWhite', 'AntiqueWhite', 'Tan', 'BurlyWood', 'Bisque', 'DarkOrange', 'Linen', 'Peru', 'PeachPuff', 'SandyBrown', 'Chocolate', 'SaddleBrown', 'Seashell', 'Sienna', 'LightSalmon', 'Coral', 'OrangeRed', 'DarkSalmon', 'Tomato', 'MistyRose', 'Salmon', 'Snow', 'LightCoral', 'RosyBrown', 'IndianRed', 'Red', 'Brown', 'FireBrick', 'DarkRed', 'Maroon', 'White', 'WhiteSmoke', 'Gainsboro', 'LightGrey', 'Silver', 'DarkGray', 'Gray', 'DimGray']

    def getRandomColor(self):
        return random.choice(self.colors)


gui.views.GUImain.GUImain(assistants())
