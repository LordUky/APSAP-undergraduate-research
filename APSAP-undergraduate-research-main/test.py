import os

folder_path = "D:\Jupyter notebooks\APSAP" # replace with the path to the folder you want to iterate over


directories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
print(directories)
