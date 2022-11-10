# -*- coding: utf-8 -*-
import sys
import os

def mei(r):
    nulldir = False
    nowdir = os.getcwd()
    filename = os.path.splitext(os.path.basename(r))[0]
    f=open(r,"rb")
    f.seek(0)
    nametest = f.read(8)
    if nametest != b'\x4C\x4B\x53\x50\x55\x30\x30\x32':     
        print('File magic number NG')
        return None 
    elif nametest == b'\x4C\x4B\x53\x50\x55\x30\x30\x32':  
        print('File magic number OK')
    else :
        print('Unknown NG')
        return None 
    f.seek(12)
    filenumberbyte=f.read(4)
    filenumber=int.from_bytes(filenumberbyte, byteorder='little')
    print(str(filenumber)+" files")
    for i in range(0, filenumber):
        filenamelenbyte=f.read(4)
        filenamelen=int.from_bytes(filenamelenbyte, byteorder='little')
        filename=f.read(filenamelen)[:-1].decode('ascii')
        print(filename)
        filensizebyte=f.read(4)
        filensize=int.from_bytes(filensizebyte, byteorder='little')+1
        filedata=f.read(filensize)
        z=open(filename,'bw')
        z.write(filedata)
        z.close
        filenuknown2byte=f.read(15)

print('')
print('Project Level UPPER')
print('UPPER KIT THE FINAL')
print('EXTRA 1 - A BEAUTIFUL STAR')
print('')
try : 
    input = sys.argv[1]
except IndexError:
    print('No file specified')
    exit()
mei(input)