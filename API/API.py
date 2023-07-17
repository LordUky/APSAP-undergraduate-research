# this test changes from test3

import requests

class API:
    # initiation function
    def __init__(self,base_url,isTest:bool=True) -> None:
        self.base_url = base_url
        self.isTest = isTest
        self.session = requests.Session()

    # get data
    def login(self,username,password):
        # send and check
        data = {'username':username,
                'password':password}
        url_login = self.base_url + "auth-token/"
        response = self.session.post(url_login,data=data)
        if response.status_code == 200:
            print("Login successful")
            token = response.json()['token']
            # print("Current toke = ",token)
            self.token = token

        else:
            print(response.status_code)
            print(response.text)                
    
    # post data into database
    def create_find(self,data:dict):
        headers = {'Authorization': f'Token {self.token}'}
        api_url = self.base_url + "api/find/"

        response = self.session.post(api_url, data= data, headers= headers)
        print(response.text)

        if response.status_code == 201:
            print("New finds added")
        else: 
            print(response.status_code)
            print("Add failed")
        

if __name__ == "__main__":
    # test website url
    base_url = "https://j20200007.kotsf.com/asl/"
    
    # parameters for login purpose
    username = 'autophoto'
    password = 'Armenia1'

    # test data for creating finds
    data = {
        'utm_hemisphere':'N',
        'utm_zone':38,
        'area_utm_easting_meters':478230,
        'area_utm_northing_meters':4419430,
        'context_number':1,
        'material':'pottery', # user input
        'category':'rim' # user input
    }
    # list of material and category combinations (material,catgegory)
    # ('pottery','body') ('pottery','rim') ('pottery','base') ('pottery','handle')
    # ('pottery','spout') ('metal','nail')

    api = API(base_url)
    api.login(username=username,password=password)
    api.create_find(data)
    