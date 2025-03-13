student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# so sánh với toán tử sum
#Cách 1: dùng sum
total_course = sum(student_scores)
print("Giá trị tổng là:", total_course)
#Cách 2: dùng vòng for
sum = 0
for score in student_scores:
    sum += score
print("Giá trị tổng là:", sum)

# so sánh với toán tử max
#Cách 1 : dùng max
print("Giá trị lớn nhất là:", max(student_scores))

#Cách 2: dùng vòng for + if
max = student_scores[0]

# Duyệt qua danh sách để tìm giá trị lớn nhất
for score in student_scores:
    if score > max:
        max = score

print("Giá trị lớn nhất là:", max)
