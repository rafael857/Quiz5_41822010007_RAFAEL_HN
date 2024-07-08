#expresion
x = 15 % 5
print(x)

x = 12  + 3 * 5 ==75
print(x)

x = "PML"+ "15523"
print(x)

x = "100"
y = 234
z = int(x) + y
print(z)

x = ((11%3)+2) != 8/2
print(x)

#bollean
p =  11
q = 5
r = 4

a =  ((p-r) == (r+q) )
print(a)

b= (((p%3)+q)!=(r%2))
print(b)

c= ((q-3)==(p%2+q))
print(c)

d= ((r+q)!=((p*2)%2))
print(d)

e =((((q%3)+p)>(r%2)))
print(e)

f = (((r+p))<=(q*5))
print(f)

#isian singkat
x = "boo"
h = "Honney"
y = 3
z = h  + x * int(y)
print(z)


capitals = {}


capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'

print(capitals['Germany'])

# a = "23"
# b=9
# print(a+b)

# Definisikan list
letters = ["a", "b", "o", "c", "p"]

print(letters[1])
print(letters[len(letters)-2])
print(letters + ["x"])
print(letters)

r = ' '.join('h a n d s'.split())
print(r)

#import json

#json_string = """
#[
 #   {1: 'one', 2: 'two', 3: 'three'},
  #  {1: 'un', 2: 'deux', 3: 'trois'},
   # {1: 'eins', 2: 'zwei', 3: 'drei'}
#]
#"""

#result_6 = json.loads(json_string)[1][2]
#result_6

print("deux")

#lengkapi kode python berikut
def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return  -1
vals = [100,66,55,64,41,35,18,64]
hasil = pembagi_indeks(vals, 5)
print(hasil)


#nomor delapan
def mystery(n, m):
    p = 0
    e = 0
    while p < n:
        p += 1

    while e < m:
        e += m

    return p


print(mystery(4,3))




