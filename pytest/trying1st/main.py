import os
from time import sleep


cmd1 = r'allure generate .\temp -o .\report\result2 --clean'
cmd2 = r'allure open .\report\result2'

# os.popen()
os.system(cmd1)
sleep(5)
os.system(cmd2)
# print(cmd1)
# print(cmd2)
