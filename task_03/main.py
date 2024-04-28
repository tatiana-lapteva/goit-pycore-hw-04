"""
Display requested directory content, incl. nested directories
"""

import sys
from pathlib import Path
from show_folder_content import show_folder_content



if len(sys.argv) > 1:
    dir_path = sys.argv[1]
    dir_path = Path(dir_path).absolute()
    
    if dir_path.is_dir():
        show_folder_content(dir_path)
    else:
        print("Invalid path")

else:
    print("Entry directory path")


