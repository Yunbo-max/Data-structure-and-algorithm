import hashlib
hashlib.md5('hello world').hexdigest()
hashlib.sha1('hello word').hexigest()

m=hashlib.md5()
m.update("hello world")
m.update("this is A")
m.hexdigest()