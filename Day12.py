Students = 0
Profs = 0

a = int(input('pleease enter number of emails:'))
for i in range(a):
    b = input('Enter email:')
    if b.split('@')[1] == 'student.college.edu':
        Students = Students+1
    elif b.split('@')[1] == 'prof.college.edu':
        Profs = Profs+1
        print('number of students=' ,Students , 'number of professors=' , Profs)