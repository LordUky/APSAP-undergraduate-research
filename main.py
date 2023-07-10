import gui
from cam_ctrl import cam_ctrl
from scale_read import scale_read
import sys

class assistants():
    def __init__(self) -> None:
        self.pm = gui.models.photo_manager(r"photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")
        com_port = sys.argv[1]
        self.sr = scale_read.scaleRead(com_port)
        self.cp = 0 # current page. 0:login; 1:firstPage; ......

gui.views.GUImain.GUImain(assistants())
