bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # This prints a representation of the list, basically how it appears in the IDE
print(bicycles[0]) # This displays the first item in the list/array. Everything starts at 0
print(bicycles[0].title()) # You can combine previous methods into lists. 

# Create a list, then change the first item in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 

motorcycles[0] = 'ducati'
print(motorcycles)

# Append an item onto the end of a list with the append() method
motorcycles.append('honda')
print(motorcycles)

# Reset list
motorcycles = []

# Create the list with append. You can append an item to an empty list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
motorcycles.insert(0, 'ducati')

print(motorcycles)