/*
Write a method to print the last K lines of an input file using C++.
*/

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void LastKLines(string file_name, int k)
{
  ifstream input_stream (file_name);
  int oldest = 0;
  string lines[k];
  while (input_stream.peek() != EOF)
  {
    getline(input_stream, lines[oldest % k]);
    oldest++;
  }
  
  int start = oldest % k;
  for (int i = 0; i < k; i++)
  {
    cout << lines[(i+start) % k] << endl;
  }
}

int main(int argc, char const *argv[])
{
  LastKLines("TEST", 4);
  return 0;
}

