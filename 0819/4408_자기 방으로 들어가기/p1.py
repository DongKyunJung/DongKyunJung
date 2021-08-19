import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    student_number = int(input())
    students = []
    road = []
    count = 1
    for i in range(student_number):
        students.append(list(map(int,input().split())))
    for k in range(student_number):
        for j in range(students[k][0], students[k][1]):
            if not j in road:
                road.append(j)
            else:
                count += 1
                break

    print('#{} {}'.format(test_case,count))

