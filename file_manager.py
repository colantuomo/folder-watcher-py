import os
import shutil
import settings


def read_folder():
    files = [f for f in os.listdir(
        settings.get_base_path()) if os.path.isfile(os.path.join(settings.get_base_path(), f))]
    if _has_files(files):
        print(f'-- {len(files)} file(s) found --')
        _manage_files(files)
    else:
        print('== Empty folder - Nothing to move ==')


def _has_files(files):
    return len(files) > 0


def _manage_files(files):
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
    new_path = '{}/{}'.format(settings.get_base_path(), folder)
    file_path = '{}/{}'.format(settings.get_base_path(), file)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    shutil.move(file_path, new_path)
    print(f'FILE: [{file}] moving to: [{new_path}]')


def is_pdf(file):
    types = ['.pdf']
    return exists(file, types)


def is_video(file):
    types = ['.mp4']
    return exists(file, types)


def is_code(file):
    types = ['.js', '.html']
    return exists(file, types)


def is_compressed(file):
    types = ['.gz', '.zip', '.rar', '.7zip']
    return exists(file, types)


def is_sheet(file):
    types = ['.xlsx', '.xls', '.csv']
    return exists(file, types)


def is_image(file):
    types = ['.png', '.jpeg', '.jpg', '.svg']
    return exists(file, types)


def exists(file, types):
    return any(x in file for x in types)
