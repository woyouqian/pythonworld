import pytest
import os
from time import sleep


pytest.main(['.\\'])
sleep(5)

cmd1 = r'allure generate .\temp -o .\report\result2 --clean'
cmd2 = r'allure open .\report\result2'

# os.popen()
print('allure generate report in running...')
os.system(cmd1)
sleep(3)
# os.system(cmd2)
# print(cmd1)
# print(cmd2)
