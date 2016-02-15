def calculate_grade(score):
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else:
        return "F"

# WAY #1
# score_file = open("class_grades.txt")

# score_list = score_file.readlines()
# print "score_list"
# print score_list

# score_file.close()

# for score in score_list :
#     print calculate_grade(int(score))



# WAY #2
with open("class_grades.txt") as f:
    for score in f:
        print calculate_grade(int(score))


# WAY #3
# score_file = open("class_grades.txt")

# score = score_file.readline()
# while score != '' :
#     print calculate_grade(int(score))
#     score = score_file.readline()

# score_file.close()

# WAY #4
# score_file = open("class_grades.txt")

# scores = score_file.read()
# score_file.close()

# score_list = scores.split('\n')

# for score in score_list:
#     print calculate_grade(int(score))


