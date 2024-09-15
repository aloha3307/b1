# B1 SAVES 備份程式
#

import os,shutil

from datetime import datetime
current_time=(datetime.now().strftime('%Y%m%d%H%M%S'))

sav_note=input("請輸入存檔備註?(英文或數字為佳，若無備註直接按Enter開始備份)")

with open("b1_install_path.ini","r",encoding="utf-8") as f:
    source_dir=f.read()
source_dir=source_dir.replace("\n","").strip()

dist_dir = os.getcwd()

# 指定文件路徑
if sav_note!="":
    new_folder_name = f"B1-SAV-{current_time}-{sav_note}"
else:
    new_folder_name = f"B1-SAV-{current_time}"

dist_folder_path = dist_dir+"\\"+new_folder_name

# 檢查資料夾是否存在
if os.path.exists(dist_folder_path) and os.path.isdir(dist_folder_path):
    shutil.rmtree(dist_folder_path)
    print(f'資料夾 {dist_folder_path} 已刪除')
else:
    print(f'資料夾 {dist_folder_path} 不存在')

if not os.path.exists(dist_folder_path):
    os.makedirs(dist_folder_path)
    print(f'新資料夾 {dist_folder_path} 已建立!')
else:
    print(f'新資料夾 {dist_folder_path} 已存在!')

##################################################
##################################################

# 複製所有 .sav 檔案
for file_name in os.listdir(source_dir):
    if file_name.endswith('.sav'):
        full_file_name = os.path.join(source_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dist_folder_path)
            print(f'檔案 {file_name} 已複製到 {dist_folder_path}')
##################################################
##################################################
input(f'B1存檔備份完成! 資料夾:{dist_folder_path}')
