try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive value")
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No Errors')
finally:
    print("End of the Block")
