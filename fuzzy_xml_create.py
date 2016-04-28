import os
import glob
import commands
import codecs

f = codecs.open("write.xml","w",'utf-8')
f.write("<add>")
f.write("<doc>")
tmp = glob.glob("*.csv")
pwd = commands.getoutput('pwd')
print pwd
for i in tmp:
    fuzzy = commands.getoutput("python /Users/nakamurajun/yamamoto15scis/prog/fuzzyhashing.py -b "+ pwd+"/"+i)
    print fuzzy
    fuzzy_split = fuzzy.split(" ")
    f.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>")
    f.write("<field name=\"filename\">"+fuzzy_split[1]+"</field>")
f.write("</add>")
f.write("</doc>")
