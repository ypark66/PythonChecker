#ASSERTION ERROR
def a(n):
    return n * 2

def test_a():
    assert a(2) == 5

test_a()   #BUG, AssertionError



    return n % 2 == 0
def test_b(n):
    assert b(n) % 2 == 1, "it's not an even number"
test_b(4)
test_b(5)   #BUG, AssertionError "it's not an even number"



#ATTRIBUTE ERROR
# raised when you try to access or call an attribute
# that a particular object type doesn't possess

import string

a = string.capitalize("jamie") #BUG, AttributeError
a = string.capwords("jamie")

b = "hello".lowercase() #BUG, AttributeError
b = "hello".lower()



#INDEX ERROR
import sys

a = "abcde"
n = input()
print(a[n])  #BUG, IndexError
print(a[-7]) #BUG, IndexError

print(sys.argv[0])
print(sys.argv[1]) #BUG, IndexError

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list[-6])  #BUG, IndexError
print(a_list[-3])

a_list.append(['c','d','e'])
print(a_list[5][3])  #BUG, IndexError , two dimensional

a_list.pop(-1)  #BUG, IndexError



#KEY ERROR
a="abasdlfkajadfjakeinkxjdfjaioedsksjskjdksjfei"

d = {}
for k in a:
    if k not in d:
        d[k] = 1
    else:
        d[k]+=1

print(d['y'])  #KeyError


a_set = {1,2,3,4,5}
a_set.discard(6)
a_set.remove(6)       #BUG, Key error

a_set.clear()
a_set.pop()						#BUG, Key error


#MODULENOTFOUND ERROR
import str
str.lower() #ModuleNotFoundError



#NAME ERROR
print(a)  #NameError

a = 2
b= 4
a_dict = {a:5,b:6}
del a
print(a_dict[a])		#BUG, NameError
print(a_dict[b])



myArray = [1, 2, 3, 4, 5, 6]
for i in myArra:   #NameError
    print (i)




#OVERFLOW ERROR
import math

math.exp(1000)  #OverflowError



#STOP ASYNC ITERATION
class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)
    def __aiter__(self):
        return self
    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

async def aprint(str):
  async for letter in AsyncIteratorWrapper(str):
    print(letter)

import asyncio
loop = asyncio.get_event_loop()
co = aprint("abcde")
loop.run_until_complete(co)




#STOP ITERATION
def countdown(n):
    while n> 10:
        yield n
        n -= 1
    return n


for x in countdown(13):
    print(x)

c = countdown(13)
next(c)
next(c)
next(c)
next(c)   # StopIteration Error




#UNBOUND LOCAL ERROR

count = 0
def increment():
    count += 1

increment()




#ZERO DIVISION ERROR
a = 4 / 0			#BUG, division by zero
a = True / False #BUG, division by zero

import fractions

def method():
  return 0

fractions.Fraction(a,0)  #BUG, division by zero
fractions.Fraction(2,method())  #BUG, division by zero





# BLOCKING IO ERROR - BUGGY
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

host = socket.gethostname()
port = 1234

sock.connect((host, port))  # BUG, BlockingIOError

msg = "--> From the client\n"

select.select([], [sock], [])
if sock.send(bytes(msg, 'UTF-8')) == len(msg):
    print("sent ", repr(msg), " successfully.")

sock.close()



# BLOCKING IO ERROR - NON BUGGY
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

host = socket.gethostname()
port = 1234

try:
    sock.connect((host, port))
except BlockingIOError:
    print("BlockingIOError")

msg = "--> From the client\n"

select.select([], [sock], [])
if sock.send(bytes(msg, 'UTF-8')) == len(msg):
    print("sent ", repr(msg), " successfully.")

sock.close()




# BROKEN PIPE ERROR - BUGGY
import subprocess as sub

p = sub.Popen(["ls", "-al", "../"], stdin=sub.PIPE, stdout=sub.PIPE)

p.stdout.read()

p.stdin.write("ls\n")  # BUG, BrokenPipeError



# BROKEN PIPE ERROR - NON BUGGY
import subprocess as sub

p = sub.Popen(["ls", "-al", "../"], stdin=sub.PIPE, stdout=sub.PIPE)

p.stdout.read()

try:
    p.stdin.write("ls\n")
except BrokenPipeError:
    print ("Broken Pipe Error")
    
    



# CONNECTION ABORTED ERROR
import pickle
import socket
import threading

