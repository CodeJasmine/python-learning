"""
百分制成绩转换为等级制成绩
"""

score = float(input('请输入成绩：'))
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
elif score >= 0 and score < 60:
    grade = 'E'
else:
    grade = '成绩无效！'
print('对应的等级是：', grade)
