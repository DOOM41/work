# Python
import os


APPS = {
    'steam': 'C:\\Program Files (x86)\\Steam\\Steam.exe',
    'discord': 'C:\\Users\\duman\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe',
    'dota': 'steam://rungameid/570'
}


def open_file(file_name: str):
    try:
        paths: str = APPS[file_name]
        if file_name == 'discord':
            os.system(paths)
        else:
            os.startfile(paths)
        return True
    except Exception:
        return False
