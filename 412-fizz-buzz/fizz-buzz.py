class Solution(object):
    def fizzBuzz(self, n):
        lst = []
        
        for i in range(1, n + 1):
            # 1. Check for FizzBuzz first
            if i % 3 == 0 and i % 5 == 0:
                lst.append("FizzBuzz")
            # 2. Check for Fizz
            elif i % 3 == 0:
                lst.append("Fizz")
            # 3. Check for Buzz
            elif i % 5 == 0:
                lst.append("Buzz")
            # 4. If none match, append the number as a string
            else:
                lst.append(str(i))
                
        return lst