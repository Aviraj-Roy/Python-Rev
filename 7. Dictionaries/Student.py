n=int(input('Enter no. of students -> '))
Student_dict={}
for i in range(n):
    print('Enter the details of student ',i+1)
    name = input('Name -> ')
    roll_no = input('Roll No.-> ')
    marks = float(input('Marks -> '))
    Student_dict[roll_no] = {'Name':name, 'Marks':marks}
highest = max(Student_dict.items(),key=lambda x:x[1]['Marks'])
print('Details of highest scorer')
print('Name ', highest[1]['Name'])
print('Roll No', highest[0])
print('Marks ', highest[1]['Marks'])