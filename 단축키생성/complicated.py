from pynput.keyboard import Key, Listener , KeyCode
import win32api


MY_HOT_KEYS = [
    {"function1" : {Key.ctrl_l, Key.alt_l, KeyCode(char="n") }},
    {"function2" : {Key.shift, Key.ctrl_l , KeyCode(char="b")}},
    {"function3" : {Key.shift, Key.alt_l , KeyCode(char="g")}}
] #컨트롤, 알트 , n 키가 눌리면 funtion1이 동작하게함 , 

current_keys = set() # 현재 눌려진 키를 기억하는 변수 b

def function1():
    print("함수 1 호출")
    win32api.WinExec("calc.exe")

def function2():
    print("함수 2 호출")
    win32api.WinExec("notepad.exe")

# def function3():
#     print("함수 3 호출")
#     win32api.WinExec("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
# 크롬 여는 단축키 인데 크롬 실행 파일 문제인지 안열림  나중에 오류 분석하기 


def key_pressed(key):
    print("pressed{}" . format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0] #(data.keys())는 딕트 형태 -> 리스트로 캐스팅
        KEYS = list(data.values())[0]

        if key in KEYS:
            current_keys.add(key)
            
            if all(k in current_keys for k in KEYS): #모든 리터러블이 트루면 트루 하나라도 펄스면 펄스  
            # for k in KEYs:
            #     if k not in current_keys:
            #         checker = False
            #         break 
            #     if checker :
                function =eval(FUNCTION)
                function()

def key_released(key):
    print("released{}".format(key))

    if key == Key.esc:
        return False
with Listener(on_press = key_pressed , on_release = key_released) as listener :
    listener.join()