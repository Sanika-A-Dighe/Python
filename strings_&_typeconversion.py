#string indexing
a = "PROGRAMMING"
# to print only one index
print([7])# +ve indexing strats from 0 to infinite (left to right)
print([-3])# -ve indexing strats from -1 to infinite (right to left )

 #string slice
b = "PYTHON"
print(b[2:6:1])

c = "Hello how are you"
#  printing how / you / hello
print(c[6:10:1])
print(c[14:18:1])
print(c[0:6:1])

#type conversion
d = "13"  #STRING TO INTEGER
e = int(d)
print(type(e))

f = 13.5     #FLOAT TO INTEGER
g = int(f)
print(type(g))


# string can be converted to integers only if it holds valid values
#  float values can be also converted to integer

h = "12.6" # STRING TO FLOAT
i = float (h)
print(type(i))
print(i)

j = 24       #INTEGER TO FLOAT
k = float(j)
print(type(k))
print(k)

l = 13
m = str(l)
print(m)

n = 24.5
o = str(n)
print(o)

p = 27 + 1j
q = str(p)
print(q)

r = True
s = str(r)
print(s)

t = 12  #INTEGER TO BOOLEAN
u = 0.0 # FLOAT TO BOOLEAN
v = 12.4  # FLOAT TO BOOLEAN
w = 34 + 7j  # COMPLEX TO BOOLEAN 
x = "hello"   # STRING TO BOLLEAN
y = {}        
z = ()

print(bool(t))
print(bool(u))
print(bool(v))
print(bool(w))
print(bool(x))
print(bool(y))
print(bool(z))


# THE FOLLOWING 7 VALUES WILL BE ALWAYS FALSE WHEN CONVERTING TO BOLLEAN
# EXCEPT THE FOLLOWING 7 VALUES EVERYTHING WILL BE TRUE

# False
# 0
# 0.0
# ""
# {}
# []
# ()