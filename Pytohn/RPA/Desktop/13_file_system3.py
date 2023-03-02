#주어진 경로가 파일인지? 폴더인지?
import os
print(os.path.isdir("Exel")) #Exel은 폴더인가?
print(os.path.isfile("Exel")) #Exl은 파일인가?

# 만약 지정된 경로에 해당하는 파일 / 폴더가 없다면?
print(os.path.isdir("run_btn.png")) # run_btn.png은 폴더인가? 파일이 없으니 False
print(os.path.isfile("run_btn.png")) # run_btn.png은 파일인가? 파일이 없으니 False

# 주어진 경로가 존재하는지?
# if os.path.exists("run_btn.png"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재 하지 않습니다")

# 파일 만들기
# open("new_file.txt","a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt","new_file_rename.txt") # new_file.txt -> new_file_rename.txt로 이름 변경

# 파일 삭제
# os.remove("new_file_rename.txt") 

# 폴더 만들기
# os.mkdir("new_folder")
# os.mkdir("new_folders/a/b/c") # 실패 : 하위 폴더를 가지는 폴더 시도
# os.makedirs("new_folders/a/b/c") # 성공 : 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
# os.rename("new_folder","new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename") # 폴더 안이 비었을 경우에만 가능

# import shutil
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든파일이 삭제될 수 있으므로 주의!!!