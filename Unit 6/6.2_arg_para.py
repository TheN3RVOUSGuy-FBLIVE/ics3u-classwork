#1 ---------------------------------------------------

def num_chairs(tables, chairs_per_table):
    chairs = tables * chairs_per_table
    print(f"You will need {chairs} chairs.")


num_chairs(4, 5)

# 4 and 5 are arguments being sent to the function
# tables, chairs_per_table are the parameters. 4 and 5 are sent to them.
# the output is 4 * 5
# error because the variable will be undefined


#2 ---------------------------------------------------

def print_int(int):
    return int

print(print_int(6))


#3 ---------------------------------------------------

def diff(a, b):
    return a - b

print(diff(3, 2))


#4 ---------------------------------------------------

# only one parameter
# does not return a value

def subtract(a, b):
    return a - b

print(subtract(1, 2))


#5 ---------------------------------------------------

def activate_thrusters(percent_power):
    pass

activate_thrusters(1)
activate_thrusters()


#6 ---------------------------------------------------

# no arguments
def person_apples(a, b):
    return a, b
print(person_apples("bob", 7))