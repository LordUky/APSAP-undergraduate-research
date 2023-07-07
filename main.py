import gui
from scale_read.scale_read import scaleRead
from cam_ctrl import cam_ctrl


class assistants():
    def __init__(self) -> None:
        self.pm = gui.models.photo_manager(r"photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")
        self.scaleReader = scaleRead()


gui.views.GUImain.GUImain(assistants())
