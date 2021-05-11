
myArray = [
    [100, 500, 600],
    [900],
    [5, 8],
    [1, 2 ,3], 
    [1, 2, 3],
]


# a function checks that number
# is or not a Prime number
def isPrime(number):

    flag = True
    if number > 1:
        # we will go just till
        # half of our number 
        # because no number have 
        # divisor after half of it
        for i in range(2, number // 2):
             if number % i == 0:
                # found divisor, then it's a composite number
                flag = False
                break
        
        # checking do we found a composite number or not:
        if flag == False:
            return False
        elif flag == True:
            return True

def rowWithOnePrime(arr):


    # iterating by each list in array and checking each element in list for Prime
    for i in arr:

        # initialinzing a Counter of Primes for each list
        cnt = 0

        for j in i:
            # if element is Prime then increament Counter
            if isPrime(j) == True:
                cnt += 1 

        # checking counter of each row
        if cnt == 1:
            return "YES " + str(i)
            break


def rowDivisibleBy100(arr):

    # iterating by each row in array
    # then iterating by each element in row
    for i in arr:
        
        allDivisible = True 
        for j in i:
            if j % 100 != 0:
                allDivisible = False
                break

        # checking if all elements in arr are divisible
        if allDivisible == True:
            return "YES " + str(i)
            break


        



print(rowWithOnePrime(myArray))
print(rowDivisibleBy100(myArray))
     
    