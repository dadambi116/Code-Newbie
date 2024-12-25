# 8단 만들어보기 
# version 1
'''
dan = 8
print('=={}단=='.format(dan))

i = 1
print("{}*{}={}".format(dan,i,dan*i))

i +=1
print("{}*{}={}".format(dan,i,dan*i))


# version 2
dan = 8
i = 1
print("=={}단==".format(dan))

while i < 10:
   print("{}*{}={}".format(dan,i,dan*i))
   i += 1
'''

'''
for first in range(2,10):    #왜 range가 '9'까지?
    print("\n",first,"단 --------------")
    for second in range(1,10):  #오ㅐ range가 '10'까지??
        print(first,'X',second,'=',first*second, sep=', ',end=' ')
        

# 보기 좋게 한 줄에 3개씩만 인쇄 하려면??


number = input("\n숫자 입력:")
number = int(number)

while number > 2 and number <= 9:
    print(number,'단',"--------")
    for i in range(1,10):
        print(number,"x",i,"=", number*i)
    number = input("\n숫자 입력:")
    if number == 'e':
        print('종료합니다.') 
        break
    number = int(number) 

if number >= 10:
    print('다시 숫자를 입력해주세요.')
    number = input("\n숫자 입력:")
    number = int(number)

# e를 넣었을 때 종료 안 뜸
'''
    

'''else:
    print('다시 숫자를 입력해주세요.')
    number = input("숫자 입력:")
    number = int(number)
'''

dan = 2
while dan <= 9:
    print("== dan단==".format(dan))
    i = 1
    while i <= 9:
        print("{}*{} = {}".format((dan),(i),(dan*i))
    i +=1
    dan +=1
