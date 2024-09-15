# B1 SAVE 還原程式
#
import sys,os,shutil

with open("b1_install_path.ini","r",encoding="utf-8") as f:
    DIST_FOLDER_PATH=f.read()
DIST_FOLDER_PATH=DIST_FOLDER_PATH.replace("\n","").strip()+"\\"

def is_folder_or_file(path):
    if os.path.isfile(path):
        #print(f"{path} 是一個檔案")
        return 'FILE'
    elif os.path.isdir(path):
        #print(f"{path} 是一個目錄")
        return 'FOLDER'
    else:
        #print(f"{path} 不是有效的檔案或目錄")
        return 'FALSE'

if __name__ == '__main__':
    try:
        if len(sys.argv)>1 and sys.argv[1]!="":
            #print(argv[1])
            ck = is_folder_or_file(sys.argv[1])
            if ck=='FILE':
                # 先刪除 DIST_FOLDER_PATH 裡同名的 sav
                tmp = DIST_FOLDER_PATH + sys.argv[1].split("\\")[-1]
                # 檢查文件是否存在
                if os.path.exists(tmp):
                    # 刪除文件
                    os.remove(tmp)
                shutil.copy(sys.argv[1], tmp)
                # 將 sav 複制到 DIST_FOLDER_PATH
                print(f"[COPY OK]{tmp}")
            elif ck == 'FOLDER':
                for file_name in os.listdir(sys.argv[1]):
                    if file_name.endswith('.sav'):
                        full_file_name = os.path.join(sys.argv[1], file_name)
                        # 先刪除 DIST_FOLDER_PATH 裡同名的 sav
                        tmp = DIST_FOLDER_PATH + full_file_name.split("\\")[-1]
                        # 檢查文件是否存在
                        if os.path.exists(tmp):
                            # 刪除文件
                            os.remove(tmp)
                        if os.path.isfile(full_file_name):
                            shutil.copy(full_file_name, DIST_FOLDER_PATH)
                            print(f'檔案 {file_name} 已複製到 {DIST_FOLDER_PATH}')
            else:
                pass
        else:
            print('no thing')
    except:
        pass
    input("press enter key to exit...")
