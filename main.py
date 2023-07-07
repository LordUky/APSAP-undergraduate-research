import gui
from cam_ctrl import cam_ctrl


class assistants():
    def __init__(self) -> None:
        self.pm = gui.models.photo_manager(r"photo_folder/N")
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")


gui.views.GUImain.GUImain(assistants())
