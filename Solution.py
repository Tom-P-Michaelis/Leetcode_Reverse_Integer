class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Determine if number is proceeded by negative 
        negative = False
        if x < 0:
          negative = True
          
        # Converting each digit to a string in a list 
        x = abs(x)
        word = str(x)
        listed = [char for char in word]
        blist = []
        
        # Performing reverse by adding to a new list 
        while len(listed) > 0 :
            blist.append(int(listed.pop(-1)))

        # return to integer 
        blist = blist
        counter = 0
        
        # multiplying by correct factor of 10 and summing 
        for n in range(len(blist)):
           num = blist.pop(-1) 
           power = 10**(n)
           counter =  counter + power*num
        
        # remembering if number was negative 
        if negative == True:
           counter = counter*(-1)
        
        # Memory considerations
        if counter >= 2**31-1  or counter <= -2**31:
           counter = 0

        return counter
