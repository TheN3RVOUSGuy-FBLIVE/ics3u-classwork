# 1 --------------------------------------------------

animals = "monkey bat cat dog"

for i in animals.split(" "):
    print(i)

# 2 --------------------------------------------------

nums = "65, 75, 32, 22"
e = 0
for j in nums.split(", "):
    print(int(j), end = " ")
    print(f"at index {e}")
    e += 1

# 3 --------------------------------------------------

string = ""
add = input("enter numbers with ', '\n")
string = add
numlist = []
for word in string.split(", "):
    if word == "zero":
        numlist.append(0)
    elif word == "one":
        numlist.append(1)
    elif word == "two":
        numlist.append(2)
    elif word == "three":
        numlist.append(3)
    elif word == "four":
        numlist.append(4)
    elif word == "five":
        numlist.append(5)

print(numlist)

# 4 --------------------------------------------------

scores = input("enter wins/loses/ties (W/L/T) \n").split(" ")
new_score = []

for letter in scores:
    if letter == "W":
        new_score.append(2)
    elif letter == "L":
        new_score.append(1)
    elif letter == "T":
        new_score.append(0)
    
print(new_score)

# 5 --------------------------------------------------

message = str(input("X POSITION \n")).split(",")
print(message)
mes = ""
for posi in range(len(message)):
    mes += message[posi]
mes = mes.split("x:")
mes = (mes[1:])

for q in range(len(mes)):
    mes[q] = int(mes[q])
print(mes)

# 6 --------------------------------------------------

msg = input("input x and y\n")
positions = msg.split(" - ")
newposi = []

print(positions)

for t in range(len(positions)):
    x, y = positions[t].replace("x:", "").replace("y:", "").split(",")
    newposi.append([int(x), int(y)])

print(newposi)
