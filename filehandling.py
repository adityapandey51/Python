# File Handling

#     - There are primarily 2 types of files
#             1. Textual Files
#             2. Binary Files
#     - And we primarily perform these activities on these files in any program
#             1. Open the File
#             2. Read/Write the file 
#             3. Close the File 

# Creating and writing a file
# this creates a file or writes to that file if it already exists
f = open('sample.txt', 'w')
f.write('hello world')
# # to write multiple lines use writelines and pass a list of sentences
f.writelines(['aaaa', 'bbbb'])
f.close()

# but the problem with write mode is that it deletes 
# the old content of the file before writing the content so we have 'a' mode which is append mode

f = open('sample.txt', 'a')
f.write('something')
f.close()

# Reading a file

f = open('sample.txt', 'r')
f.read() # --> You can also give it a number to read only that many chars
f.close()

f = open('sample.txt', 'r')
f.readline() # --> read the first line
f.close()

#########################################################################

# USING CONTEXT MANAGER(with)
with open('sample.txt', 'r') as f: # --> this automatically closes a file after usage, no need to use close()
    chunk_size = 1
    data = f.read(chunk_size)
    while len(data)>0:
        print(data, end = " ")
        data = f.read(chunk_size)  
    # f.write('something')
f.tell() # --> tells us which will be the next index to get printed after f.read(chunk_size)
# --> if we want to move that buffer back and forth to some other index then just use
f.seek(100) # --> moves the buffer to 100th index, and now the f.read will start reading from 100th index


# BINARY FILES --> just use 'rb' or 'wb' methods

with open('something.png', 'rb') as f:
    with open('somethin_else.png', 'wb') as wf:
        wf.write(f.read())

## SERIALIZATION/DESERIALIZATION

# serialization   - process of converting python data types into JSON
# deserialization - process of converting JSON to python data types

# for this we need json module

import json

with open('sample.txt','w') as f:
    json.dump({'hello': 'aditya', 'hin':'gghh', 1:'ggh'}, f , indent = 4)

with open('sample.txt', 'r') as f:
    print(json.load(f))

#  --> we can also serialize objects

class A:

    def __init__(self):
        self.a = 1
        self.b = 2

obj = A()

def serilize_obj(object):
    if isinstance(object,A):
        return "{}:{}".format(object.a,object.b)
    
with open('sample.txt','w') as f:
    json.dump(obj,f,default=serilize_obj) # --> here the default argument tells json.dump how to serialize the given object

#  To serialize into byte we use pickle 
# Also it is more efficient than json becuase it preserves the exact state of the python object
# tuple doesn't becomes list, numerical keys of dict doesn't become string while serialization

import pickle

with open('smaple.pkl','wb') as f:
    pickle.dump(obj,f) # --> similarly we pickle.load(f) in 'rb' mode