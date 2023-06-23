import gphoto2 as gp
from PIL import Image
import io
import time
# @TODO: Not fully tested yet.


class cameraControl:
    camera = None
    config = None

    def __init__(self):
        pass

    def initialize_camera(self) -> bool:
        """
        Initialize camera
        @return: 0 if success, 1 if fail
        """
        self.camera = gp.Camera()
        try:
            self.camera.init()
            self.config = self.camera.get_config()
            return 0
        except Exception as e:
            print(e)
            return 1

    def get_config_tree(self):
        """
        Get configure tree
        @return: dict like {type: {config: [option, ...], ...}, ...}
        """
        ret = {}
        for child in self.config.get_children():
            child_dict = {}
            for _c in child.get_children():
                try:
                    print(_c.get_name(), _c.count_choices())
                    child_dict.update({_c.get_name(): list(_c.get_choices())})
                except Exception as e:
                    print(e)
            ret.update({child.get_name(): child_dict})
        return ret

    def set_config_tree(self, config_tree):
        """
        Set configure tree
        @param config_tree: dict like {type: {config: option, ...}, ...}
        """
        for _c in config_tree.values():
            for name in _c:
                self.config.get_child_by_name(name).set_value(_c[name])
        self.camera.set_config(self.config)

    # def capture_preview(self):
    #     """
    #     Capture preview fram
    #     @return: PIL Image object
    #     """
    #     try:
    #         self.initialize_camera()
    #         buf = self.camera.capture_preview().get_data_and_size()
    #         self.exit_camera()
    #         img = Image.open(io.BytesIO(buf))
    #         return img
    #     except Exception as e:
    #         print("cap prev err:", e)
    #         return None

    def capture_download(self, fp: str):
        """
        Capture and then save to fp
        """
        try:
            file_path = self.camera.capture(gp.GP_CAPTURE_IMAGE)
            self.camera.file_get(
                file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL).save(fp)
            return 0
        except:
            return 1

    def exit_camera(self):
        self.camera.exit()


# unit test
if __name__ == '__main__':
    # initialize camera
    cc = cameraControl()
    print("Initialize camera: ", cc.initialize_camera())

    input(">>> ")

    cc.capture_download("aaa.jpg")
