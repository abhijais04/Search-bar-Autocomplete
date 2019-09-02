import names

a={"dummy name"}

for i in range(0,310000):
	a.add(str(names.get_full_name()))
	#print (len(a))

print(len(a))
