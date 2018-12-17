# TEST Python
import copy

print("Hello World")

# 변수
a = "데이터"
b = "문자열"
# Case Sensitive
len(a)
# You must indent.,, otherwise there will be an error
c = 1
if c == 1:
    print(c)
else:
    print(a)


# 문자열은 Slicing이 가능하다
a = 'python'
print(a[0:1])  # p
print(a[1:4])  # yth
print(a[:4])  # pyth

# Minus reads from the back
print(a[-4])  # t

strA = """
save
multiple
lines
"""
print(strA)

print("c\\hello")  # 파일의 경로를 설정할떄는 이렇게!


########################################################

isRight = False
type(isRight)

var1 = 1 < 2  # var should be True
var2 = 1 != 2  # var should be True
var3 = True or False # var should be True
print(var3)


# Soft Copy and Deep Copu
a = 1
b = a
print(hex(id(a)))
print(hex(id(b)))  # should be the same

c = 1
d = copy.deepcopy(c)


print(hex(id(c)))
print(hex(id(d)))  # should be the same


print(3 / 2)  # 1.5
print(3 // 2)  # 1




