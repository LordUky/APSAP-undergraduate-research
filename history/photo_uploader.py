import requests
import shutil
import os
# import photo_automation_module as PAM

class photo_uploader:

    def __init__(self, workpath:str, username:str, password:str):
        # basic settings
        self.workpath = workpath
        api_url = "https://j20200007.kotsf.com/asl"
        params = {'username':username,'password':password}

        # connect to api and 
        api = requests.Session()
        self.api = api
        response = api.post(api_url, json=params)


        # check if connect successful
        if response.status_code == 200:
            # Extract the auth token from the response
            print("Connected successfully")
        else:
            print("Error: conenct failed")

        # return status code
        return response.status_code

    def upload(self):
        pass



    # def abandon(self, photo_num: int):
    #     '''Method to clear the temporary folder when click '''
    #     PAM.clear_floder(self.workpath, photo_num)

    def disconnect(self):
        '''Use this method to disconnect with api'''
        self.api.close()


if __name__ == "__main__":
    workpath = "D:/test/working_temp"
    uploader = photo_uploader(workpath,"autophoto","Armenia1")