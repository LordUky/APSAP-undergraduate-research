import flurl
from flurl import http
import io
import json
import os
import requests
import shutil
import tempfile
import traceback

class API:
    """
    A class for interacting with the API of a web application.

    Attributes:
        _baseurl (str): The base URL of the API.
    """

    def __init__(self):
        """
        Initializes a new instance of the API class.
        """
        self._baseurl = os.environ.get('BASE_URL') or 'http://aslcv2'

    def login(self, username, password):
        """
        Logs in to the web application with the given username and password.

        Args:
            username (str): The username to use for authentication.
            password (str): The password to use for authentication.

        Returns:
            str: The authentication token for the logged-in user, or None if the login failed.
        """
        url = self._baseurl.append_path_segment('auth-token') + '/'
        response = url.post_json({
            'username': username,
            'password': password
        })
        if response.status_code == 200:
            token = AuthToken.from_json(response.text)
            return token.token
        else:
            print(response.text)
            return None

    def get_current_token(self):
        """
        Gets the current authentication token for the logged-in user.

        Returns:
            str: The authentication token for the logged-in user.
        """
        return 'Token ' + os.environ['AUTH_TOKEN']

    def get_spatial_contexts(self):
        """
        Gets a list of the available spatial contexts in the web application.

        Returns:
            list: A list of SpatialContext objects representing the available spatial contexts.
        """
        token = self.get_current_token()
        context_list_url = self._baseurl.append_path_segment('api/context') + '/'
        response = context_list_url.with_header('Authorization', token).get()
        contexts = []
        if response.status_code == 200:
            contexts = [SpatialContext.from_json(c) for c in response.json()]
        return contexts

    def get_object_finds(self, spatial_context):
        """
        Gets a list of object finds in the specified spatial context.

        Args:
            spatial_context (SpatialContext): The spatial context to get object finds for.

        Returns:
            list: A list of ObjectFind objects representing the object finds in the specified spatial context.
        """
        token = self.get_current_token()
        url = self._baseurl.append_path_segment('api/find').append_path_segments(
            spatial_context.utm_hemisphere,
            spatial_context.utm_zone,
            spatial_context.area_utm_easting_meters,
            spatial_context.area_utm_northing_meters,
            spatial_context.context_number
        ) + '/'
        response = url.with_header('Authorization', token).get()
        if response.status_code == 200:
            root = ObjectFindRoot.from_json(response.text)
            finds = root.results
            i = 0
            while len(finds) < root.count and i < 20:
                next_url = root.next
                response = requests.get(next_url, headers={'Authorization': token})
                if response.status_code == 200:
                    root = ObjectFindRoot.from_json(response.text)
                    finds += root.results
                i += 1
            finds = sorted(finds, key=lambda x: x.find_number, reverse=True)
            return finds
        else:
            print(response.text)
            return []

    def create_object_find(self, data):
        """
        Creates a new object find with the specified data.

        Args:
            data (dict): The data for creating the object find.
        """

