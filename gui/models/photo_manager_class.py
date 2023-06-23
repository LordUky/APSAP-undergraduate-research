'''this is a tool class that stores the temporary photo path and destination path (in local mapping of remote server)'''
import os
import shutil

class photo_manager:
    '''
    property:
        _root_path: path of mapped remote (should be mapped to local driver), require initial set up first
        (following parameters are from scanning/manual input). e.g."D:/ararat/data/files/N"
        _from_path: path where photos are taken, fixed in this program
        _num1: first number
        _num2: second number
        _latitude: which latitude
        _context: context number
    '''
    def __init__(self, rp=r"D:/ararat/data/files/N", temp_photo_path="", num1="", num2="", latitude="", context="") -> None:
        # restore last working setting
        # eg.D:/ararat/data/files/N/38/478130/4419430/1/finds/individual/1/photos
        self._root_path = rp # path of mirrored remote drive
        self._from_path = temp_photo_path # path where the temporary photo is stored
        self._latitude = latitude  # latitude, optional
        self._num1 = num1 # first number, optional
        self._num2 = num2   #second number, optional
        self._context = context # context number, optioanl

        # scan the current folder
        ## -situation: no connection -> prompt for internet checking
        ## -situation: no path -> prompt for server system checking
        ## -situation: no previous path -> change the attributes to None type
        ## -situation: previous path exists -> pass

    # setter and getters for the class attributes
    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, rp):
        self._root_path = rp

    @property
    def latitude(self):
        return self._latitude
    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude
    
    @property
    def num1(self):
        return self._num1
    @num1.setter
    def num1(self, num1):
        self._num1 = num1
    
    @property
    def num2(self):
        return self._num2
    @num2.setter
    def num2(self, num2):
        self._num2 = num2
    
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context
    
    # *methods for this class*

    ## generate output path when all class variables are filled 
    def to_path(self):
        # check for completeness
        if self.root_path == "":
            raise NameError("Remote drive path not existing, please check")
        elif self._num1 == "":
            raise NameError("code1 not existing, please check")
        elif self._num2 == "":
            raise NameError("code2 number not existing, please check")
        elif self._latitude == "":
            raise NameError("Latitude not existing, please check")
        elif self._context == "":
            raise NameError("Context not existing, please check")
        elif self._indiv_num == "":
            raise NameError("Individual folder not existing, please check")
        else: # full path of remote link
            return f"{self.root_path}/{self._latitude}/{self._num1}/{self._num2}/{self._context}/finds/individual"

    ## move all photos from temp file to destination
    def copy_and_paste_photo(self):
        if self._from_path == "":
            raise NameError("Local photo path not existing, please check")
        self.copy_and_paste(self._from_path,self.to_path(),False)

    # *general functions*
    ## create new folder in remote drive
    def create_context(self, context_number):
        new_path = f"{self.root_path}/{self._latitude}/{self._num1}/{self._num2}/{context_number}/finds/individual"
        # examine if the path already exists
        if os.path.exists(new_path):
            return "Path already exist!!"
        try:
            os.makedirs(new_path)
            return "new context is created successfully"
        except:
            return "new context cannot be created, please retry"
        
    ## sub directories finder
    def find_sub_dir(self, path):
        '''This function returns a list of sub directories given a full path
            This can be used in pull up selection in GUI view
        '''
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return directories
    
    ## folder cleaner
    def clear_folder(self, workpath:str, num:int):
        '''
        description: delete everything in path inputed
        '''
        for file in os.listdir(workpath):
            if file.name == str(num):
                os.remove(os.path.join(workpath,file))
    # 
    def get_name_list(self, work_path:str):
        '''
        A function used in sort_folder: return new file list (folder name converted to int)
        '''
        name_list = os.listdir(work_path)
        for i in range(len(name_list)):
            name_list[i] = int(name_list[i])  
        name_list.sort()  
        return name_list

    # 
    def sort_folder(self, work_path:str)-> bool:
        '''
        Description: this function detects missing folders and sort them
        '''
        name_list = self.get_name_list(work_path)

        if len(name_list) == max(name_list):
            print("No missing")  # to do: change to return
            return False
        else:
            it = range(len(name_list))
            for idx in it:
                os.chdir(work_path)
                if idx + 1 == name_list[idx]:  
                    pass
                else:
                    os.rename(f"{str(name_list[idx])}",f"{str(idx+1)}")
                    name_list = self.get_name_list(work_path)
            print("Sorted")
            return True
            
    ## file mover
    def copy_and_paste(self,  from_path:str, to_path:str, remove:bool=False, photo_format:str = ".jpg"):
        '''
        input: 
            from_path: working folder path, should have a default value
            to_path: share folder path
            remove: false = only copy; true: cut
            photo_format: the format of file
        return: file numbers in destination that is modified
        description: this function copy batch files from path to path, make sure working path 
        is empty

        ''' 
        #must do sort before copy and paste
        self.sort_folder(to_path)

        #scan target folder and get new index  
        start_num = len(os.listdir(to_path))+1
        out_1 = start_num 

        # loop copy and paste files
        name_list_from = os.listdir(from_path)

        count = 1
        for file_name in name_list_from:
            # get full path name
            full_from_name = from_path + "/"+file_name
            # create new folder
            directory1 = os.path.join(to_path,str(start_num))
            directory = os.path.join(to_path,str(start_num),"photos")
            if not os.path.exists(directory1):
                os.mkdir(directory1)
                os.mkdir(directory)
            # final dst path
            full_to_name = directory+f"/{2-count%2}"+photo_format # front:1, back:2

            # copy and paste
            if os.path.isfile(full_from_name):
                shutil.copy(full_from_name,full_to_name)
                # delete original files
                if remove == True:
                    try:
                        os.remove(full_from_name)
                    except OSError as e:
                    # If it fails, inform the user.
                        print("Error: %s - %s." % (e.filename, e.strerror))
            # only update start_num when 
            if count%2 == 0:
                start_num += 1
            # next file name
            count += 1

        return (out_1,start_num-1)
    





# test
if __name__ == "__main__":
    # basic setting, will be given input from GUI
    from_path = "D:/test/working_temp" # set to be the same output folder as Canon APP
    ns = "N" # to do
    latitude = "38" #~
    context = "1" #~
    to_path = f"D:/ararat/files/N/{latitude}/478130/4419430/{context}/finds/individual"

    

    # copy and paste test
    