# buggy client side
class BuggyConnectionThread(threading.Thread):
    def run(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 2727))  # BUG, ConnectionAbortedError

        for x in range(10):
            client.send(pickle.dumps(x))
            print('Sent:', str(x))
            print('Received:', repr(pickle.loads(client.recv(1024))))

        client.close()


for x in range(5):
    BuggyConnectionThread().start()
    
    

    
# CONNECTION REFUSED ERROR
import pickle
import socket
import threading

# buggy client side
class BuggyConnectionThread(threading.Thread):
    def run(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 2727))  # BUG, ConnectionRefusedError

        for x in range(10):
            client.send(pickle.dumps(x))
            print('Sent:', str(x))
            print('Received:', repr(pickle.loads(client.recv(1024))))

        client.close()


for x in range(5):
    BuggyConnectionThread().start()



# CONNECTION RESET ERROR
import pickle
import socket
import threading


# buggy client side
class BuggyConnectionThread(threading.Thread):
    def run(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 2727))  # BUG, ConnectionResetError

        for x in range(10):
            client.send(pickle.dumps(x))
            print('Sent:', str(x))
            print('Received:', repr(pickle.loads(client.recv(1024))))

        client.close()


for x in range(5):
    BuggyConnectionThread().start()
    

    
# CONNECTION ERROR - NON BUGGY
import pickle
import socket
import threading

