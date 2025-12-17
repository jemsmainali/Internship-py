import random
def game():
    options=["sissor🖖","paper✋","rock👊"]
    name=input("Enter any one from(scissor,paper,rock):")

    if name not in options:
        print("enter any one from scissor ,paper or rock")


    computer= random.choice(options)
    print(f"computer choose:{computer}")
    print(f"You choose is:{name}")

    if name==computer:
        print(f"Both choose same{name}")

    elif (name=='paper'and computer=='rock')or\
            (name=='scissor'and computer=='paper') or\
            (name=='rock'and computer=='scissor'):
        print("you win")
    else:
        print("computer win")
game()

