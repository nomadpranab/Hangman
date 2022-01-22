import random

with open("wordlist.txt",'r') as hangmanword:
    words=hangmanword.readlines()

word=random.choice(words)[:-1]

allowed_errors=7
guesses=[]
done=False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")
    
    guess=input(f"allowed errors left {allowed_errors},next guess :")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors-=1
        if allowed_errors==0:
            break
    done=True
    for letter in word:
        if letter.lower() not in guesses:
            done=False 

if done:
    print("YOU WON  THE GAME THE WORD WAS",word)
    print("------------------")
else:
    print("Better Luck Next Time The word was",word)




