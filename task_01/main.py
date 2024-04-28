"""
Extract salary data from input txt file. 
Calculate total and average salary
"""

from pathlib import Path

def extract_salary(text: str) -> int:
    salary = 0
    for item in text.split(","):
        if item.strip().isnumeric():
            salary = int(item)
    return salary


def total_salary(path: str) -> tuple:
    total = 0
    average = 0
    empl_number = 0
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    total += extract_salary(line)
                    empl_number += 1
                average = int(total / empl_number)
            return total, average
        except IOError:
            print("Error: could not read file " + path.name)
    else:
        print(f"file {path.name} not found")


path = Path("salary_data.txt").absolute()

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

