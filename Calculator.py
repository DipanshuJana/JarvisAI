import math
import re

def calculate(query):
    numbers = re.findall('[0-9]+', query)
    n = [int(i) for i in numbers]
    try:
        if ('factorial of' in query) or ('factorial' in query):
            if (len(numbers) > 1):
                return 'Please say only one number at a time.'
                
            if (len(numbers) < 1):
                return 'Please say atleast one number.'

            else:
                return math.factorial(n[0])

        if ('sin' in query) or ('sin of' in query):
            if (len(numbers) > 1):
                return 'Please say only one number at a time.'

            if (len(numbers) < 1):
                return 'Please say atleast one number.'
        
            else:
                return format(math.sin(num[0]), ".2f")
                
        if ('cos' in query) or ('cos of' in query):
            if (len(numbers) > 1):
                return 'Please say only one number at a time.'

            if (len(numbers) < 1):
                return 'Please say atleast one number.'
            
            else:
                return format(math.cos(num[0]), ".2f")

        if ('tan' in query) or ('tan of' in query):
            if (len(numbers) > 1):
                return 'Please say only one number at a time.'

            if (len(numbers) < 1):
                return 'Please say atleast one number.'
            
            else:
                return format(math.cos(num[0]), ".2f")

        if ('+' in query) or ('add' in query):
            if (len(numbers) < 1):
                return 'Please say atleast one number.'
            else:
                return sum(n)

        if ('-' in query) or ('substract' in query):
            if (len(numbers) < 1):
                return 'Please say atleast one number.'
            else:
                result = 0
                for num in n:
                    result -= num

                return result

        if ('*' in query) or ('multiply' in query):
            if (len(numbers) < 1):
                return 'Please say atleast one number.'
            else:
                result = 0
                for num in n:
                    x *= num

                return result
            
        if ('/' in query) or ('divide' in query):
            if (len(numbers) < 2):
                return 'Please say atleast two numbers.'

            if (len(numbers) > 2):
                return 'Please say only two numbers.'

            if ('0' in numbers):
                return "Can't divide a number by 0."
            else:
                print (n[0] / num[1])
                speak (n[0] / num[1])

        if ('hcf' in query) or ('gcd' in query):
            if (len(numbers) < 2):
                return "I can't handle with more than two numbers."

            if (len(numbers) > 2):
                return 'Please say atleast two numbers.'

            else:
                commonFactors = []
                for num in [i for i in range(1, n[0]+1) if n[0]%i == 0]:
                    if num in [i for i in range(1, n[1]+1) if n[1]%i == 0]:
                        commonFactors.append(num)

                return max(commonFactors)

        if ('lcm' in query):
            if (len(numbers) < 2):
                return "I can't handle with more than two numbers."

            if (len(numbers) > 2):
                return 'Please say atleast two numbers.'

            else:
                maxNum = max(n)
                while (True):
                    if (maxNum % n[0] == 0) and (maxNum % n[1] == 0):
                        break
                    maxNum += maxNum
                return maxNum

        if ('mean' in query):
            return sum(n)/2

        if ('median' in query):
            if (len(n) % 2 == 0):
                return n[int(len(n)/2 - 1)] + n[int(len(n)/2)]/2
            else:
                return n[int(len(n)/2)]
        
        if ('mode' in query):
            return max(set(n), key = n.count)

        if ('value of pi' in query):
            return math.pi()
        
    except Exception as e:
        return 'I am unable to do the calculations right now.'