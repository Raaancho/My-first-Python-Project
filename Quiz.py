print()
print("Let's see how much you know about the person that wrote this code")

User_name = input("What's your name? ")

print("It's nice to have you here", User_name)
print("Press Enter to Continue")

Ent = input()

print("So let us get to business, make sure you supply only the number corresponding to your option")

First_name = ['Babatunde', 'Animasahun', 'Uthman', 'Abidemi']
Nick = ['Newton', 'Rancho', 'YoungProf', 'Labamba']
Age = [22, 23, 24, 25]
Fav_Artist = ['Big Wiz', 'Davido', 'Burna Boy', 'Kizz Daniel']
Course_of_study = ['Telecommunication Science', 'Computer Science', 'Electrical Engineering', 'Applied Mathematics']

p = 0
f = 0

print()
for (i,j) in enumerate(First_name, start = 1):
    print(i,j)
name_ans = int(input("What is my first name? "))
if name_ans == 3:
    p = p+1
    print("Yes sir!!!")
else:
    f = f+1
    print("That's not correct")

print()
for (i,j) in enumerate(Nick, start = 1):
    print(i,j)
nick_ans = int(input('What is my nick name? '))
if nick_ans == 2:
    p =p+1
    print("Nice One!!!")
else:
    f =f+1
    print('Ouchhhh')

print()
for (i,j) in enumerate(Age, start = 1):
    print(i,j)
age_ans = int(input('How old am I? '))
if age_ans == 3:
    p = p+1
    print('Keep it up!')

else:
    f+=1
    print("I may look old but that ain't my age")
print()
for(i,j) in enumerate(Fav_Artist, start = 1):
    print(i,j)

Fav_Artist_ans = int(input('Which Artist is my favorite? '))
if Fav_Artist_ans == 3:
    p+=1
    print('You sabi!!!')

else:
    f+=1
    print('Your GOAT no come close')
print()
for (i,j) in enumerate(Course_of_study, start =1):
    print(i,j)

Course_of_study_ans = int(input('What was my course of study? '))
if Course_of_study_ans == 1:
    p+=1
    print('Yeah Yeah, I am a Telcommunication Engineer')

else:
    f+=1
    print("Nah Nah, that ain't my course")


print()
print('Weldone',User_name)
print()

if p == 5:
    print('You got everything correctly: \n \n My first name is Uthman \n My nickname is Rancho \n I am 24 years old \n Burna Boy is my favourite artist and \n I studied Telecommunication Science')
elif f == 5:
    print('You got everthing wrong, Try again some other time.')

else:
    print('You got',p,'correctly and',f,'incorrectly')

print()
print('See you around',User_name,'.')