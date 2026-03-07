try:
    a=int(input())
    print(a[4])
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No Errors')
finally:
    print("End of the Block")
