# Python program to execute 
# function directly 
def my_function(): 
    print ("I am inside function")



# Python program to execute 
# main directly 
print ("Always executed")
 
if __name__ == "__main__": 
    print ("Executed when invoked directly")
    
    # Python program to use 
    # main for function call.
    my_function()
    
else: 
    print ("Executed when imported")
