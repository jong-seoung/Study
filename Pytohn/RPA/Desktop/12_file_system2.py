# 파일 목록 가지고 오기
from ast import pattern
import os
from unittest import result
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("Desktop")) # 주어진 폴더 밑에 모든 폴더, 파일 목록 가지고오기

#파일 목록 가져오기 (하위 폴더 포함)
# result = os.walk("Desktop") # 주어진 폴더 밑에 모든 폴더, 파일 목록 가지고오기
# result = os.walk(".") # 현재 폴더 밑에 모든 폴더, 파일 목록 가지고오기 

# for root, dirs, files in result:
    # print(root,dirs,files)

# 만약 폴더 내에서 특정 파일들을 찾을려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾을려면
# *.xlsx, *.txt, 자동화*.png
import fnmatch
pattern = "*.png" # .png로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
            result.append(os.path.join(root,name))
print(result)