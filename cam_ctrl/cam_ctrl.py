import os
import subprocess
from PIL import Image
import io
import platform
import threading

class cameraControl:
    _DEBUG = False
    
    lv_process = None
    lv_thread = None

    lv_frame = None
    lv_update_running = False
    LV_UPDATE_TIMEOUT = 0.5  # second
    LV_UPDATE_CHUNK = 1024  # bytes

    def __init__(self, tmp_dir = "/tmp/") -> None:
        # assume tmp_fp is empty
        self.tmp_dir = tmp_dir
        self.count = 0

    # def start_lv(self):
    #     self.lv_process = subprocess.Popen(["gphoto2", "--capture-movie", "--stdout"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # def get_lv_frame(self):
    #     out_list = []
    #     # wait for starting bytes FF D8
    #     while True:
    #         out = self.lv_process.stdout.readline()
    #         idx = out.find(b"\xff\xd8")
    #         if (idx != -1):
    #             out_list.append(out[idx : ])
    #             break

    #     # wait for starting bytes FF D9
    #     while True:
    #         out = self.lv_process.stdout.readline()
    #         idx = out.find(b"\xff\xd9")
    #         if (idx == -1):
    #             out_list.append(out)
    #         else:
    #             out_list.append(out[ : idx + 2])
    #             break

    #     out = b"".join(out_list)
    #     if platform.system() == "Windows":
    #         out = out.replace(b"\x0d\x0a", b"\x0a")
    #     print("\n=====\n")
    #     print(out)
    #     return Image.open(io.BytesIO(out))

    # def stop_lv(self):
    #     if (self.lv_process != None):
    #         self.lv_process.kill()
    #     self.lv_process = None


    def start_lv(self):
        self.lv_process = subprocess.Popen(["gphoto2", "--capture-movie", "--stdout"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        self.lv_update_running = True
        self.lv_thread = threading.Thread(target=self._update_lv_frame)
        self.lv_thread.start()

    def _update_lv_frame(self):
        out_list = []
        while self.lv_update_running:
            out = self.lv_process.stdout.read(self.LV_UPDATE_CHUNK)
            sof_idx = out.find(b"\xff\xd8")
            eof_idx = out.find(b"\xff\xd9")
            
            if (eof_idx != -1 and out_list != []):  # end of frame exists, and outlist not empty
                out_list.append(out[ : eof_idx + 2])
                frame_bytes = b"".join(out_list)
                if platform.system() == "Windows":
                    frame_bytes = frame_bytes.replace(b"\x0d\x0a", b"\x0a")
                try:    
                    self.lv_frame = Image.open(io.BytesIO(frame_bytes))
                except:
                    pass
                out_list = []

            if (sof_idx != -1):  # start of frame exists
                out_list = []
                out_list.append(out[sof_idx : ])
            
            if (sof_idx == -1 and eof_idx == -1 and out_list != []):  # interval bytes, and outlist not empty
                out_list.append(out)

    def get_lv_frame(self):
        return self.lv_frame
    
    def stop_lv(self):
        if (self.lv_process != None):
            self.lv_process.kill()
            self.lv_process = None
        if (self.lv_thread != None):
            self.lv_update_running = False
            self.lv_thread.join()
            self.lv_thread = None

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
    cc = cameraControl()
    cc.start_lv()

    import time
    try:
        for i in range(10):
            img = cc.get_lv_frame()
            # print(img)
            img.show()
            time.sleep(0.5)
    except Exception as e:
        print(e)
        exit()
    finally:
        cc.stop_lv()