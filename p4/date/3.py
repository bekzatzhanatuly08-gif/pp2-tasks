from datetime import datetime 
a = datetime.now()
a_new = a.replace(microsecond = 0)
print(a_new)