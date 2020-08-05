file = open("gfile.txt", "r")
temp = file.read().splitlines()
#print(temp)

a = "a b 0"
a = a.split(" ")
print(a[0])
print(a[1])
print(a[2])