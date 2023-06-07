# This module provides automation functions to aid photo automation
# to do: connect with GUI
import shutil
import os

def clear_folder(workpath:str, num:int):
    '''
    description: delete everything in path inputed
    '''
    for file in os.listdir(workpath):
        if file.name == str(num):
            os.remove(os.path.join(workpath,file))
    

def copy_and_paste(from_path:str, to_path:str, remove:bool=False, photo_format:str = ".jpg")->(int,int):
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
    sort_folder(to_path)

    #scan target folder and get new index  
    start_num = len(os.listdir(to_path))+1
    out_1 = start_num 

    # loop copy and paste files
    name_list_from = os.listdir(from_path)

    count = 1
    for file_name in name_list_from:
        # get full path name
        full_from_name = from_path + "\\"+file_name
        # create new folder
        directory1 = os.path.join(to_path,str(start_num))
        directory = os.path.join(to_path,str(start_num),"photos")
        if not os.path.exists(directory1):
            os.mkdir(directory1)
            os.mkdir(directory)
        # final dst path
        full_to_name = directory+f"\\{2-count%2}"+photo_format # front:1, back:2

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


def sort_folder(work_path:str)-> bool:
    '''
    Description: this function detects missing folders and sort them
    '''
    name_list = get_name_list(work_path)

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
                name_list = get_name_list(work_path)
        print("Sorted")
        return True


def get_name_list(work_path:str):
    '''
    A function used in sort_folder: return new file list (folder name converted to int)
    '''
    name_list = os.listdir(work_path)
    for i in range(len(name_list)):
        name_list[i] = int(name_list[i])  
    name_list.sort()  
    return name_list




# test
if __name__ == "__main__":
    # basic setting, will be given input from GUI
    from_path = "D:\\test\\working_temp" # set to be the same output folder as Canon APP
    ns = "N" # to do
    latitude = "38" #~
    context = "1" #~
    to_path = f"D:\\ararat\\files\\{ns}\\{latitude}\\478130\\4419430\\{context}\\finds\\individual"

    

    # copy and paste test
    result = copy_and_paste(from_path,to_path,False)
    print("Created folder from ",result[0]," to ",result[1])
    
