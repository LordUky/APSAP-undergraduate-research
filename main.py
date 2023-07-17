import gui
from cam_ctrl import cam_ctrl
from scale_read import scale_read
import sys


class assistants():
    def __init__(self) -> None:
        self.pm = gui.models.photo_manager(r"photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")
        if len(sys.argv) == 1:
            com_port = 'x'
        else:
            com_port = sys.argv[1]
        self.sr = scale_read.scaleRead(com_port, debug=(com_port == "x"))
        self.cp = 0  # current page. 0:login; 1:firstPage; ......
        self.fc = {'combo1': None, 'combo2': None, 'combo3': None, 'combo4': None}


gui.views.GUImain.GUImain(assistants())
