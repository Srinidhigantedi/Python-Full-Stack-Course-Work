try:
    a=a+'8'
    print(a[4])
except(NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f'Error Occured: {e}')
else:
    print("No Errors")
finally:
    print("End of the Block")
