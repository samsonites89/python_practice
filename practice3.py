# Yield and Iter
def abc():
    data = 'abc'
    for element in data:
        return element

# The example below uses yield instead of return
def efg():
    data = 'efg'
    for element in data:
        yield element

print(abc())
print(efg()) # a generator object
for char in efg():
    print(char)

# Range practice
print(list(range(0, 10, 1))) # 0 부터 10(미포함)까지 출력. 1씩 증감


