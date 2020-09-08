import time 
import random 
import os

WORD_LIST= [
    "동해물과 백두산이 마르고 닳도록",
    "하느님이 보우하사 우리나라 만세",
    "무궁화 삼천리 화려강산",
    "대한사람 대한으로 길이 보전하세",
    "남산위에 저소나무 철갑을 두른듯",
    "바람서리 불변함은 우리 기상일세",
    "가을하늘 공활한데 높고 구름 없이"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n' )).strip()
    end_time = time.time() - start_time

    correct = 0 
    for i , c in enumerate(user_input):
        if i >= len(q):
            break 
        if c == q[i]:
            correct += 1
    
    tot_len = len(q)

    c= correct / tot_len *100  #정확도 백분율 
    e= (tot_len -correct) / tot_len* 100 #오타율
    speed =(correct / end_time) *60 #60 분당 타수 

    print("속도: {:0.2f} 정확도 : {:0.2f} 오타율 :{:0.2f}" .format(speed, c ,e))
    os.system("pause")