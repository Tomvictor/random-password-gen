import hashlib
import random

word = str(random.random())
#print(word)
word1 = word.encode('utf8')
#print(word1)
salt = hashlib.sha1(word1).hexdigest()[:20]
print(salt)