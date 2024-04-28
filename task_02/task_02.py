"""
Extract cats info from input txt file. 
Careate list with info about every cat (dict: id, name, age)
"""


from pathlib import Path

def get_cats_info(path: str) -> list:
    list = []
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip().split(",")
                    list.append({"id": line[0], "name": line[1], "age": line[2]})
            return list
        except IOError:
            print("Error: could not read file " + path.name)
    else:
        print(f"file {path.name} not found")



path = Path("cats_file.txt").absolute()

cats_info = get_cats_info(path)
print(cats_info)