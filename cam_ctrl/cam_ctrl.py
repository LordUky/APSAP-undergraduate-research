import os

class cameraControl:
    _DEBUG = True
    def __init__(self, tmp_dir = "/tmp/") -> None:
        # assume tmp_fp is empty
        self.tmp_dir = tmp_dir
        self.count = 0

    def capture_preview(self) -> str:
        """
        If success, return image file path.
        If fail, return None.
        """
        if self._DEBUG:
            return "cam_ctrl/aaa.jpg"
        cpf = "{}.jpg".format(self.count)
        if (os.system("gphoto2 --capture-preview --filename={} --force-overwrite".format(self.tmp_dir + cpf)) != 0):
            return None
        self.count += 1
        return self.tmp_dir + "thumb_" + cpf

    def capture_image_and_download(self, fp):
        if self._DEBUG:
            os.system("cp cam_ctrl/aaa.jpg {}".format(fp))
            return
        # @TODO capture and download format according to ext. name in fp
        ext_name = fp[-3 : ].lower()
        ret = None
        if (ext_name == 'jpg'):
            ret = os.system("gphoto2 --capture-image-and-download --filename={} --force-overwrite".format(fp))
        elif (ext_name == 'cr2'):
            # capture and download RAW
            pass
        return ret
    
if __name__ == "__main__":
    from time import time
    cc = cameraControl("tmp/")
    
    t0 = time()
    for i in range(10):
        cc.capture_preview()
    t1 = time()
    print((t1 - t0) / 10)
