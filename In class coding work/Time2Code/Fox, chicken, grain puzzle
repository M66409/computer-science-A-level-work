def wrong_move():
  if (chicken==fox) and (chicken!=farmer):
    print("The fox ate the chicken.")
    return True
  elif (chicken==grain) and (chicken!=farmer):
    print("The chicken ate the grain.")
    return True
  else:
    return False
    
def puzzle_solved():
  if chicken==1 and fox==1 and grain==1 and farmer==1:
    print("You solved the puzzle.")
    return True
  else:
    return False
    
def output():
  objects=[fox,farmer,grain,chicken]
  objects_names=["fox","farmer","grain","chicken"]
  print("On the other side of the river")
  for i in range(len(objects)):
   if objects[i]==1:
    print(objects_names[i])
  print("On this side of the river")
  for i in range(len(objects)):
   if objects[i]==0:
    print(objects_names[i])

print("A fox, chicken and a bag of grain wait by the side of a river.")
fox=0
chicken=0
grain=0
farmer=0
while (puzzle_solved()==False) and (wrong_move()==False):
  choice=input("""A fox, chicken and a bag of grain wait by the side of a river.
                Which item will you take in your rowboat to the other side?
                fox, chicken, grain or farmer""")
  if choice=="chicken" and chicken==farmer:
    chicken=1-chicken
    farmer=1-farmer
  elif choice=="grain" and grain==farmer:
    farmer=1-farmer
    grain=1-grain
  elif choice=="fox" and fox==farmer:
    farmer=1-farmer
    fox=1-fox
  else:
    farmer=1-farmer
  output()
