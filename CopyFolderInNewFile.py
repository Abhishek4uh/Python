import os, shutil
dict_ex={
    'python_ex':('.py'),
    'png_ex':('.png')
}
folderpath=input(('enter folder path'))
def file_find(folderpath,file_exten):
    files=[]
    for file in os.listdir(folderpath):
        for exten in file_exten:
            if file.endswith(exten):
                files.append((file))
    return files
#print(file_find(folderpath,ex))

for extype,extupe in dict_ex.items():
    foldername=extype.split('_')[0]+'Files'
    folder_path=os.path.join(folderpath,foldername)
    os.mkdir(folder_path)
    for item in (file_find(folderpath,extupe)):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.copy(item_path,item_new_path)

    # print('calling file finder')
    # print(file_find(folderpath,extupe))
