s= set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

st =  'aaaaaaaaabbbcccceee'
settt = set(st)
print(settt)

#hash maps - Dictonaries
d = {'a':1, 'b':2, 'c':3}
print(d)
d['d'] = 4
print(d)
print(d['a'])
d['a'] = 5  
print(d)

#loop over the key:value pairs
for key, val in d.items():
    print(f"{key}:{val}")
