import hashlib
MyHash = "fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa"
MySalt = "5UA@/Mw^%He]SBaU"
f = open("./data.txt", 'r')
Tab = f.read().split('\n')
for i in Tab:
    print("->", hashlib.sha256(i.encode('utf-8')).hexdigest())