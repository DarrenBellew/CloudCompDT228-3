#Palindrome of input
#Darren Bellew
#Lab 3


def palindrome(word):
  if(word[::-1] == word):
    return True
  return False


userInput = raw_input("Please input string to be tested: ")
if palindrome(userInput):
  print(userInput + " is a palindrome.")
else:
  print(userInput + " is not a palindrome.")

