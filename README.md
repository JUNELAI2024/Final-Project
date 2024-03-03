# Final-Project
# 1 Objective - Create a robotic tour guide for Disneyland park tourist
# 2 Requirement - to provide direction and destination information to tourist according to their provided direction & time
# 3 Project Timeline - 2 weeks
# 4 Method & Solution - start below
# 4.1 -- greeting 
name = input("Type your name: ")
print("Welcome", name, "to Disneyland Park!")

# 4.2 Tourist need to return direction (right/left)
answer = input("Pls take your direction first (right/left). ")

# 4.2 if tourist wants to turn right, ask him how long they would spend and give him the destinction of 10 mins or 20 mins
if answer == "right":

  answer = input("Do you prefer 10 or 20 minutes walk?" )

     if answer == "10":
 
  print("You will arrive at Animaition Academy First.")


  elif answer =="20":
  print("You will arrive at Ant-Man and the Wasp")
  else:
  print('Not a valid option.')

# 4.2 if tourist wants to turn left, ask him how long they would spend and give him the destinction of 10 mins or 20 mins  
elif answer == "left":
answer = input("Do you prefer 10 or 20 minutes walk?" )

if answer == "10":
  print("You will arrive at Art of Animation")
  elif answer =="20":
  print("You will arrive at Castle of magical Dreams")
  else:
  print('Not a valid option.')

else:
print('Not a valid option.')

# 4.2 complete conversation
print("Thank you for trying this guide tool, name)

# 5 Result 
Type your name: Tim
Welcome Tim to Disneyland Park!
Pls take your direction first (right/left). left
Do you prefer 10 or 20 minutes walk? 20
You will arrive at Castle of magical Dreams
Thank you for trying this guide tool, Tim

# 6 Resourcec
Website of disneyland 

# 7 What's Next
Include and Design more detail questions to make it more precise to what tourist would want to know including opening hour, time of different activities.