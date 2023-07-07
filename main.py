import gui
from cam_ctrl import cam_ctrl


class assistants():
    def __init__(self) -> None:
<<<<<<< HEAD
        self.pm = gui.models.photo_manager(r"photo_folder/N")
=======
        self.pm = gui.models.photo_manager(r"C:/Users/User/PycharmProjects/APSAP-undregraduate-research/APSAP-undergraduate-research/N")
>>>>>>> 62157f216a4d397307d9d9956a003e62c1c65345
        self.cc = cam_ctrl.cameraControl(tmp_dir="tmp/")


gui.views.GUImain.GUImain(assistants())
