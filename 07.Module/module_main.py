# our_class.py 모듈을 가져와서 (import 구문 사용)
# 선생님 이름과 학생 수를 출력하고
# study() 함수와 lecture() 함수를 호출하고

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!

'''
import our_class

print(our_class.teacher_name)
print(our_class.student_count)

our_class.study()
our_class.lecture()

menus = ['떡볶이','치킨','피자','라면','김밥']
print(our_class.go_lunch(menus))
'''
'''
# from 모듈명 import 함수명 및 변수명
from our_class import teacher_name,student_count,study,lecture,go_lunch    # 모듈명을 매번 앞에 안 써도 됨!/ 반대로 어느 모듈에서 온건지 추적하기 어렵렵

print(teacher_name)
print(student_count)

study()
lecture()   # print 안에 넣을 경우 return 반환값이 없고 숨어만 있음 none 이 출력됨
               # sort 의존해서 정렬하는 기능 와 sorted 반환하는 함수  # 함수에서도 다시 한번 더 확인!

menus = ['떡볶이','치킨','피자','라면','김밥']
print(go_lunch(menus))
'''

###3. 패키지 내의 모듈 import
import our_class_dir.official.official_module # as off_md 이렇게 별칭으로 할때 모두 별칭으로 바꾸어줘야 함함
from our_class_dir.unofficial.unofficial_module import study,go_lunch


# 선생님 이름과 학생 수를 출력하고
print(our_class_dir.official.official_module.teacher_name)
print(our_class_dir.official.official_module.student_count)


# study() 함수와 lecture() 함수를 호출하고
study()
our_class_dir.official.official_module.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menus = ['떡볶이','치킨','피자','라면','김밥']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!
print(go_lunch(menus))



 


