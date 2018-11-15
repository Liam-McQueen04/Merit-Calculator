#Liam McQ - Merit Calculator

print("Did you get a merit?")

french = int(input("What mark did you get for French?\n"))
history = int(input("What mark did you get for History?\n"))
maths = int(input("What mark did you get for Maths?\n"))
computing = int(input("What mark did you get for Computing?\n"))
english = int(input("What mark did you get for English?\n"))

total = float(french + english + history + maths + computing)

average = total / 5

if total > 6:
    print("Well Done! You have been awarded a merit.")
else:
    print("Sorry! You didn't get a merit.")
