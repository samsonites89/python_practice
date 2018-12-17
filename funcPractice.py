def returnMulti(x, y):
    return x * y

def swap(a, b):
    return b, a

print(returnMulti(2,  2))
print(swap(3, 6))

# 교집합
def intersect(preList, postList):
    returnList = []
    for x in preList:
        if x in postList and x not in returnList:
            returnList.append(x)
    return returnList

a = [1, 2, 3]
b = [3, 4, 5]

print(intersect(a, b))


# Scope Test
g = 1
def testScope(a):
    global g
    g =2
    return g+a
print(testScope(1))
print(g)

def change(x):
    x[0] = 'H'

wordList = ['J', 'A', 'M']
print(wordList)

def changeAgain(x):
    x = x[:]
    x[0] = 'H'
    print(x)


change(wordList)
print(wordList)


g = 1
def testScopeOf(a):
    global g
    g = 2
    return g + a

var = testScopeOf(2)
print(var)
print(g)

count = 0
def testCount():
    global count
    count += 1
    print("Run func")

testCount()
testCount()
print(count)

a=1.2
print(hex(id(a)))
a=2.3
print(hex(id(a)))

# most variables are immutable : 정수, 실수, 문자열, tuple
hello = "hello"
print(hex(id(hello)))
hello = "hi"
print(hex(id(hello)))


# Orderdoesnotmatter
def connect(server,port):
    print("http://" + server + ":" + port)


connect("127.0.0.1", "8080")
connect(port="8080", server="localhost")  # 순서는 상관없음
