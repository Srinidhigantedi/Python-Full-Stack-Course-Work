try:
    '''
    if a>10:
        print("good")

       '''
    '''
    a=int(input())
    '''
    '''
    a="s"+1
    '''
    '''
    a=2/0
    '''
    '''
    b=[1,2,3]
    a=print(b[3])
    '''
    '''
    b={"name":"srinidhi","id":"12345"}
    a=print(b["name"])
    '''
except NameError:
    print('a is not defined')
except ValueError:
    print('Enter the requested data type')
except TypeError:
    print('Data types are different.')
except ZeroDivisionError:
    print("Can't divide with zero")
except IndexError:
    print('The index is not present')
except KeyError:
    print('In dict this key is not present')
else:
    print('No Error')
finally:
    print("End of the block")
