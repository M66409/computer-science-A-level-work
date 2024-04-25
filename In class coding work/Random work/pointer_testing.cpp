#include <iostream>

int func(int *x){
    int s=*x;
    std::cout << x <<"\n";
    s=s+1;
    return s;
}

int otherfunc(int x){
     x=x+1;
     std::cout<< &x <<"\n";
     return x;
}
int main() {
    int y =5;
    int* w = &y;
    std::cout << w <<"\n";
    int z = func(w);
    std::cout << z << "\n";
    int v = otherfunc(y);
    std::cout << v;
    return 0;
}
