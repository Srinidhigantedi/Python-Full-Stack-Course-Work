data ={

'Satwik':{'status': True, 'python': 100, 'mysql': 99, 'softskills': 88},
'Ravi':{'status': False, 'python': 0, 'mysql': 0, 'softskills': 0},
'Dileep':{'status': True, 'python': 36, 'mysql': 22, 'softskills': 40},
'Kamal':{'status': True, 'python': 46, 'mysql': 84, 'softskills': 72},
'Aswin':{'status': True, 'python': 83, 'mysql': 96, 'softskills': 54}
    }

user = input('Enter the student name:')

if user in data:
    if data[user]['status']:
        sum = data[user]['python']+data[user]['mysql']+data[user]['softskills']
        avg = sum/3
        if avg > 80:
            print(f"Congrats {user} you got 'A' grade")
        elif avg > 60:
            print(f"Better luck next time {user} you got 'B' grade")
        elif avg > 40:
            print(f"Need improvement {user} you got 'c' grade")
        else:
            print(f"{user} failed, Bring your parents")
    else:   
        print(f"{user} didn't write the exams.")
else:
    print(f"{user} data not found")
