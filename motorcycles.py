motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles[0])

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(1,'BMW')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motocycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motocycle)

motorcycles.remove('honda')
print(motorcycles)