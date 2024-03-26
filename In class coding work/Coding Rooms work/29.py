A=int(input())
B=int(input())
N=int(input())
A=A*100
M=A+B
M=M*N
A=M//100
B=M%100
print(A," ",B)
