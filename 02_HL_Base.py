import random


# instructions
def instructions():
    print("**** Welcome to Higher Lower Game *****")
    print()
    print("For each game you will be asked to..",
          "\n- Enter a 'low' and 'High' number. The computer will randomly",
          "\ngenerate a 'secret' number between your two chosen numbers",
          "\nIt will use this number for all the rounds in a given game",
          "\n-The computer will calculate how many guess you are allowed",
          "\n-enter the number of rounds you want to play",
          "\nguess the secret number")
    print()
    print("Good Luck!")
    print()
    print("Please press <enter> to begin...")
    print()


# Number checking function
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or
            # too low if both an upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between",
                          f"{low} and {high}")
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("please enter a number that is more than",
                          f"(or equal to) {low}")
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("Please enter an integer")
            continue
