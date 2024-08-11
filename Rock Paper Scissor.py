import random
comp = ["Rock","Paper","Scissor"]
print("Let's Play Rock Paper Scissor")
user=(input("ENTER---> Rock/Paper/Scissor:"))
comp_choice=random.choice(comp)
print(f"Your Choice:{user.upper()}")
print(f"Computer Choice:{comp_choice.upper()}")


if (comp_choice == user):
     print("DRAW!!!")
elif (user == "Rock" and comp_choice == "Scissor") or \
         (user == "Paper" and comp_choice == "Rock") or \
         (user == "Scissor" and comp_choice == "Paper"):
        print("YOU WIN!!!")
else:
    print("YOU LOOSE :(")
