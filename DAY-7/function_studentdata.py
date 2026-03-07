def student_data(info):
     print(f'name: {info[0]}')
     print(f'Course: {info[1]}')
     print(f'Gra_Year: {info[2]}')
     print('------End------')

data=[
    ['Varsha','PFS','2026'],
    ['Srinidhi','JFS','2026'],
    ['Dileep','AD','2026'],
    ['Sangeetha','DC','2026']]
for i in data:
    student_data(i)
