import os
import shutil
import settings

def read_folder():
    files = os.listdir(settings.BASE_PATH)
    print(f'-- {len(files)} files found --')
    if has_files(files):
        manage_files(files)
    else:
        print('== Empty folder - Nothing to move ==')

def has_files(files):
    return len(files) > 0

def manage_files(files):
    for file in files:
        if is_image(file):
            move_file(file, 'imgs')
        if is_sheet(file):
            move_file(file, 'sheets')
        if is_compressed(file):
            move_file(file, 'compresseds')
        if is_code(file):
            move_file(file, 'codes')
        if is_video(file):
            move_file(file, 'videos')
        if is_pdf(file):
            move_file(file, 'pdfs')            

def move_file(file, folder):
    new_path = '{}/{}'.format(settings.BASE_PATH, folder)
    file_path = '{}/{}'.format(settings.BASE_PATH, file)
    shutil.move(file_path, new_path)
    print(f'== "{file}" moving to {new_path} ==')

def is_pdf(file):
    types = ['.pdf']
    return any(x in file for x in types)

def is_video(file):
    types = ['.mp4']
    return any(x in file for x in types)

def is_code(file):
    types = ['.js', '.html']
    return any(x in file for x in types)

def is_compressed(file):
    types = ['.gz', '.zip', '.rar', '.7zip']
    return any(x in file for x in types)

def is_sheet(file):
    types = ['.xlsx', '.xls', '.csv']
    return any(x in file for x in types)

def is_image(file):
    types = ['.png', '.jpeg', '.jpg', '.svg']
    return any(x in file for x in types)

read_folder()    