score_student = dict()
scores = list()
for _ in range(int(input())):
	name = input()
	score = float(input())
	if score not in score_student:
		score_student[score] = list()
	score_student[score].append(name)
	scores.append(score)
second_lowest = list(sorted(set(scores)))[1]
student_names = score_student[second_lowest]
for student in sorted(student_names):
	print(student)