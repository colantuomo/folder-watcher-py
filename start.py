import os
import shutil
import settings

basePath = settings.basePath

def readFolder():
    files = os.listdir(basePath)
    print('-- {} files found --'.format(len(files)))
    if hasFiles(files):
        manageFiles(files)
    else:
        print('== Empty folder - Nothing to move ==')

def hasFiles(files):
    return len(files) > 0

def manageFiles(files):
    for file in files:
        if isAImage(file):
            moveFile(file, 'imgs')
        if isSheet(file):
            moveFile(file, 'sheets')            

def moveFile(file, folder):
    newPath = '{}/{}'.format(basePath, folder)
    filePath = '{}/{}'.format(basePath, file)
    shutil.move(filePath, newPath)
    print(f'== "{file}" moving to {newPath} ==')

def isSheet(file):
    types = ['.xlsx', '.xls']
    return any(x in file for x in types)

def isAImage(file):
    types = ['.png', '.jpeg']
    return any(x in file for x in types)

readFolder()    