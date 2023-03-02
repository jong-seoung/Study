import shutil

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("Desktop//run_btn.png","test_folder") # 원본 경로, 대상 경로
# shutil.copy("Desktop//run_btn.png","test_folder/copide_run_btn.png") # 다른 이름으로 복사
# shutil.copyfile("Desktop//run_btn.png","test_folder/copide_run_btn2.png") # 원본 경로, 대상 파일 경로
# shutil.copy2("Desktop//run_btn.png","test_folder/copide_run_btn3.png") # 원본 경로, 대상 폴더

# copy, copyfile : 메타정보 복사 x
# copy2 : 메타정보 복사 o

# 폴더 복사
# shutil.copytree("test_folder","test_folder2") # 원본 폴더, 다른 이름으로 복사

# 폴더 이동
# shutil.move("test_folder","test_folder2")
shutil.move("test_folder2","test_folder") # 폴더명이 변경되는 효과