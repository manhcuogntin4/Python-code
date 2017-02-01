import os
import glob
path=os.getcwd()
print path
print os.listdir(os.curdir)
os.mkdir("test_dir")
os.rename("test_dir", "test_dir_2")
f=open("hello.txt","w")
f.write("Hello Cuong")
a=os.path.abspath("hello.gook.txt")
print a
ls=os.path.split(a)
base=os.path.basename(a)
dirname=os.path.dirname(a)
split=os.path.splitext(base)
txt_files=glob.glob('*.txt')
print txt_files
print base
print dirname
print ls
print split
