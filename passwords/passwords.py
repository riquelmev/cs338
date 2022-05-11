import hashlib
import binascii
import json

#Part 1
words = [line.strip().lower() for line in open('words.txt')]

passwords1 = [line.strip().lower() for line in open('passwords1.txt')]


print(len(words))
print(len(passwords1))

final_names = []
final_passwords = []
for password in passwords1:
  password = password.split(":")
  final_names.append(password[0])
  final_passwords.append(password[1])


cracked_name = []
cracked_pass = []

def hash(input):
    encode = input.encode('utf-8') # type=bytes
    hasher = hashlib.sha256(encode)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    hash = digest_as_hex.decode('utf-8') 
    return hash


print("Jeffs")
print(hash("moose"))
print ("182072537ada59e4d6b18034a80302ebae935f66adbdf0f271d3d36309c2d481" == (hash("moose")))

hashesCount = 0
hashes = dict()
for w in words:
    h = hash(w)
    hashesCount+= 1
    hashes[h] = w

print(hashesCount,"HashesCount")
cracked_keys = {}
i=0
for hash in (final_passwords):
    password = hashes[hash]
    cracked_keys[final_names[i]] = password
    i = i + 1
    
print(cracked_keys)
with open('cracked1.txt', 'w') as file:
    for name in cracked_keys.keys():
        file.writelines(name + ":" + cracked_keys[name] + "\n")

#Part 2

words = [line.strip().lower() for line in open('words.txt')]
passwords2 = [line.strip().lower() for line in open('passwords2.txt')]

final_names = []
final_passwords = []
hashToName = {}

for password in passwords2:
    password = password.split(":")
    final_names.append(password[0])
    final_passwords.append(password[1])
    hashToName[password[1]] = password[0]

cracked_name = []
cracked_pass = []

def hash(input):
    encode = input.encode('utf-8')
    hasher = hashlib.sha256(encode)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    hash = digest_as_hex.decode('utf-8') 
    return hash

cracked2 = open("cracked2.txt", "w")
print ((hash("moose")) in final_passwords)
print ((hash("moose")) in hashToName)


j = 0
hashCount = 0
for w in words:
    for ww in words:
        concat = w + ww
        h = hash(concat)
        hashCount +=1
        if h in hashToName:
            j+=1
            index = final_passwords.index(h)
            print(final_names[index]+ ":" + concat)
        if j == 300:
            break
    if j ==300:
        break
print(hashCount)

#Part3 

words = [line.strip().lower() for line in open('words.txt')]

passwords3 = [line.strip().lower() for line in open('passwords3.txt')]

# print(len(words))
# print(len(passwords3))

def salt_hash(salt,input):
    new_input = salt+input
    encode = new_input.encode('utf-8') # type=bytes
    hasher = hashlib.sha256(encode)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    hash = digest_as_hex.decode('utf-8') 
    return hash

print("Jeffs")
print(salt_hash("e75fa822","moose"))
print(salt_hash("73f5c390","moose"))

print ("6b5b88886d9fcd76e5c4dceafb0069cb969d4f63d331793ae78b1f9b99bdee41" == (salt_hash("73f5c390","moose")))

final_names = []
salts = []
final_passwords = []
hashToName = {}
for password in passwords3:
    password = password.split(":")
    final_names.append(password[0])
    salt = password[1][3:11]
    salts.append(salt)
    final_passwords.append(password[1][12:])
    hashToName[password[1][12:]] = password[0]


    # for w1 in wordlist:
    #     for w2 in wordlist:
    #         h = hash(w1 + w2)
    #         for user in password file:
    #             if h == hash for user:
    #                 yay
print("Is it in")
print(salt_hash("73f5c390","moose") in final_passwords)
#print(final_passwords)

print(len(hashToName))
print(len(final_names))

hashesFound= set()
print(hashToName['cf31c6f5eb2003e7c106bc73c11a44a056dd3340618ac341d5d0943b4324cd48'])
print(final_passwords.index('cf31c6f5eb2003e7c106bc73c11a44a056dd3340618ac341d5d0943b4324cd48'))
print(salts[1215])
print(final_names[1215])
#'ohrstroma:$5$5dc7f2b6$cf31c6f5eb2003e7c106bc73c11a44a056dd3340618ac341d5d0943b4324cd48::0:99999:7:::'

# for word in words:
#     sa = '5dc7f2b6'
#     h = salt_hash(sa,word)
#     if h == 'cf31c6f5eb2003e7c106bc73c11a44a056dd3340618ac341d5d0943b4324cd48':
#         print('ohrstroma',word)
# print("Done looking")
hashesCount = 0
with open('passwords3done.txt', 'w+') as passfile:
    for word in words:
        for i in range(len(salts)):
            h = salt_hash(salts[i],word)
            if h in hashToName:
                index = final_passwords.index(h)
                print(final_names[index] + ":" + word)
                hashesCount += 1

print(hashesCount)
    
     