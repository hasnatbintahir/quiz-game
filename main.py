from quiz_seperater import l2
import random

numbers = list(range(1, 96))
score = 0
fails = 0
total_num = 100

for i in range(1,11):
    choosen_number = random.choice(numbers)
    numbers.remove(choosen_number)
    print(f"{i}: {l2[choosen_number][0]}\n The Options are: \n {l2[choosen_number][1]}\n{l2[choosen_number][2]}\n{l2[choosen_number][3]}\n{l2[choosen_number][4]}\n")
    print()
    ans = input("Choose a) , b) , c) or d) ")
    try:
        if ans == l2[choosen_number][-1]:
            score += 1
        else:
            fails+=1
    except:
        print("you choose wrong input")
            
print(f" You right answers are {score} and wrong answers are {fails}.")
print(f" You got {((score*10)/total_num)*100}/100")
    


