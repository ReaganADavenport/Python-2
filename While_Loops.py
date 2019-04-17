#should_run = True
"""
bye_count = 0

while bye_count < 3:
    should_run = True

    while should_run:
        user_input = input("What? ")
        print("%s" % (user_input,))

    if user_input == "bye":
        should_run = False

        bye_count = bye_count + 1
    print(bye_count)
    
"""

#assignment 1
"""
counter = 1

while counter<=10:
    print(counter)
    counter = counter + 1
"""

"""
#assignment 2

lower = int(input("Start from: "))
upper = int(input("End on: "))

counter = lower

while counter <= upper:
    print(counter)
    counter = counter + 1
"""


#assignment 3
"""
counter = 0

while counter <= 10:
    if counter%2 ==0:
        counter = counter + 1
    else:
        print(counter)
        counter = counter + 1

"""

#assignment 4
"""
answer = "yes"
counter = 0
print("You have %s coins" % counter)

while answer == "yes":
    answer = input("Do you want another? ")
    if answer.lower() == "yes":
        counter = counter + 1
        print("You have %s coins" % counter)

#Don't type "yes" in all caps.
"""

#Assignment 5

#length = 5
#width = 5

len_count = 0
width_count = 0

while len_count <= 4:
    print("*" * 5)
    len_count = len_count + 1    