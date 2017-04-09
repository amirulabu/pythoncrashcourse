one_to_twenty = []
for x in range(1,21):
	one_to_twenty.append(x)
print(one_to_twenty)

one_to_million = []
for y in range(1,1000001):
	one_to_million.append(y)
#print(one_to_million)
print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

odd_numbers = []
for z in range(1,21,2):
	odd_numbers.append(z)
print(odd_numbers)

multiple_of_3 = []
for a in range(3,31,3):
	multiple_of_3.append(a)
print(multiple_of_3)	

cubes = []
for b in range(1,11):
	cubes.append(b**3)
print(cubes)

cubes2 = [c**3 for c in range(1,11)]
print(cubes2) 