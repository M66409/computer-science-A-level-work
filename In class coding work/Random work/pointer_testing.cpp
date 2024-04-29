#include <iostream>
#include <chrono>
int func(int *x){
    int s=*x;
    std::cout << x <<"\n";
    s=s+1;
    return s;
}

int otherfunc(int x){
     std::cout << &x << "\n";
     x=x+1;
     return x;
}

int* test( int* x){
    std::cout << x <<"\n";
    int* y = x+1;
    int* z = x-1;
    std::cout << y <<"\n";
    std::cout << z <<"\n";
    std::cout << *x << "\n";
    std::cout << *y << "\n";
    std::cout << *z << "\n";
    return y;
}

void loop( int* x){
    int i =100;
    while (i>0){
        i--;
        std::cout << *x << "\n";
        x--;
    }
    std::cout << "\n";
    
    i = 100;
    while(i<200){
        i++;
        std::cout << *x << "\n";
        x++;
    }
}


int main() {
    
    int arr[10]={42,763,126,3,751,126,2,545,7654};
    int* w = arr;
    int i = 0;
    while(i<9){
        w++;
        i++;
        std::cout << (w-1) << "\n";
        std::cout << *(w-1) << "\n"; 
    }
    
    for(int i=0;i<9;i++){
        std::cout << arr[i] << "\n";
        std::cout << &arr[i] << "\n";
    }
    /*int y =5;
    int* w = &y;
    loop(w);
    /*std::cout << w <<"\n";
    
    int z = func(w);
    //std::cout << z << "\n";
    
    int v = otherfunc(y);
    //std::cout << v;
    */
    return 0;
}
