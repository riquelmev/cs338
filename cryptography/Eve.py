def crack(value,g,mod):
    for i in range(mod):
      if ((g**i) % mod == value):
        return i

# print("X = ", crack(57, 13, 59))
# print("Y = ", crack(44,13,59))

# print("Alice computes", (44**20)%59)
# print("Bob computes", (57**47)%59)

def find_num(target):
	for i in range(target):
		for j in range(target):
			if(i * j == target):
				print(i,j)

find_num(5561)

def lcm(x,y):
  orig_x = x
  orig_y = y
  while True:
    if x < y:
      x = x + orig_x
    elif y < x:
      y = y + orig_y
    else:
      return x

print(lcm(66,82))

def find_db(eb,mod):
  for i in range(100000):
    if ((eb*i) % mod == 1):
      return i

print(find_db(13,2706))

def gcd_check(x,y):
  greater = max(x,y)
  for i in range(2,greater):
    if ((x%i) == 0 and (y%i) == 0):
      return False
  return True

print(gcd_check(2706,13))

# compute ydB mod nB

def decrypt(list, db, nb):
	decrypted = []
	for i in range(len(list)):
		decrypted.append((list[i]**db) % nb)
	return decrypted

def to_ASCII(list):
  message = ""
  for letter in list:
	  message += chr(letter)
  return message
    

encrypted_list = [1516, 3860, 2891, 570, 3483, 4022, 3437, 299,570, 843, 3433, 5450, 653, 570, 3860, 482,
 3860, 4851, 570, 2187, 4022, 3075, 653, 3860,
 570, 3433, 1511, 2442, 4851, 570, 2187, 3860,
 570, 3433, 1511, 4022, 3411, 5139, 1511, 3433,
 4180, 570, 4169, 4022, 3411, 3075, 570, 3000,
 2442, 2458, 4759, 570, 2863, 2458, 3455, 1106,
 3860, 299, 570, 1511, 3433, 3433, 3000, 653,
 3269, 4951, 4951, 2187, 2187, 2187, 299, 653,
 1106, 1511, 4851, 3860, 3455, 3860, 3075, 299,
 1106, 4022, 3194, 4951, 3437, 2458, 4022, 5139,
 4951, 2442, 3075, 1106, 1511, 3455, 482, 3860,
 653, 4951, 2875, 3668, 2875, 2875, 4951, 3668,
 4063, 4951, 2442, 3455, 3075, 3433, 2442, 5139,
 653, 5077, 2442, 3075, 3860, 5077, 3411, 653,
 3860, 1165, 5077, 2713, 4022, 3075, 5077, 653,
 3433, 2442, 2458, 3409, 3455, 4851, 5139, 5077,
 2713, 2442, 3075, 5077, 3194, 4022, 3075, 3860,
 5077, 3433, 1511, 2442, 4851, 5077, 3000, 3075,
 3860, 482, 3455, 4022, 3411, 653, 2458, 2891,
 5077, 3075, 3860, 3000, 4022, 3075, 3433, 3860,
 1165, 299, 1511, 3433, 3194, 2458]

print(decrypt(encrypted_list, 1249, 5561))

decrypted = decrypt(encrypted_list, 1249, 5561)

print(to_ASCII(decrypted))