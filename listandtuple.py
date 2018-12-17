# samsam.son

colors = ['red', 'green', 'gold']
print(colors)
print(type(colors))

colors += ["blue"]
print(colors)
colors.pop()  # Takes the top out.. this exists in a list??? that's interesting
print(colors)  # red green gold
colors.pop(1)
print(colors)  # red gold
colors.append("green")
print(colors)  # red gold green

# sorting function
colors.sort()  # reverse,, etc.
print(colors)  # gold green red

# tuple
tu = (1, 2, 3)
print(type(tu))

a = 1
b = 2


def calc(a, b):
    return a + b, a * b


args = (4, 5)
print(calc(*args))
x, y = calc(3, 3)  # each value is assigned to  x and y
print(x)
print(y)

argsList = list(args)
print(type(argsList))

argsList.clear()
print(argsList)


device = {"iPhone":"1", "galaxy":"2"}
happy = device  # happy is a reference to device

print(device.items())
print(device_items)

# set has what it calls items...


print(hex(id(device)))  # this is how you print the memory address of a variable in python
print(hex(id(happy)))




