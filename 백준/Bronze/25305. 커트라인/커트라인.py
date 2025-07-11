total, prize = map(int, input().split())

students = list(map(int, input().split()))
students.sort(reverse = True)

print(students[prize - 1])