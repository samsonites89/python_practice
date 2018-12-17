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

