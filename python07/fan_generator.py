#Fan generator 
#Nesting code 

answer = input("Are you really a fan of Mario Lopez?")
if answer == "yes":
  print("Okay...")
  show = input("What is your favorite show?")
  if show == "Saved By The Bell":
    print("Right on!")
  else: 
    print("Yikes!")
elif answer == "no":
  print("Your loss.")
else: 
  print("Nothing answering my question!")