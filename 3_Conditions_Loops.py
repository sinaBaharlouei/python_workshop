x = 10
y = 2
print x == 10
print x == 20

if x == 10:
    print "x equal to 10"
else:
    print "x is not equal to 10"

if x == 10 and y == 3:
    print x + y
elif y == 2 or x == 20:
    print x - y

listA = [1, 2, 3, 4]

if 3 in listA:
    print "3 is in listA"

if 5 not in listA:
    print "5 is not in list A"

# ------------------------------------------
# Loops
print "Numbers:"
for i in range(1, 10):
    print i

print "Numbers:"
for i in range(100, 10, -5):
    print i

print "Alist:"
for x in listA:
    print x

# while loop
count = 0
while count < 5:
    print count, " is  less than 5"
    count += 1
else:
    print count, " is not less than 5"