import random



total = 0
while True:
    num = int(input("how many sides to the dice? "))
    y = int(input("how many times do you want to roll it? "))
    x = 1
    z = 0
    while x <= y:
        
    
        no = random.randint(1,num)
        

        print("on your",num,"sided die, you got",no,"for dice number", x)
        print("                                     ")
        print("************************************")
        print(" ")
        z = z + no
        

        x = x +1
    print("total is equal to", z)
