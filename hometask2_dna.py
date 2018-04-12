from collections import defaultdict
#DNA
"""
a = 0 #adenine
c = 0 #cytosine
g = 0 #guanine
t = 0 #thymine

"""

s = 'AGCTTTTCATTCTGACTGCAACGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#to_print = True
dic = defaultdict(int)
dic = {dic[i]+ 1 for i in s}
for i in s:
  dic[i]+=1
"""
  if i =='A':
    a+=1
  elif i == 'C':
    c+=1
  elif i == 'G':
    g+=1
  elif i == 'T':
    t+=1
  else:
    print("DNA string is formed only by (a, c, g, t). There is a symbol {}.".format(i))
    to_print = False
    break
if to_print:
  print('{} {} {} {}'.format(a, s.count('C'), g, t))
"""
print(dic)
#RNA
print()
t = 'GATGGAACTTGACTACGTAAATT'
u = ''
for i in t:
  if i == 'T':
    u+= 'U'
  else:
    u+=i
print(u)

#REVC
print()
s = 'AAAACCCGGT'
reversed_s = ''
for i in s:
  if i == 'A':
    reversed_s+= 'T'
  elif i == 'T':
    reversed_s+= 'A'
  elif i == 'C':
    reversed_s+= 'G'
  elif i == 'G':
    reversed_s+= 'C'
  else:
    print("DNA string is formed only by (a, c, g, t). There is a letter {}.".format(i))
    break
reversed_s = reversed_s[::-1]
print(reversed_s)
