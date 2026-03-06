# Data types
a = 20
print(type(a))

b = 'python'
print(type(b))

a = True
b = False
print(type(a))
print(type(b))

c =10.6
print(type(c))

d = 3+4j
print(type(d))

marks = [34,65,87,53,67,98,90,86]
print(marks)
print(type(marks))

items = ['sugar', 'milk', 'rice', 'salt']
print(items)
print(type(items))

mixed_list = ['sugar', 45, 67, 83, 'rice']
print(mixed_list)
print(type(mixed_list))

mixed_list.append('curd')
print(mixed_list)

cgpa = (8.6, 9.4, 8.0, 7.6, 10.0)
print(cgpa)
print(type(cgpa))

total_score = (9.8, 7.9, 8.3, 'passed', 8.8, 'passed')
print(total_score)
print(type(total_score))

# Tuple is immutable, once we create tuple then we can not add or remove from the tuple.

container = None
print(type(container))

store = {'Books', 'pens', 'pencils', 'markers'}
print(store)
print(type(store))

# Set is immutable and it doesn't contain duplicte elements.

student = {'Roll number': '23NM1F0018', 'Name': 'Raju', 'Branch': 'MCA', 'score': 8.9}
print(student)
print(type(student))

# Adding another element to the dictionary as follows
student['Grade']= 'A'
print(student)
