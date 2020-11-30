import random
a = ["rock", "paper", "scissor"]

cpoint=0
upoint=0

print("""press rock for 'rock'
press paper for 'paper'
press scissor for 'scissor'""")

while cpoint<5 and upoint<5:
    computer = random.choice(a)
    user_choice = input("choose from rock, paper, scissor: ").lower()
    if user_choice == computer:
        print("same choice from both sides, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")

    elif user_choice == "rock":
        if computer == "paper":
            cpoint = cpoint + 1
            print("you lose bro! computer choosed paper, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")
        elif computer == "scissor":
            upoint = upoint + 1
            print("you win! computer choosed scissor, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")

    elif user_choice == "paper":
        if computer == "rock":
            upoint = upoint + 1
            print("you win! computer choosed rock, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")
        elif computer == "scissor":
            cpoint = cpoint + 1
            print("you lose bro! computer choosed scissor, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")

    elif user_choice == "scissor":
        if computer == "rock":
            cpoint = cpoint + 1
            print("you lose! computer choosed rock, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")
        elif computer == "paper":
            upoint = upoint + 1
            print("you win! computer choosed paper, point of computer: " +str(cpoint) +" your point: "+ str(upoint)+"\n")
