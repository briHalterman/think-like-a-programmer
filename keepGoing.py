"""keepGoing.py
  demonstrate loop with multiple exits
  Andy Harris"""

# exits with a positive result if the user chooses the right password
# exits with a negative result if the user is wrong 3 times

correct = "IndyPy"
tries = 0

keepGoing = True
while(keepGoing):

  tries = tries + 1
  print ("try # ",tries)

  guess = input("What is the password? ")
  if guess == correct:
    print("That's correct! Here's the treasure!")
    keepGoing = False

  elif tries >= 3:
    print("Too many tries. Launching the missiles")
    keepGoing = False