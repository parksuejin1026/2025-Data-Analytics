
import csv

try:
    with open('subwaytime.csv', encoding='cp949') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i < 5:
                print(f"Row {i}: {row}")
            else:
                break
except Exception as e:
    print(e)
