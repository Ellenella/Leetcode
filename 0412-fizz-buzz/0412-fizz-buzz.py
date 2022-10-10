class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [None] * (n)
        for i in range(1, n+1):
            if((i%3==0) and (i%5==0)):
                result[i-1] = "FizzBuzz"
                continue
            elif(i%5==0):
                result[i-1] = "Buzz"
                continue
            elif (i%3==0):
                result[i-1] = "Fizz"
                continue
            else:
                result[i-1] = str(i)
                continue
        return result

                
        