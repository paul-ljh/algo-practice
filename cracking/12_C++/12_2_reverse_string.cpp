/*
Implement a function void reverse(char* str) in c++ which reverses a null-terminated string.
*/
#include <iostream>
#include <string>
using namespace std;

void reverse(char* str) {
  for (int i = 0; i < strlen(str) / 2; ++i) {
    char temp = str[i];
    str[i] = str[strlen(str) - i - 1];
    str[strlen(str) - i - 1] = temp;
  }
}

int main(int argc, char const *argv[])
{
  char empty_str[1] = "";
  reverse(empty_str);
  cout << ((strcmp(empty_str, "") == 0) ? "PASS" : "FAIL") << endl;

  char even_str[5] = "paul";
  reverse(even_str);
  cout << ((strcmp(even_str, "luap") == 0) ? "PASS" : "FAIL") << endl;

  char odd_str[6] = "pauli";
  reverse(odd_str);
  cout << ((strcmp(odd_str, "iluap") == 0) ? "PASS" : "FAIL") << endl;

  return 0;
}

