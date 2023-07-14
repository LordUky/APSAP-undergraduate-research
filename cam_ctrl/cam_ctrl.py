import os
import subprocess
from PIL import Image
import io
import platform

class cameraControl:
    _DEBUG = False
    lv_process = None

    def __init__(self, tmp_dir = "/tmp/") -> None:
        # assume tmp_fp is empty
        self.tmp_dir = tmp_dir
        self.count = 0

    def start_lv(self):
        self.lv_process = subprocess.Popen(["gphoto2", "--capture-movie", "--stdout"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get_lv_frame(self):
        out_list = []
        while True:
            out = self.lv_process.stdout.readline()
            out_list.append(out)
            if b"\xff\xd9" in out:
                break
        out = b"".join(out_list)
        if platform.system() == "Windows":
            out = out.replace(b"\x0d\x0a", b"\x0a")
        return Image.open(io.BytesIO(out))
    
    def stop_lv(self):
        self.lv_process.kill()

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
            _cmd = "cp cam_ctrl/aaa.jpg {}".format(fp)
            print("CP COMMAND:", _cmd)
            os.system(_cmd)
            return 0
        ret = os.system("gphoto2 --capture-image-and-download --filename={} --force-overwrite".format(fp))
        return ret
    
if __name__ == "__main__":
    from time import time
    cc = cameraControl("tmp/")
    
    t0 = time()
    for i in range(10):
        cc.capture_preview()
    t1 = time()
    print((t1 - t0) / 10)
