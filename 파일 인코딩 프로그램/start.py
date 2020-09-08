import os 
from chardet import detect #인코딩타입을 구할수 있는 라이브러리
import argparse

#재귀함수 
def search_dir(dirname):
    result_list =[]
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path =os.path.join(dirname, filename)

        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path)) #append하면 리스트안에 리스트 들어가니까 extend
            #search_dir 함수가 search_dir을 호출하는 함수 ->재귀함수
        else:
            result_list.append(full_path)
    return result_list 

def get_encoding_type(filepath):
    with open(filepath, "rb") as f: #바이너리 데이터로 읽음
        rawdata =f.read()

    codec = detect(rawdata)
    return codec["encoding"]

INCLUDE_EXT_LIST = [".txt",".smi"]
#실행시에 넘어오는 인자값 받기
parse = argparse.ArgumentParser()
parse.add_argument("-f",type=str)
parse.add_argument("-e",nargs="+")
args = parse.parse_args()


if args.f is not None:
    path = args.f
    file_lists =search_dir(path)

    if args.e is not None:
        if len(args.e) >0:
            INCLUDE_EXT_LIST =[]
            print(INCLUDE_EXT_LIST)
            for e in args.e:
                if e[0:1] ==".":
                    INCLUDE_EXT_LIST.append(e)
                else:
                    INCLUDE_EXT_LIST.append("."+e)
            #INCLUDE_EXT_LIST = [e[0:1] == "."else ".{}" . format(e.lower())for e in in args.e]
        
        for file in file_lists:
            filename ,ext = os.path.splitext(file) #파일과 ext를 분리해주는함수
            tempfile = filename + "_tmp" +ext

            if ext.lower() in INCLUDE_EXT_LIST:
                encoding = get_encoding_type(file)
                if encoding.lower().find("utf")< 0:
                    try:
                        with open(file, "r") as read, open(tempfile,"w", encoding="utf-8") as write:
                            write.write(read.read()) #리드파일을 읽어서 라이트파일을 라이트함

                        os.unlink(file) #원본파일 삭제
                        os.rename(tempfile, file)
                        print("{}이 저장되었습니다".format(file))
                    except:
                        pass
                    finally:
                        if os.path.exists(tempfile):
                            os.unlink(tempfile)

