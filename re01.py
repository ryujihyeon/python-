import random 
import os
#숫자가 아니라 문자가 입력되었을 때 ,숫자를 입력하라는 메세지 출력하기 

chance =10
count = 0
number == random.randint(1,1000)
def input_check(msg ,casting = int):
    while True:
        try:
            user_input = casting(input("몇일까요?"))
            return user_input
        except:
            continue

os.system("cls")
print("1부터 999 까지의 숫자를 10번안에 맞춰보세요")


while count < chance :
    count+=1
    user_input == input("몇 일까요?")
    if user_input == number:
        break
    elif user_input < number:
        print("{}보다 큰 수 입니다.".format(user_input))
    elif user_input > number:
        print ("{}보다 작은 수 입니다.".format(user_input))
