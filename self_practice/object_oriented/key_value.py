Lyft Laptop Interview
Thanks for coming to interview with us today! You will be given 90 minutes to work on the below problem (15 minutes briefing, 60 minutes coding, 15 minutes debriefing). You will be coding independently, but your interviewer is available to answer questions during the whole process, either through chat or in person.
This question simulates solving a problem in a real world setting, separate from the whiteboard problems you'll solve in the rest of your interview. Since we're simulating the real world:
You can use any language and environment you're comfortable with.
You will submit your source code for your interviewer to review, compile, and grade.
Consulting online resources and using open source libraries is completely fair. Use StackOverflow, Rosetta Code, and other sites to find resources. Reusing and adapting code fragments will not penalize your grade; we're grading your solution end-to-end as a whole, more than just the code that you wrote independently. Be sure to add a comment with the link of anything you adapted.
Also note that using a complete solution found online is prohibited, as this does not tell us anything about your coding ability. For the same reason you can’t use ChatGPT, Copilot or similar software.
Your goals should be to get a working and runnable solution, even if it's not complete. Your solution will be graded as follows:
Correctness (40%) - Your code should pass the sample test cases and other test cases you can think of. Handle edge cases sensibly. Don't worry about thread-safety or rogue input that doesn't adhere to the problem spec.
Clean Code (35%) - Your code should be split up into multiple classes or functions when relevant. It doesn't have to be in multiple files. It should have comments where relevant, but don't add comments just for the sake of commenting.
Performance (25%) - If you can make your solution's time and space complexity better, without sacrificing correctness, please do so!
Remember, if you get really stuck, try and make progress however you can. Focus on simple cases, reduce the problem to more simpler components, and ask your interviewer for how to prioritize your time.
After the assignment, you will turn in your code to the interviewer. Your code will be graded by the interviewer.
Here's the problem:
Versioned Key-Value Store
Overview
You are to build a simple key-value store for storing integers (keys are strings, values are integers) and a global version (integer). You will not persist data to disk. You will store the data in memory.
The version number is an integer that increases monotonically. Every time any key is written with a value, the version number is increased. The first write is version number 1. The second write is version number 2, and so on.
The store supports three operations. The first is PUT, which returns the version number of this write. The second operation is the simple GET. This returns the last value mapped to the key. The third operation is the versioned GET. This takes a key and a version number and returns the value mapped to the key at the time of the version number. Assume that all inputs are case sensitive.
The input contains three types of commands corresponding to the three operations supported by the store:
PUT <key> <value>
Set the key name to the value. Key strings will not contain spaces. Print out the version number, the key and the value as PUT(#<version number>) <key> = <value>. The first write in the file should be version number 1, the second should be version number 2, etc.
GET <key>
Print out the key and the last value of the key, or <NULL> if that key has never been set as in: GET <key> = <value>
GET <key> <version number>
Print out the key, the version number and the value of key as it was at the time of the version number, as in GET <key>(#version) = <value>. If the key was not set at the time of the version number, print <NULL> for value. If the input version number is not recorded for a key, return the latest version recorded for that key that is smaller than the input version. See below for examples of formatted output.
Key name:  { { version: value} }
Version: 4
{
key1: {1: 5, 3: 7}
Key2: {2: 6}
}
Get key1 => 5
Get key1, 1 => 5
Get key2, 2 => 6
PUT key1, 7 => 7
Get key1, 2 => 5
Sample Input
PUT key1 5
PUT key2 6
GET key1
GET key1 1
GET key2 2
PUT key1 7
GET key1 1
GET key1 2
GET key1 3
GET key4
GET key1 4
GET key2 1
Sample Output
PUT(#1) key1 = 5
PUT(#2) key2 = 6
GET key1 = 5
GET key1(#1) = 5
GET key2(#2) = 6
PUT(#3) key1 = 7
GET key1(#1) = 5
GET key1(#2) = 5
GET key1(#3) = 7
GET key4 = <NULL>
GET key1(#4) = 7
GET key2(#1) = <NULL>
Notes & Tips
You can download sample files at https://go.lyft.com/interviews-versioned-kv-store (password: enginterviews).
For us to grade your solution, your solution MUST read data from stdin and emit results to stdout. The emitted data must match the format described in the problem. You may use code from http://go.lyft.com/stdin and http://go.lyft.com/stdout as a starting point.
Compile early and often. Run your code against the sample input often to make sure your code continues to work as you make changes.
Think about edge cases and other cases that aren't invoked in the sample input.
Focus on correctness first before clean code and performance. Get your v1 working and passing our test cases, and any other cases you can think of, before iterating on refactoring code or making it more performant. We will value correctness above all when grading.
Submit the zipped solution at http://go.lyft.com/submit-solution. You can do this in Finder by right-click > “Compress” or on the command line: zip -r filename.zip foldername. File name should be versioned-kv-store-15-09-2023.zip. Use interviewer's name and email while uploading instead of candidate's (illiab@lyft.com).






KEY1 (2, version 1), value (5, version 4), value (7, version 9)
GET KEY1 at version 7


Class KeyValueStore:
def __init__(self):
Self.version = 1
Self.store = {}


Def call(self, input):
	Input_array = input.split(“ ”)
	Operation = input_array[0]
	If operation == ‘GET’:
		If len(input_array) == 2:
			self.get(input_array[-1])
		Else:
			self.tricky_get(*input_array[1:-1])
	Else:
		self.put(*input_array[1:-1])


# (value, version)
	Def put(self, key, value):
		If key not in self.store:
			Self.store[key] = []
		self.store[key].append((key, self.version))
		put(“PUT(##{self.version} #{key} = #{value}”)
		Self.version += 1


	Def get(self, key):
		If key not in self.store:
			Return None
		Put “GET #{key} = #{self.store[key][-1][0]}”
		return key, self.store[key][-1][0]


	Def tricky_get(self, key, version):
		If key not in self.store:
			Return None
		Value_array = self.store[key]
		Index = bisect_left(value_array, version, 0, len(value_array), lambda pair: pair[1])
		Target_index = index + 1
		If target_index >= len(value_array):
			Result = (key, value_array[index][0], version)
		elIf value_array[target_index][1] == version:
			Result =(key, value_array[target_index][0], version)
Else: # version not available
Result = (key, value_array[index][0], version)
Put “GET result[0](##{result[-1]}) = #{result[1]}”
Return result








from bisect import bisect_left

class KeyValueStore:
  def __init__(self):
    self.version = 1
    self.store = {}

  def call(self, input):
    input_array = input.split(" ")
    operation = input_array[0]
    if operation == "GET":
      if len(input_array) == 2:
        self.get(input_array[-1])
      else:
        self.tricky_get(input_array[1], int(input_array[-1]))
    else:
      self.put(input_array[1], int(input_array[-1]))


  # (value, version)
  def put(self, key, value):
    if key not in self.store:
      self.store[key] = []
    self.store[key].append((value, self.version))
    result = f"PUT(#{self.version}) {key} = {value}"
    print(result)
    self.version += 1
    return result

  def get(self, key):
    if key not in self.store:
      return None
    result = f"GET {key} = {self.store[key][-1][0]}"
    print(result)
    return result


  def tricky_get(self, key, version):
    if key not in self.store:
      return None
    value_array = self.store[key]
    index = bisect_left(value_array, version, key=lambda pair: pair[1])
    target_index = index + 1
    if target_index >= len(value_array):
      result = (key, value_array[index-1][0], version)
    elif value_array[target_index][1] == version:
      result =(key, value_array[target_index][0], version)
    else: # version not available
      result = (key, value_array[index][0], version)
    print(f"GET {result[0]}(#{result[-1]}) = {result[1]}")
    return f"GET {result[0]}(#{result[-1]}) = {result[1]}"


def test():
  s = KeyValueStore()
  inputs = [
    'PUT key1 5',
    'PUT key2 6',
    'GET key1',
    'GET key1 1',
    'GET key2 2',
    'PUT key1 7',
    'GET key1 1',
    'GET key1 2',
    'GET key1 3',
    'GET key4',
    'GET key1 4',
    'GET key2 1',
  ]
  outputs = [
    'PUT(#1) key1 = 5',
    'PUT(#2) key2 = 6',
    'GET key1 = 5',
    'GET key1(#1) = 5',
    'GET key2(#2) = 6',
    'PUT(#3) key1 = 7',
    'GET key1(#1) = 5',
    'GET key1(#2) = 5',
    'GET key1(#3) = 7',
    'GET key4 = <NULL>',
    'GET key1(#4) = 7',
    'GET key2(#1) = <NULL>',
  ]
  for i in range(len(inputs)):
    print('PASS' if s.call(inputs[i]) == outputs[i] else 'FAIL')

if __name__ == '__main__':
  test()
