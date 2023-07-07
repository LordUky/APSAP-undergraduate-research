import gui
from cam_ctrl import cam_ctrl
from scale_read import scale_read

class assistants():
    def __init__(self) -> None:
        self.pm = gui.models.photo_manager(r"photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")
        self.sr = scale_read.scaleRead('COM10')

gui.views.GUImain.GUImain(assistants())
