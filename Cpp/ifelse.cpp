// #include <iostream>
// using namespace std;

// int main() {
//     int n = 45;
    
//     if (n>=0) {
//         cout << "Positive number" << endl;
//     }
//     else {
//         cout << "Negative number" << endl;
//     }

// return 0;

// }

// #include <iostream>
// using namespace std;
 
// int main(){
//     int age;
//     cout<<"enter your age:";
//     cin>>age;
//     if (age>=18){
//         cout<<"you are eligible to vote"<<endl;
//     }
//     else{
//         cout<<"you are not eligible to vote"<<endl;
//     }

// }


#include <iostream>
using namespace std;
int main(){
    int a, b;
    cout<<"enter to" <<" numbers: ";
    cin>>a>>b;     
    if (a>b){
        cout<<a<<" is greater than "<<b<<endl;
    }
    else if (b>a){
        cout<<b<<" is greater than "<<a<<endl;
    }
    else{
        cout<<"both numbers are equal"<<endl;
    }

}