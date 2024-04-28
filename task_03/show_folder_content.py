
from pathlib import Path
from colorama import Fore


def select_color(string: str, type: str) -> str:
    """ 
        return string colored according to provided type
    """
    if type == "folder":
        return Fore.BLUE + string
    elif type == "file":
        return Fore.GREEN + string
    else:
        return string



def show_folder_content(path: Path) -> str:
    '''
        loop folders and shows folder structure, incl nested folders
    '''
    indentation = "   "
    
    def loop_folder(folder_path: Path, indent_counter: int) -> str:
        nonlocal indentation
        for item in folder_path.iterdir():
            if item.is_dir():
                print(f"{indentation * (indent_counter)} {select_color(item.name, "folder")}/")
                loop_folder(item, indent_counter+1)
            else:
                print(f"{indentation * (indent_counter + 1)} {select_color(item.name, "file")}")
    
    print(f"{select_color(path.name, "folder")}/")
    if path.is_dir:
        loop_folder(path, 0)
    