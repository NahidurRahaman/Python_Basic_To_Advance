x=10
y=10.5
z=10+5j
print(type(x))
print(type(y))
print(type(z))
print(isinstance(z,complex))
print(isinstance(10,float))
print(isinstance(10,int))
n=float(x)
print(n)
print(type(n))
n=int(n)
print(type(n))
n=complex(n)
print(n)
#sequencce data type
l = [1,2,3,4,True,[1,2],'data',(1,2,3,8)]
print(l[0])
print(l[-1])
print(l[-1][-1])
print(type(l))
#tuple
t = (1,5,8,9,'Ai')
print(t[0])
print(t[0:4])
#range
x = range(10)
for i in x:
    print(i)
x = range(5,20) #2nd case
for i in x:
    print(i)
x = range(5,20,3) #3rd case
for i in x:
    print(i)
x = range(20,5,-3) #4th case
for i in x:
    print(i)
#array
import array as ar
a = ar.array('i',[1,2,3,4])
print(type(a))
#Set

s = {1,2,3,5}
#Dictionary

dic={
    'varsity': 'FAU Germany',
    'Dept': 'Data Science'
}
#Data Frame (Pandas)

import pandas as pd

df = pd.read_csv('python.csv')
print(df.head(10))
print(df.info(10))
