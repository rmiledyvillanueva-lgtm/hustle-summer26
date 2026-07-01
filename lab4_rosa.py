# Rosa | Lab 4 | Intro to python

# Ticket 1:
# Predict: I believe that the age 11 and 9 will get "Too young: and the rest will get "Access granted."

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age < 13:
        print (f"{age} - Too young")
        continue
    else:
        print (f"{age} - Access granted")

# Explain: The variable "age" holds a number which grants or denies access based on what was programed. 

#ticket 2:
#Predict: I believe that if they type "no" on the first check, it will not print. Since they said no
keep_checking = "yes"

while keep_checking == "yes":
    age = input("what is your age?")

    if int(age) < 13:
        print("Too young")
        print() 
        keep_checking = input("Check another age?").lower()
    elif int(age) >= 13:
        print("Access granted")
        keep_checking = "no"
        # an "keep_checking == "no" was needed to go to the next thing because it was starting to become an infinite loop. 
#Explain: A while loop allows the user to add another age, when they type yes. 
    
#Ticket 3:
#Predict: I believe that if I were to forget to type "stop" it would loop forever like in ticket 2.

while True:
    age = input("Enter your age or type 'stop':")
    if age.lower() == "stop":
        break

    if int(age) < 13:
        print("Too young")
    elif int(age) >= 13:
        print("Access granted")
        if age.lower() == "stop":
            break

#Explain: I think the difference is that ticket 3 has a "stop:" and a break. Tiket two doesnt. 
#But Honestly, it looks the same to me. I am so confused. Hopefully I am following the diffections correctly. 

#Ticket 4:
#Predict:The difference is that there is no if and else, it looks more clean since it was defined. 

age = [17, 11, 25, 13, 9]
def can_access(age):
    if age >= 13:
        return True
    else: 
        return False
for age in ages:
    if can_access(age):
        print(f"{age} - Access granted")
    else:
        print(f"{age} - Too young")
#Explained: I was confused on this part because there is still an "if/else" on this ticket. Putting it inside the function is better so it does not messes you up

#Ticket 5:
#Predict: I think it will count all the approved ages which is a sum of 4
signup_report = [22, 10, 15, 8, 19, 13]
approved = 0

for num, item in enumerate(signup_report, start=1):
    if can_access(item):
        print(f"Signup #{num}. | Age {item} - Access granted")
        approved += 1
    else:
        print(f"Signup #{num}. | Age {item} - Too young")

print(f"Approved: {approved} out of {len(signup_report)}")
#Explain: I used an f string and a len to count the total number, and a enumerate to count the approved ages. 