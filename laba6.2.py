import random
myfile = open('pred.txt',"r")
rows = myfile.read().split("\n")
while True:
    number=int(input("\nEnter number 1 or 2 (1 random, 2 continue, 0 exit), please -->"))
    if number==1:
        your_row = random.randint(0,len(rows))
        print(rows[your_row-1])
    elif number==2:
        go_array=True
        while go_array:
            print("Choose variant 1 to 30")
            manual_wish=int(input("[1-30] --> "))
            if manual_wish>=1 and manual_wish<=30:
                print(rows[manual_wish-1])
                go_array = False
            else:
                print("Wrong input, repeat, please")
    elif number==0:
        print("Best wishes, bye")
        break
    else:
        print("Please choose only 1 or 2")
