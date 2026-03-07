#module is group of functions and variables
#we have to call the import file_name to import functions and variables
#we write the code in a file and reusing it in other file.
#we have two methods of creating modules,this is the first method
# we have written the functions and variables in the operations file and asscessing in the file_operations
'''
#METHOD-1
import operations

operations.add(6,7)
operations.sub(6,7)
operations.mul(6,7)
operations.div(6,7)
'''
'''
#METHOD-2
import operations as op
op.add(6,7)
op.sub(6,7)
op.mul(6,7)
op.div(6,7)
'''
'''
#METHOD-3
#no used much
from operations import add,sub
add(6,7)
sub(6,7)
'''
#METHOD-4
from operations import *
add(6,7)
sub(6,7)
mul(6,7)
div(6,7)



