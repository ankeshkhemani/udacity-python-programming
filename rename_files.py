import os

def rename_files(folder_name):
    file_list=os.listdir(folder_name)
    print file_list
    os.chdir(folder_name)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    
rename_files(r"/Users/ankeshkhemani/Dropbox/Projects/prank")