# buggy client side
class NonBuggyConnectionThread(threading.Thread):
    def run(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(('localhost', 2727))
        except ConnectionRefusedError:
            print("Connection Refused")
        except ConnectionAbortedError:
            print("Connection Aborted")
        except ConnectionResetError:
            print("Connection Reset")

        for x in range(10):
            client.send(pickle.dumps(x))
            print('Sent:', str(x))
            print('Received:', repr(pickle.loads(client.recv(1024))))

        client.close()


for x in range(5):
    NonBuggyConnectionThread().start()


    

#FILE EXISTS ERROR - BUGGY
import os

def buggy_mkdir(path):
    os.mkdir(path)  # BUG, FileExistsError

path = "C:"
buggy_mkdir(path)




#FILE EXISTS ERROR - NON BUGGY
import os

def non_buggy_mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print ('Directory not created.')


path = "C:"
non_buggy_mkdir(path)





#FILE NOT FOUND ERROR - BUGGY
def buggy_open_file():
    filename = "nothing.txt"
    f = open(filename)  # BUG, FileNotFoundError

buggy_open_file()

import os

os.chdir('some directory') #BUG, FileNotFoundError




#FILE NOT FOUND ERROR - NON BUGGY
def non_buggy_open_file():
    filename = "nothing.txt"
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File Not Found")

non_buggy_open_file()




#IS A DIRECTORY ERROR - BUGGY
import os

path = "C:"
# assume that file.txt exists
f = open("file.txt")
f.write("hello\n")
os.replace(f.name, path)  # BUG, IsADirectoryError




#IS A DIRECTORY ERROR - NON BUGGY
import os

path = "C:"
# assume that file.txt exists
f = open("file.txt")
f.write("hello\n')
try:
    os.replace(f.name, path)
except IsADirectoryError:
    print ("Is a directory")
    
    


#NOT A DIRECTORY ERROR - BUGGY
import os

def compruebaArchivo(cadena, archivo):
    archivo_nuevo=""
    if "cadena" in archivo:
        if "_"+cadena in archivo:
            archivo_nuevo = archivo.replace("_"+cadena, '')
        elif "-"+cadena in archivo:
            archivo_nuevo = archivo.replace("-"+cadena, '')

    print(archivo_nuevo)
    return archivo_nuevo


def mueveArchivos():
    home = os.path.expanduser("~")
    Descargas = home + "/Descargas/"
    UGR = home + "/UGR/"
    for path, dirs, files in os.walk(Descargas):
        for arch in files:
            #Asignatura TSI
            if "TSI" in arch:
                arch_nuevo=compruebaArchivo("TSI", arch)
                os.rename(Descargas + arch, UGR + "TSI/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""
            #Asignatura FBD
            elif "FBD" in arch:
                arch_nuevo=compruebaArchivo("FBD", arch)
                os.rename(Descargas + arch, UGR + "FBD/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""
            #Asignatura IC
            elif "IC" in arch:
                arch_nuevo=compruebaArchivo("IC", arch)
                os.rename(Descargas + arch, UGR + "IC/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""
            #Asignatura IA
            elif "IA" in arch:
                arch_nuevo=compruebaArchivo("IA", arch)
                os.rename(Descargas + arch, UGR + "IA/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""
            #Asignatura AC
            elif "AC" in arch:
                arch_nuevo=compruebaArchivo("AC", arch)
                os.rename(Descargas + arch, UGR + "AC/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""
            #Asignatura ALG
            elif "ALG" in arch:
                arch_nuevo=compruebaArchivo("ALG", arch)
                os.rename(Descargas + arch, UGR + "ALG/" + arch_nuevo)  #BUG, NotADirectoryError if archivo_neuvo = ""

    
    
    
#PERMISSION ERROR - BUGGY
def buggy_open_file():
    # assuming that we do not have an access to a.txt
    a_file = open('a.txt', encoding='utf-8')  # BUG, PermissionError
    return a_file

buggy_open_file()





#PERMISSION ERROR - NON BUGGY
def non_buggy_open_file():
    # assuming that we do not have an access to a.txt
    try:
        a_file = open('a.txt', encoding='utf-8')
    except PermissionError:
        print("permission denied")
    return a_file

non_buggy_open_file()




#TME OUT ERROR - BUGGY
import urllib
from urllib.request import Request


def download(url):
    request = urllib.request.urlopen(url, timeout=60)  # BUG, TimeoutError
    data = request.read()
    decoded = data.decode('utf-8')
    return decoded


  
#TIME OUT ERROR - NON BUGGY
import urllib
from urllib.request import Request


def download(url):
    try:
        request = urllib.request.urlopen(url, timeout = 60)
        data = request.read()
        decoded = data.decode('utf-8')
    except TimeoutError:
        print("Timeout Error")
    return decoded


##############################################################################################
#NOT SURE ABOUT THESE TEST CASES  - TODO

#OS ERROR

import os
import io

#OSerror
def delete_files_and_dir(self):
    try:
        os.remove(os.path.join(self.output_dir_, "output1.xml"))
    except os.error:
        pass
    try:
        os.remove(os.path.join(self.output_dir_, "output2.xml"))
    except os.error:
        pass
    try:
        os.rmdir(self.output_dir_)
    except os.error:
        pass


def walk_with_symlinks(top, func, arg):
    """Like os.path.walk, but follows symlinks on POSIX systems.

    If the symlinks create a loop, this function will never finish.
    """
    try:
        names = os.listdir(top)
    except os.error:
        return
    func(arg, top, names)
    exceptions = ('.', '..')
    for name in names:
        if name not in exceptions:
            name = os.path.join(top, name)
            if os.path.isdir(name):
                walk_with_symlinks(name, func, arg)




#PROCESS LOOKUP ERROR - BUGGY    : need to fix server module


#process look up error
import subprocess

#there is normally no need to kill the subprocess after the call to wait returns
def buggy_process_lookup():
    for package in server.packages:
        n = subprocess.Popen(['which', package], stdout=subprocess.DEVNULL)
        n.wait()
        if n.returncode != 0:
            n.kill()


buggy_process_lookup()




#PROCESS LOOKUP ERROR - NON BUGGY     : need to fix server module


import subprocess
import socketserver

def non_buggy_process_lookup():
    processes = []
    for package in socketserver.packages:
        n = subprocess.Popen(['which', package], stdout=subprocess.DEVNULL)
        processes.append(n)
    for p in processes:
        try:
            p.kill()
        except OSError:
            # silently fail if the subprocess has exited already
            pass


non_buggy_process_lookup()



###########################################################################################
https://stackoverflow.com/questions/35668520/python-eof-error-when-reading-input

n = int(input())
dum = input()
d = {}
for i in range(0,n+1):
    x = raw_input()
    x = x.split(" ")
    d[int(x[0])] = int(x[1])

array = d.keys()

for key in d.keys():
    if(d[key]!=0):
        if(d[key] not in d.keys()):
            for i in d.keys():
                for j in d.keys():
                    if(i!=j and i!=key and j!=key):
                        if(i+j==d[key]):
                            # print str(i)+"-"+str(j)
                            if(i in array):

                                array.remove(i)
                            if(j in array):
                                # print j
                                array.remove(j)
        else:
            # print d[key]
            array.remove(d[key])
print(array[0])


#VALUE ERROR
import sys
import urllib
import urllib.request

fullurl = input("Please specifiy the vulnerable url: ")

resp = urllib.request.urlopen(fullurl + "=\' or \'1\' = \'1\'")
body = resp.read()
fullbody = body.decode('utf-8')






##############################################################################################################################################################################
#Type Mismatch
class error(object):
    def __init__(self):
        self.string = "string"
        self.integer = 10
    def implemented(self):
        raise NotImplemented
class derived(error):
    def implemented(self):
        print("derived")

def type_mismatch(int = 5):
  	a = int + 5							#BUG, type mismatch
		stone = 5 + 5
    intone = "hi" + " yeah"
    None == 0										//caught by pylint, useless statement
    None == ''
    temp = stone + intone   #BUG, Type mismatch
    test = 5 if int == 5 else "hi"
    test = stone + test     #BUG, Type mismatch

def argument_type_error(a , b = False):
  	print("hi")
    
def tuple_error():
 	 	a = ('a','b','c')
    a[0] = 'd'
  
print("testing for errors")
obj = error()
type_mismatch()
#argument_type_error(b = False, True)   #BUG, argument type mismatch
#argument_type_error(a = 4000, True)    #BUG, named argument followed by unnamed(positional) argument



#Unicode Error
def decode_error():
    b'\x80abc'.decode("utf-8", "strict") #BUG, decode error


def encode_error():
    u = chr(40960) + 'abcd' + chr(1972)
    u.encode('ascii')   #BUG, encode error(ASCII) for ascii encoding, if the code point is 128 or greater, the unicode string can't be represented

decode_error()
encode_error()



#Recursion Error
import random as rand

def fib(n, sum):
    if n < 1:
        return sum
    else:
        return fib(n-1, sum+n)

a = input()      						#BUG, c < 998
print(fib(a, 0))
b = 998											#BUG
print(fib(b, 0))
c = rand.randint(0,1000)   	#BUG
print(fib(c, 0))
print(fib(fib(a,0),0)) 			#BUG





#weakreference error     ////////// incomplete///////////////////////////
import weakref
import gc

class MyObject(object):
    def __init__(self):
        self.name = "object"
    def my_method(self):
        print("my method was called!")

obj = MyObject()
weak = weakref.ref(obj)
proxy = weakref.proxy(obj)
print(proxy)

gc.collect()

print(proxy)





#logically Wrong Condition
def redundant_condition(int):
  if int > 0:
    print("reachable")
  elif int <= 0:
    print("reachable")
	elif int == 4:                #BUG, redundant
    print("unreachable")

def unreachable_condition(int):
  while int > 0:
    if int == -1:								#BUG, unreachable
      print("wrong")
    int = int + 1
  for i in range(0,5):
    if i == -1:									#BUG, unreachable
      print("wrong")

def logical_error(int):
  a = int + 1
  if a == int:									#BUG, not logical
    print("wrong")
    
    
def recursion(int): #///////////////incomplete//////////////////////////
	print("not implemented yet")
  
    
a = random.randint(-5,5)
redundant_condition(a)
unreachable_condition(a)
logical_error(a)


#Infinite Loop
def infinite_recursion(int):
  if int == -1:
    return 0
	int = int + infinite_recursion(int)		#BUG, infinite loop
  return int

def infinite_while_loop(int):
  while int > 0:												#BUG, infinite loop
    int = int + 1
    
infinite_recursion(1)
infinite_while_loop(1)
    
    
    
    
    
#Number of Arguments error
class test(object):
    def __init__(self, int, string):
        self.int = int
        self.name = string

def arguments(int, string, bug):
    a = int
    b = string
    c = bug
    print("hi")

def correct(int, string, bug = 3):
  	print("hi")
    
arguments(1, "hi")  #BUG, wrong number of arguments in calling a method
correct(1, "hi")
a= test(1)          #BUG, wrong number of arguments at initiating object



    
#floating point error
a = 0.1234567891123456711   #BUG, floating point numbers are accurate to 15 decimal places
b = 0.1234567891123456744		#BUG, overflow
if a == b:
    print("wrong")
    
    
    
    
#infinite precision error
import math
math.tan(math.pi / 4)   #BUG, no limit value
    

  
  
#value error
a_list = ['a', 'b', 'new']
a_list.index('new')
a_list.index('c')				#BUG, value error
a_list.remove('a')
a_list.remove('c')  		#BUG, value error

(a,b,c) = a_list
(d,e) = a_list					#BUG, too many values to unpack
(a,b,c) = range(5)			#BUG, too many values to unpack
(a,b,c) = range(2) 			#BUG, not enough values to unpack


#not subscriptable
a = int(input())
print(a[0])							#BUG, not subscriptable

