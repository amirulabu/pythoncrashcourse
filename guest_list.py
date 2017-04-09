guest = ['Elon Musk', 'Mark Zuckerberg', 'Issac Newton']
print(guest)

print(guest[2])

print(guest[0] + " you are invited")
print(guest[1] + " you are invited")

guest.insert(0,'Jack Ma')
print(guest)
guest.insert(2,'Bill Gates')
print(guest)
guest.append('Richard Branson')
print(guest)

removed_guest = guest.pop()
print("Sorry, you cannot come " + removed_guest)
removed_guest = guest.pop()
print("Sorry, you cannot come " + removed_guest)
print(guest)
del guest[3]
del guest[2]
print(guest)
print(len(guest))