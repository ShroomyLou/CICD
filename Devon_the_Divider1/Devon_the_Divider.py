
import time
import random
from tabulate import tabulate

my_file = open("Devon_results.txt", "w")
my_data = []

print("Hello! I am Devon the Divider\n"
          "My job is to divide numbers and opinions among other things.\n"
      "I am also capable to create a txt file with your asked data for powers. \n"
      "If you'd like, I can give you lottery or keno numbers too.\n")

def decision():
    devonchoice = input("What would you like me to solve? Choose:\n 1 for division,\n 2 for powers,\n 3 for squareroots, or\n 4 for gambling:\n You can also type in exit if you wish to exit. ").strip()

    if devonchoice.isnumeric():
        devonchoice = int(devonchoice)
    elif devonchoice == "exit" or "Exit" or "EXIT":
        quit()
    else:
        time.sleep(1)
        print("ERROR")
        print("ERROR")
        print("DANGER")
        print("DANGER")
        print("My sensors indicate that that is not even a number. Try again")
        print()
        print()
        decision()

    
    if int(devonchoice) == 1:
        print()
        print("Alrighty, you want divisions huh? No problemo buddy guy.")
        print()
        devondivide()
        
    if int(devonchoice) == 2:
        print()
        print("Hahhaa! Powers of your choice! Not superpowers but numerical powers.")
        print()
        devonpower()


    if int(devonchoice) == 3:
        print()
        print("I have been taught to give you squareroots of the first 100 numbers, no more, no less")
        print()

        devonsquares()

    if int(devonchoice) == 4:
        print("A small time gambler, huh?\n")
        time.sleep(1)
        choose = input("Pick your poison, 1 for lottery, 2 for keno: \n")
        if choose.isnumeric():
            choose = int(choose)
            if choose == 1:
                lotto()
            if choose == 2:
                keno()
            else:
                print("I don't know that choice.")
                decision()
        else:
            print("I don't know that choice.")
            decision()


        
    else:
        time.sleep(2)
        print("...")
        print()
        print("1 or 2 only, very simple, then press enter.")
        print()
        decision()

def devondivide():
 
    numerator = input("Please, give me a number to be a numerator: ")
    denominator = input("Now, please give another number for denominator: ")

    if numerator.isnumeric() and denominator.isnumeric():
        numerator = int(numerator)
        denominator = int(denominator)
    else:
        time.sleep(1)
        print("ERROR")
        print("ERROR")
        print("DANGER")
        print("DANGER")
        print("My sensors indicate that that is not even a number. Try again")
        print()
        print()

        devondivide()

    print("You picked numbers ", numerator, " and ", denominator, " for division.")

    nrt = int(numerator)
    dnm = int(denominator)
    nrt1 = nrt - 1
    dnm1 = dnm + 1
    div1 = nrt1/dnm1

    excuses = ["Just a little more", "I haven't done this in a while, sorry buddy",
               "Devon, you can do this! *heavy calculating sounds*",
               "Why is this so hard?", "I'm sorry I just woke up.",
               "This should be already done", "You're not a real program Devon, they said. I'll show them!",
               "Sorry bud, almost done", f"If  {nrt1} divided by {dnm1} equals {div1} then..."]

    excuse = random.choice(excuses)
    excuses.remove(excuse)
    excuse1 = random.choice(excuses)
    excuses.remove(excuse1)
    excuse2 = random.choice(excuses)
    
    try:
        division = nrt / dnm
        print(nrt, " divided by ", dnm, " is...")
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")
        time.sleep(2)
        print(excuse)
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")
        time.sleep(3)
        print(excuse1)
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")
        print(excuse2)
        print("...")
        print("...")
        print("...")
        print("...")
        print("...")
        time.sleep(2)
        print ("Ah, finally, the division of ", nrt, " and ", dnm, " equals to\n", division)

    except ZeroDivisionError:
        print("Can't divide with 0")
        print()
        print("Please give some other numbers.\n"
              "Don't give a 0 as the denominator,\n"
              "unless you want the universe to\n"
              "implode and explode at the same time")
        
        devondivide()
    decision()


def devonpower():


    
    number = input("Give me a number you want exponentially multiplied!")
    expo = 0
    time.sleep(2)

    if number.isnumeric():
        numb = int(number)
    else:
        time.sleep(1)
        print("ERROR")
        print("ERROR")
        print("DANGER")
        print("DANGER")
        print("My sensors indicate that that is not even a number. Try again")
        print()
        print()

        devonpower()
    
    print("All right, I'm all set, let's go")
    print()
    print("You chose the powers of ", numb, ".")

    power = 0
    
    
    while expo < 11:
        print(numb, "to the power of ", expo, "equals to: \n",
              pow(numb, expo))
        print()
        time.sleep(0.5)
        expo = expo + 1
        power = pow(numb,expo)
        temp_list = [numb, expo, power]
        my_data.append(temp_list)

        if expo == 10:
            head = ["Number", "Exponent", "Result"]
            table = tabulate(my_data, headers=head, tablefmt="grid")
            my_file.write(table)
            my_file.close()
    decision()




def devonsquares():
    base = 0

    my_squares = []

    while base < 101:
        base = base + 1
        square = base**0.5
        temp_squares = [base, square]
        my_squares.append(temp_squares)

        if base == 100:
            head = ["Number", "Squareroot"]
            table = tabulate(my_squares, headers=head, tablefmt="grid")
            print("Here's the table, I also made you a text file with the same data included.")
            print(table)
            my_file.write(table)
                
            my_file.close()
    decision()



def lotto():
    lotterynumbers = []

    for i in range(1,41):
        lotterynumbers.append(i)

    your_lottery = []
    extra_number = []

    for j in range(7):
        lotterynumb = random.choice(lotterynumbers)
        your_lottery.append(lotterynumb)
        lotterynumbers.remove(lotterynumb)

    for k in range(1):
        extra = extra_number.append(random.choice(lotterynumbers))

    print(" Your lottery numbers for this week are: \n",
          your_lottery,"\n",
          "And your extra number for this weeks lottery is: \n",
          extra_number,"\n",
          "May lady luck be on your side\n")
    time.sleep(2)
    decision()


def keno():
    print(" Oh a keno player, eh?\n")

    size = input(" First you must choose how many numbers you'd like, 2-10: \n ")

    if size.isnumeric():
        size = int(size)
    else:
        print("I can't use {size} as a number between 2 and 10, can I?")
        keno()

    kenonumbers = []
    your_keno = []

    for x in range(1,71):
        kenonumbers.append(x)

    for y in range(size):
        kenonumb = random.choice(kenonumbers)
        your_keno.append(kenonumb)
        kenonumbers.remove(kenonumb)

    print(" Your keno numbers for today are: \n",
          your_keno,"\n",
          "May lady luck be on your side\n")
    time.sleep(2)
    decision()    




decision()


