#2 Assigning variable names and using Python to identify the data type ofeach variable:

v = int(2)
print(v)

w= float(2.0)
print(w)

x = str(10j)
print(x)

y = str("2 Cool for School")
print(y)

z = str("True")
print(z)




#3 list named "A" containing all the values from above

A = [2, 2.0, '10j', '2 Cool for School', 'True']
A



#4 string named "B" containing the input "I like pie more than cake." 

B = "I like pie more than cake."
#    01234567890123456789012345

#      Using string slicing, extract “I like”
B[:6]

#      Using string slicing, extract “pie more"
B[6:16]

#      Using string slicing, extract “than cake"
B[15:]

#      Using string slicing, extract “I like more cake"
B[:6] +  B[10:16] + B[21:25]




#5 Design a function in which I can input a value, when I input the value, it returns the 4 possible outputs

def multiple_of_num(x):
    """ Return the string "foo"if x is multiple of 3 , 
    return the string "bar" if x is a multiple of 5 ,
    return the string "foobar" if x is a multiple of 15 ,
    if x does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"
    
    multiple_of_num(18)
    'foo'
    """
    if x % 15==0:
      return "foobar"
  
    elif x % 3 == 0:
         return "foo"
       
    elif x % 5 == 0:
       return "bar"
   
    else:
        return "Not a multiple of 3, 5, or 15"
   
 #Testing the function (multiple_of_num)
    multiple_of_num(18)
    multiple_of_num(25)
    multiple_of_num(45)
    multiple_of_num(202)
    
#Since 3,5,15 have common multiples, below is a more detailed function

def multiple_of_num1(x):
    """ Return the string "foo"if x is multiple of 3 , 
    return the string "bar" if x is a multiple of 5 ,
    return the string "foobar" if x is a multiple of 15 (which is also a multiple of 3 and 5) ),
    if x does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"
    
    multiple_of_num1(45)
    'foo bar foobar'
    """
  
    if ((x % 3 == 0) and not (x % 5 == 0) and not (x % 15 == 0)):
      print("foo")  
       
    elif x % 5 == 0 and not x % 3 == 0 and not x % 15 ==0:
       print ("bar")
   
    elif x % 15==0:
      print("foo","bar","foobar")
    
    else:
        print("Not a multiple of 3, 5, or 15")
   
 #Testing the function (multiple_of_num)
    multiple_of_num1(3)
    multiple_of_num1(15)
    multiple_of_num1(20)
    multiple_of_num1(75)
    multiple_of_num1(673)
