'''
한글 = ((초성*21)+중성 )*28 +종성+ 44032
chr(((0*21)+0 )*28 +0+ 44032)
> '가' 가 나오는 결과가 되는 거임
초성을 구하려면? 
초성 =((X -44032) /28) /21 _초성의 인덱스 나옴
중성 =((X -44032) /28) %21 _중성의 인덱스 
종성 =(X -44032) %28 _종성의 인덱스 
'''
import time 
import random 
import os

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
       "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
        "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

user_input = input("입력 >")
word_list = list(user_input)


def break_kor(string):
    word_list = list(string)
    break_word = []

    for k in word_list:
        if ord(k) > ord("가") and ord(k) <= ord("힣"):
            # 유니코드상 몇번째 글자인지 구한다
            char_index = ord(k) - ord('가')

            char1 = int((char_index / 28)/21)
            break_word.append(CHO[char1])

            char2 = int((char_index/28) % 21)
            break_word.append(JUNG[char2])

            char3 = int(char_index % 28)
            break_word.append(JONG[char3])

            if char3 > 0:
                break_word.append(JONG[char3])
        else:
            break_word.append(k)
    return break_word

    print("입력 : {}". format(user_input))
    print("분해 : {}". format(break_word))

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

    src = break_kor(q)
    tar = break_kor(user_input)

    print(src)
    print(tar)

    if user_input =="/exit":
        break

    correct = 0 
    for i , c in enumerate(tar):
        if i >= len(src):
            break 
        if c == src[i]:
            correct += 1
    
    tot_len = len(src)
    c= correct / tot_len *100  #정확도 백분율 
    e= (tot_len - correct) / tot_len* 100 #오타율
    speed =(correct / end_time) *60 #60 분당 타수 

    
    print("속도: {:0.2f} 정확도 : {:0.2f} 오타율 :{:0.2f}" .format(speed, c ,e))
    os.system("pause")

