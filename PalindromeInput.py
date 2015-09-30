#Palindrome of input
#Darren Bellew
#Lab 3

#Function to do python
def palindrome(word):
  if(word[::-1] == word):
    return True
  return False

#Main Code

#preset words:
wordList = ["Oxo", "OXO", "123454321", "ROTATOR", "12345 54321", raw_input("Please input string to be tested: ")]

for i in range (0, len(wordList)):
  if palindrome(wordList[i]):
    print(wordList[i] + " is a palindrome.")
  else:
    print(wordList[i] + " is not a palindrome.")

