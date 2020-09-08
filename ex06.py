# ANSI형태의 파일을  UTF-8로 변경하는 프로그램
import os
#폴더, 디렉토리 , 파일명등을 구해야함
from chardet import detect
#인코딩 타입을 구하는 라이브러리 

#재귀함수 
def seach_dir(dirname): #dirname이라는 변수는 path로 넘어가서 사용됨 
    result_list=[]
    filenames =os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)

        if os.path.isdir(full_path):
            result_list.extend(seach_dir(full_path)) #seach_dir함수는 리스트를 리턴하니까 append가 아니라 extend 함수  
        else :
            result_list.append(full_path)
    return result_list

def get_encoding_type(filepath):
    with open(filepath, "rb") as f : #바이너리데이터로 읽음
        rawdata = f.read()

    codec =detect(rawdata)
    return codec["encoding"]

INCLUDE_EXT_lIST = [".txt",".smi"]
path = "C:\\test"
filelists = seach_dir(path) 

for file in filelists:
    filename, ext = os.path.splitext(file) 

    tempfile = filename + "_tmp" + ext

    if ext.lower() in INCLUDE_EXT_lIST:
        encoding = get_encoding_type(file)
        if encoding.lower().find("utf") < 0: 
            try:   
                with open(file,"r") as read , open(tempfile ,"w" , encording="utf-8") as write :
                    write.write(read.read())
                os.unlink(file) #원본 파일 삭제 
                os.rename(tempfile, file)
                print("{}이 저장되었습니다".format(file))
            except:
                pass
            finally:
                if os.path.exists(tempfile):
                    os.unlink(tempfile)



