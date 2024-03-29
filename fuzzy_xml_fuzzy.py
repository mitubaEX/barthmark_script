import os
import glob
import commands
import codecs

cvfv = codecs.open("cvfv.xml","w",'utf-8')
fmc = codecs.open("fmc.xml","w",'utf-8')
fuc = codecs.open("fuc.xml","w",'utf-8')
kgram = codecs.open("kgram.xml","w",'utf-8')
smc = codecs.open("smc.xml","w",'utf-8')
uc = codecs.open("uc.xml","w",'utf-8')
wsp = codecs.open("wsp.xml","w",'utf-8')
cvfv.write("<add>\n")
cvfv.write("<doc>\n")
fmc.write("<add>\n")
fmc.write("<doc>\n")
fuc.write("<add>\n")
fuc.write("<doc>\n")
kgram.write("<add>\n")
kgram.write("<doc>\n")
smc.write("<add>\n")
smc.write("<doc>\n")
uc.write("<add>\n")
uc.write("<doc>\n")
wsp.write("<add>\n")
wsp.write("<doc>\n")
tmp = glob.glob("*.csv")
pwd = commands.getoutput('pwd')
print pwd
for i in tmp:
    fuzzy = commands.getoutput("python /Users/nakamurajun/yamamoto15scis/prog/fuzzyhashing.py -b "+ pwd+"/"+i)
    print fuzzy
    print
    print "cvfv" in str(i)
    print
    fuzzy_split = fuzzy.split(" ")
    tmp = glob.glob("*.csv")
    pwd = commands.getoutput('pwd')
    if len(fuzzy_split) >= 2:
        fuzzy_split[1] = fuzzy_split[1].replace('\n',"")
        if "cvfv" in str(i):
            cvfv.write("</doc>\n")
            cvfv.write("<doc>\n")
            cvfv.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            cvfv.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "fmc" in str(i):
            fmc.write("</doc>\n")
            fmc.write("<doc>\n")
            fmc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            fmc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "fuc" in str(i):
            fuc.write("</doc>\n")
            fuc.write("<doc>\n")
            fuc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            fuc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "kgram" in str(i):
            kgram.write("</doc>\n")
            kgram.write("<doc>\n")
            kgram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            kgram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "smc" in str(i):
            smc.write("</doc>\n")
            smc.write("<doc>\n")
            smc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            smc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "uc" in str(i):
            uc.write("</doc>\n")
            uc.write("<doc>\n")
            uc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            uc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
        elif "wsp" in str(i):
            wsp.write("</doc>\n")
            wsp.write("<doc>\n")
            wsp.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            wsp.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
cvfv.write("</doc>\n")
cvfv.write("</add>\n")
fmc.write("</doc>\n")
fmc.write("</add>\n")
fuc.write("</doc>\n")
fuc.write("</add>\n")
kgram.write("</doc>\n")
kgram.write("</add>\n")
smc.write("</doc>\n")
smc.write("</add>\n")
uc.write("</doc>\n")
uc.write("</add>\n")
wsp.write("</doc>\n")
wsp.write("</add>\n")
