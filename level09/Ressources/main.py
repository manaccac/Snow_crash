file = open('token').readlines()[0]
res = ""
print("Before {}".format(file))
for i in range(0, len(file) - 1):
   res = res + chr(ord(file[i]) - i)
print("After {}".format(res))