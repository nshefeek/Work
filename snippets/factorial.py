def FirstFactorial(num): 
    # code goes here
    if num == 1:
        return 1
    else:
        return FirstFactorial(num -1) * FirstFactorial(num)
    
# keep this function call here  
result = FirstFactorial(5)
print(result)




  
