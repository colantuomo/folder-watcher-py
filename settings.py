import platform
# BASE_PATH = '/home/paulomartins/Downloads'
# BASE_PATH = 'C:/Users/Paulo/Downloads'

def get_base_path():
    if platform.system() == 'Windows': 
        return 'C:/Users/Paulo/Downloads'
    else:
        return '/home/paulomartins/Downloads'
        