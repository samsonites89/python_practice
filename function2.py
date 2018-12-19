# function 2
def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res


print(union("HAM", "SPAM"))


def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/"
    for keys in user.keys():
        str += keys + "=" + user[keys] + "&"
    return str


print(userURIBuilder("localhost", "8080",
                     userId="sam", passwd="1234"))

# lambda
g = lambda x, y: x * y
print(g(2, 3))

def factorial(x):
    # 탈출 조건
    if x==1:
        return 1
    return x * factorial(x-1)

print(factorial(3))
print(factorial(10))

s ='abc'
it = iter(s)
# print(it)
def reverse(data):
    for index in range(len(data)-1,0,-1):
        yield data[index]
        # return data 하면.. 하나의 값만 리턴되는 것을 까먹으면 안된다.

for char in reverse('gold'):
    print(char)

