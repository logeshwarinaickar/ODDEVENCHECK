def oddeven(number):
    if number % 2 ==0:
        print("THIS NUMBER IS EVEN")
    else:
        print("THIS NUMBER IS ODD")

while True:
    total_numz=int(input("HOW MANY NUMBERS DO U WANT TO CHECK? "))
    for i in range(total_numz):
        num=int(input(f"ENTER NUMBER {i+1}: "))
        oddeven(num)
    again= input("DO U WANT TO TRY AGAIN? (YES/NO) ").lower()
    if again != "yes":
        print("GOODBYEEEE!")
        break