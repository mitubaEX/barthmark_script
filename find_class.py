import os
import sys
import glob

param = sys.argv
tmp = []
os.chdir(param[1])
def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in fild_all_files(param[1]):
    tmp.append(file)
for i in tmp:
    if ".jar" in i:
        print i
        os.system("jar xvf "+ i)
