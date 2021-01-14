import hashlib

MyHash = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"
f = open("./leakedDb.txt", 'r')
Tab = f.read().split('\n')
for i in Tab:
    if (hashlib.sha256(i.encode('utf-8')).hexdigest() == MyHash):
        print("Le mot de passe est :",i)