D = {'Anita': 23, 'Ashwin': 43,
     'Ahana': '24',
     'Adarsh': 30, 'Archana': 15}
try:
    # iterates through the keys from left to right
    for key in D:
        value = D[key]
        if type(value) == str:
            raise 'Error'
        print(f'{key}:{value}')
except:
    print("Values cannot be strings")
print("*********")
#----------------------------------------------

L = [1, 3, -1, 4, -2, 5, 3]

try:
    n = 10
    for i in range(n):
        if L[i] < 0:
            L[i] = 0
except IndexError:
    for i in range(n - len(L)):
        L.append(0)
finally:
    print(L)
print("**********")  
#--------------------------------------------------------

try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
        f.write(x)
except FileNotFoundError:
    print('File was not found')
except:
    print('This is some other error')
finally:
    print('The file has been closed')
    f.close()
print("**********")

#------------------------------------------------

L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(L)
L = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L.append(y - x)
print(L)   
L = [ ]
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L.append(y - x)
print(L)
L = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L += [y - x]
print(L)
L = []
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L += [y -x]
print(L)    
print("************")
#---------------------------------------------------------------


M=[[1,2],[3,4]]
rsums = [sum(row) for row in M]
print(rsums)
m, n = len(M), len(M[0])
rsums = []
for i in range(m):
    val = 0
    for j in range(n):
        val += M[i][j]
    rsums.append(val)
print(rsums)
rsums = [ ]
for row in M:
    rsums.append(sum(row))
print(rsums)
print("************")

#------------------------------------------------------------

triplets1 = [(x, y, z) for x in range(1, 100) 
            		  for y in range(x + 1, 100)
           			  for z in range(y + 1, 100)
           			  if x ** 2 + y ** 2 == z ** 2]
triplets2 = [ ]
for x in range(1, 100):
    for y in range(x + 1, 100):
        for z in range(y + 1, 100):
            if x ** 2 + y ** 2 == z ** 2:
                triplets2.append((x, y, z))
triplets3 = [(x, y, z) for x in range(1, 100) 
            		  for y in range(1, 100)
           			  for z in range(1, 100)
           			  if x ** 2 + y ** 2 == z ** 2 and x < y < z]
print(set(triplets1)-set(triplets2))
print(set(triplets1)-set(triplets3))
print(set(triplets2)-set(triplets1))
print(set(triplets2)-set(triplets3))
print(set(triplets3)-set(triplets1))
print(set(triplets3)-set(triplets2))
print("*****************")
#--------------------------------------------------------------
P=[5,3]
Q=[1,4]
R = [ ]
for x, y in zip(P, Q):
    R.append(x + y)
print(R)
R = [P[i] + Q[i] for i in range(len(P))]
print(R)
print("**************")
#-----------------------------------------------------------
M=[[1,2],[3,4]]
M_t = [[M[j][i] for j in range(len(M))] for i in range(len(M))]
print(M_t)
M_t = [ ]
n = len(M)
for i in range(n):
    M_t.append([ ])
    for j in range(n):
        M_t[-1].append(M[j][i])
print(M_t)      
