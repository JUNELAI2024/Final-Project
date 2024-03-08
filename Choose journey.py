name = input("Type your name: ")
print("Welcome", name, "to Disneyland Park!")
      
answer = input("Pls take your direction about right or left first ")
if answer == "right":

  answer = input("Do you prefer 10 or 20 minutes walk?")

     if answer == "10":
 
  print("You will arrive at Animaition Academy First.")


  elif answer =="20":
  print("You will arrive at Ant-Man and the Wasp")
  else:
  print('Not a valid option.')

  
elif answer == "left":
answer = input("Do you prefer 10 or 20 minutes walk?")

if answer == "10":
  print("You will arrive at Art of Animation")
  elif answer =="20":
  print("You will arrive at Castle of magical Dreams")
  else:
  print('Not a valid option.')

else:
print('Not a valid option.')

print("Thank you for using me for a tour guide", name)