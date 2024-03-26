timetable=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
def menu(timetable):
  choice=int(input("1. output timetable, 2. Edit a lesson, 3. Load, 4. Save, 5. Close"))
  while choice!=5:
    if choice==1:
      for i in range(len(timetable)):
        for j in range(len(timetable[i])):
          print(timetable[i][j])
          j+=1
        i+=1
