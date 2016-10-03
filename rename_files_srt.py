import os

def rename_files(folder_name):
    file_list=os.listdir(folder_name)
    print file_list
    os.chdir(folder_name)
    for file_name in file_list:
        if (file_name[-3::] == "vtt"):
            os.rename(file_name,"index"+file_name[9::])
    
rename_files(r"/Users/ankeshkhemani/Downloads")
