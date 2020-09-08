#키보드의 동작원리 업/다운 이벤트가 발생,,
#응용프로그램들 ->각자 독립적인 메모리 공간을 가지기때문에 서로 침범 불가 
#dll파일들 ->공유가능 ->공유메모리 영역에 dll을 침투시켜서~ 

from pynput.keyboard import Key, Listener , KeyCode

def key_pressed(key):
    print("pressed{}" . format(key))

def key_released(key):
    print("released{}".format(key))

    if key == Key.esc:
        return False
with Listener(on_press = key_pressed , on_release = key_released) as listener :
    listener.join() 