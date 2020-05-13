import os
import shutil

basePath = '/home/paulomartins/Personal/move-folders-test'
path = basePath + '/old-folder'

def readFolder():
    files = os.listdir(path)
    if hasFiles(files):
        manageFiles(files)
    else:
        print('== Nothing to move ==')

def hasFiles(files):
    return len(files) > 0

def manageFiles(files):
    for file in files:
        if isAImage(file):
            moveFile(file, 'new-folder')

def moveFile(file, folder):
    newPath = '{}/{}'.format(basePath, folder)
    filePath = '{}/{}'.format(path, file)
    shutil.move(filePath, newPath)
    print(f'== "{file}" moving to {newPath} ==')

def isSheet():
    return file.find('.xls') != -1

def isAImage(file):
    return file.find('.png') != -1

readFolder()    