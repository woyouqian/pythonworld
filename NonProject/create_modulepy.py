import time
import datetime
from os import path
from time import localtime


time_date = localtime()
info = time.asctime(time_date)
date = time.struct_time(time_date)
year_month_day = str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) 
# print(info, end='\t')
# print(year_month_day)

py_path = path.abspath('create_modulepy').rstrip('create_modulepy')
# print(py_path)
py_name = "\\mine" + year_month_day + '.py'
py_path += py_name
# print(py_path)

with open(py_path, 'w+') as file:
    file.write("# hello Python world!\n")
    file.write('# ')
    file.write(info)
    file.write('\n\n\n')
    file.write('if __name__ == "__main__":\n')
    file.write('    pass')
    file.write('\n\n')

if path.exists(py_path):
    print("Python module file has created success! The path is", end=' ')
    print(py_path)
else:
    print("Python module file create fail! Please confirm.")


if __name__ == "__main__":
    pass

