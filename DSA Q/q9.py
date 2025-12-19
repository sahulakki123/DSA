def Palindrome(self):
    if self==self[::-1]:
        return True
    else:
        return False
        
print(Palindrome("787"))
   