name = "Gamer"
print ("Hello  {}  "  .format(name))
import random

word = ["Python", "Machine", "Computer", "Web", "Programming"]
word = random.choice(word)

guess = 5
letters = []
x = len(word)
z = list ('_' * x)
print('_' .join(z), end='\n')

while guess > 0:
    y= input("Please Guess a Letter:" )
    if y in letters:
     print ("Please do not guess the letters you guessed earlier")
     continue
    elif len (y) > 1:
        print ("Please entered a just letter")
        continue
    elif y not in word :
        guess -= 1
        print ("Wrong guess {} you have the right to guess" .format(guess))
    else:
        for i in range (len(word)):
            if y== word[i] :
                print("correct guess!")
                z[i]= y
                letters.append (y)
                print (' ' .join(z), end='\n')
                break


    if guess==0:
     print("you are out of gueswork. you lost! the man hanged")
