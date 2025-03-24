motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati')
del motorcycles[0] #delete
print(motorcycles)
popped_motorcycles = motorcycles.pop() #storing pop return value
print(f"Remaining motorcycle after pop call {motorcycles}")
print(f"popped motorcycle {popped_motorcycles}")
print(motorcycles)
print(motorcycles.pop(0))
print(motorcycles)
