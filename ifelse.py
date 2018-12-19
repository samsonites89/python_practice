
score = int(input('Input Score: '))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"
print(grade)

# quick memory test
a = "B"
print(id(a))
a = "c"
print(id(a))
a = "d"
print(id(a))
