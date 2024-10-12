data="Nahidur Rahaman"
s=type(data)
print(s)
l=len(data)
print(l)
import sys
a=sys.getsizeof(data)
print(a)
c=data.count('a')
print(c)
sub='am'
su=data.count(sub)
print(su)
data = '60 Days of ypython'
print(data.find('of'))
print(data.find('f'))
print(data.find('y',6,14))
print(data.index('y',6,13))
print(data.lower())
print(data.upper())
print(data.casefold())
x = 'data SCIENCE is Fun'
print(x.capitalize())
print(x.swapcase())
print(x.title())
print(x.islower())
print(x.isupper())
print(x.isdigit())
print(x.split())
print(x.split()[1])
print(x.center(100))
print(x.replace('data','AI'))
x = 10
y = 100
z = x*y

print('I have ',z,'taka')
print('I have {} taka'.format(z))
