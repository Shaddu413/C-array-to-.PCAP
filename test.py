
import os
import binascii
import subprocess

import re
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

f=open("text1","r")
x=comment_remover(f.read())
f.close()

f=open("text1","w")
f.write(x)
f.close()

f = open('./text1','r')
a = [',','0x','\n','};',' ','{',]
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('./text1','w')
for line in lst:
    f.write(line)
f.close()

os.system('xxd -r -p text1 binfile')  

output = subprocess.check_output("od -Ax -tx1 -v binfile" , shell=True)


u=open("plaintext1.txt","wb")
u.write(output)
u.close()

os.system('text2pcap plaintext1.txt yourpkt.pcap')





