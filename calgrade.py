# ตัวแปรสำหรับนับจำนวะเกรด
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_F = 0

while True:
    score = int(input("Enter test score: "))
    
    # เช็คว่าเป็น -1 หรือไม่
    if score == -1:
        break  # หยุดการทำงานเมื่อกรอก -1
    
    # ตัดเกรดตามคะแนน
    if 90 <= score <= 100:
        grade_A += 1
        print("Grade is A")
    elif 80 <= score <= 89:
        grade_B += 1
        print("Grade is B")
    elif 70 <= score <= 79:
        grade_C += 1
        print("Grade is C")
    elif 60 <= score <= 69:
        grade_D += 1
        print("Grade is D")
    elif 0 <= score <= 59:
        grade_F += 1
        print("Grade is F")
    else:
        print("คะแนนไม่ถูกต้อง กรุณากรอกคะแนนใหม่")

# แสดงผลจำนวนเกรด
print("\nStudent Grades:")
print(f"A: {grade_A} คน")
print(f"B: {grade_B} คน")
print(f"C: {grade_C} คน")
print(f"D: {grade_D} คน")
print(f"F: {grade_F} คน")

