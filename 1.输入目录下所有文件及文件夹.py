#获取当前Python程序的运行路径
import os
# print(os.getcwd())
# print(os.path.join("Myprojects","AI"))
# for i in os.listdir():
#     print(i,os.path.isdir(i))
for file in os.scandir():
    print(file.name,file.is_dir())
