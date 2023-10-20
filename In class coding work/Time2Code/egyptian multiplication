def mul(num1,num2):
  sum=0
  total=0
  i=0
  first_number=num1
  second_number=num2
  first_list=[]
  second_list=[]
  while first_number>=1:
    first_list.append(first_number)
    second_list.append(second_number)
    first_number=first_number//2
    second_number=second_number*2
  while i<len(first_list):
    if first_list[i]%2==0:
      del first_list[i]
      del second_list[i]
      i=0
    else:
      i+=1
  
  for i in range(len(second_list)):
    sum=sum+second_list[i]
    i+=1
  return sum

def input_numbers():
  num1=int(input("enter the first number"))
  num2=int(input("enter the second number"))
  return num1,num2

numbers=input_numbers()
for i in range(len(numbers)):
  if i==0:
    num1=numbers[i]
  else:
    num2=numbers[i]
print(mul(num1,num2))
