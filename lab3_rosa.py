# Rosa | Lab 3| Hustle Summer 2026| Pink tiger team

# A String

# Ticket1
username = "el_huevito"
#PREDICT: 10 characters
print(len(username))
#Explain: yes, it counted every character

#Ticket2
#PREDICT: It will print the letter E and O
print(username[0])
print(username[9])
#explain : My username has 15 characters, and it is -1 (last character being#14) because it always starts with a 0

#Ticket3
#PREDICT: yes, I do think they will look identical since they are doing the same command, just written differently.
first = "Welcome to Loop, @"
last = "el_huevito!"
full = first + last
print(full)
print(f"Welcome to Loop, @{username}!")
#explain: I honestly prefer that f-string are easier. less work and i was able to memorize that one faster. 

#Ticket4
#PREDICT: I do not think it will run because username[0] that is an x, does not exist. 
#username[0] = "X"
# - Had to make it a comment to continue with the work 
#COMMENT: TypeError: 'str' object does not support item assignment
#explain: I remember that for a string, you cannot change things like in a line or dictionary. So that is why it prints error. 

#B Lists

#Ticket5
#PREDICT: I predict it will count 2, the first caption to print is "Cats4life"
feed = ["Cats4life", "Happy life", "Summer_Vives"]
print(len(feed))
print(feed[0])
#Explain: I used index 0 to get the fist code

#Ticket6
#PREDICT: This 4th post will have index 3
feed.append("Green-Earth")
print(feed)
#explain: It just adds to the (len), the previous len was 2, (+1) thus this new one is 3. Since it starts with 0.

#Ticket7
# PREDICT: the post "Cats4life" will be removed. 
feed.pop(0)
feed.sort()
print(feed)
#explain: I used the method .pop and .sort(). The pop removed the index you ask, the .sort() makes them alphabetical order. They are more easy to remember. 

#C Dictionaries

# Ticket 8
#PREDICT: It will print the number 35 since that is the value of "followers", I honestly have no clue what profile[0] does.
profile = {"username": "el_huevito", "followers": "35", "verified": "False"}
print(profile["followers"])
#profile[0]
# profile[0] - KeyError: 0
#explain: diccionaries has "something" that has a value, and that value is not a number or something like that. It does not have numbers. Its like a "whole thing"

#Ticket9
#PREDICT: .get("age") will print out Error because it does not exist. 
print(int(profile["followers"])+50)
print(profile.get("age"))
#explain: .get() is safer because it did not print out SyntaxError, which makes the terminal look uglies and stops at that error. It instead says "none" because it does not exist and goes on with the day.

#D Capstone

#Ticket 10
print(f" @{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[-1]}")
# I had some errors, for instance, used "" instead of ''. And [3] instead of -1.. I al still a little confused with that part.
#Explain: I used an f-string because I had some words that are not "coded". and used{} because it touches the "info" I want to get. The [len] which counts the amount of posts I have.
#[-1] to get the post I want to print. Although, I think I messed up for the len(feed). 