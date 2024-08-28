#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number

def square(a): #defining funtion name 
    result = pow(a,2) #defining the functionality of the square function which to calculate power 2 of the passed parameter
    return result  #returning the calculated value
ans= square(12)  #calling the function
print("The square root of the given number is : " , ans ) #printing the answer after calling the function


#answer
"""
The square root of the given number is :  144

"""
