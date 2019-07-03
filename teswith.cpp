//Space for testing C++ things

#include <iostream>
#include <cmath>

using namespace std;

/*
int main()
{
    int n, factorial = 1;
    cout << "Enter a positive integer: ";
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;   // factorial = factorial * i;
    }
    cout<< "Factorial of "<<n<<" = "<<factorial;
    return 0;
}
*/

/*
//SQUARE ROOT CALCULATION
int main()
{ double n,squarert;
  cout << "Enter an number and this should return the square root! : ";
  cin >> n;

  //Now the calculation...

  squarert = sqrt(n);

  cout << "Ya square root of "<<n<<" is " << squarert;

  return 0;
}
*/

//Trying to define a function! Adding together two numbers!

/*
int add(int, int); //Declaration (?)
int main()
{
  int n1, n2,sum;
  cout << "Enter two numbers... the programme will add them together: ";
  cin >> n1 >> n2;

  sum = add(n1, n2);

  cout << "The sum of the two entered numbers, "<<n1<<" and "<<n2<<", is " << sum;

  return 0;

}

int add(int a, int b) // Actually DEFINING the funciton now??
{
    int add;
    add = a + b;
    // Return statement
    return add;
}
*/

/*
//Function Overloading
void display(int);
void display(float);
void display(int, float); //Declaring prototypes, this time 3 functions have the same name

int main()
{
  int a = 6;
  float b = 6.78;
  display(a);
  display(b);
  display(a,b);

  return 0;

}

void display(int var)

{

  cout << "Da intaga' is dis' mon' : " << var << endl;

}


void display(float var)

{

  cout << "Da floatin' ting is dis' mon' : " << var << endl;

}


void display(int var1,float var2)

{

  cout << "Da intaga' is dis' mon' : " << var1;
  cout << " and da floatin' ting is dis' mon : " << var2;

}
*/

//Trying to understand default arguments

/*
void display(char = '*', int = 1);
int main()
{
  cout << "No arguament passed: \n ";
  display();

  cout << "\nFirst arguament passed: \n ";
  display('#');

  cout << "\nFirst and second arguaments passed : \n :";
  display('$',5);

  return 0;
}


void display(char c, int n)
{
  for(int i = 1; i <= n; ++i)
  {
    cout << c;
  }
  cout << endl;
}
*/

//Another attempt at factorials using recursion

/*
int factorial(int);

int main()
{
  int n;
  cout << "Find the factorial of the number you type in 'ere' : ";
  cin >> n;
  cout << "Factorial of "<<n<<" is : " << factorial(n);
  //return 0;
}

int factorial(int n)
{
  if (n > 1)
  {
    return n*factorial(n-1);
  }
  else
  {
    return 1;
  }
}
*/

//TIME TO WORK WITH ARRAYS

/*
int main()
{
  int oort[6], sum = 0;
  cout << "Enter, like, six numbers : ";
  for(int i=0; i<6; ++i)

  {
    cin >> oort[i];
    sum +=  oort[i];
  }

  cout << "Sum = " << sum << endl;
  return 0;
}
*/
/*
int main()
{
    int yaar[3][2] =
    {
        {2, 7},
        {4, 8},
        {1, 3}
    };
    //lets print the whole array ting yaar

    for(int i = 0; i < 3; ++i)
    {
        for(int j = 0; j < 2; ++j)
        {
            cout << "yaar[" << i << "][" << j << "] = " << yaar[i][j] << endl;
        }
    }
    return 0;
}
*/
