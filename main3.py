#range and format
"""
(list(range(2,10,2)))#срез, от 2 включительно до 10 не включая, с шагом 2 

print('python'[-6: 3: 1])
s = 'python'
n = 5
print(s[2:4] + ' ' + s[5])
print('My string:{map}{0} and {1}'.format(s, n**2,map = n))
"""
#split and join
"""
l = []
s = 'python'
for i in s:
  l.append(i*2)
result = '  '.join(l)
print(result)

print(' '.join(result.split()))
"""
r = range(2,10)
print('    ', end ='')
for i in r:
  print(i, end= '  ')
  
print()
for i in r:
  print(i, end ='  ')
  for j in r:
    if i*j<10:
      print(' ', end='' )
    print(i*j, end= ' ')
  print()


