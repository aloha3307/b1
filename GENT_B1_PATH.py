# 取得 B1 安裝路徑 然後存為 b1_install_path.ini
import sys,os

def is_folder_or_file(path):
    if os.path.isfile(path):
        #print(f"{path} 是一個檔案")
        return 'FILE'
    elif os.path.isdir(path):
        #print(f"{path} 是一個目錄")
        return 'FOLDER'
    else:
        input(f"{path} 不是有效的檔案或目錄，按[Enter] 結束...")
        return 'FALSE'

if __name__ == '__main__':
    try:
        if len(sys.argv)>1 and sys.argv[1]!="":
            #print(sys.argv[1])
            ck = is_folder_or_file(sys.argv[1])
            if ck=='FILE':
                input("b1_install_path.ini 未生成，按[Enter] 結束...")
            elif ck == 'FOLDER':
                #print(sys.argv[1])
                with open("b1_install_path.ini","w+",encoding="utf-8") as f:
                    f.writelines(f"{sys.argv[1]}\n")
                input("b1_install_path.ini 已生成，按[Enter] 結束...")
    except:
        pass
