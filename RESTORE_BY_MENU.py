import sys,os,shutil

if __name__ == '__main__':
    with open("b1_install_path.ini","r",encoding="utf-8") as f:
        DIST_FOLDER_PATH=f.read()
    DIST_FOLDER_PATH=DIST_FOLDER_PATH.replace("\n","").strip()+"\\"
    DIST_SAV_NAME="ArchiveSaveFile.10.sav"
    try:
        print("STORED SAVE FILES LIST:\n"+"-"*60)
        # 列出 SAVs 裡面的所有檔案
        SOURCE_DIR="SAVs\\"
        ls = [ i.replace(".sav","") for i in os.listdir(SOURCE_DIR) if i.endswith('.sav') ]
        for count, direction in enumerate(ls, start=1):
            print(f"NO.{count} -> {direction}")
        #print()
        sel = input("-"*60+"\nINPUT Num And Press Enter...NO.")
        try:
            sel = int(sel.strip())
        except:
            sel = -1
        if sel>0 and sel<=len(ls):
            tmp = DIST_FOLDER_PATH + DIST_SAV_NAME
            full_file_name= SOURCE_DIR+ls[sel-1]+".sav"
            # 檢查文件是否存在
            if os.path.exists(tmp):
                os.remove(tmp) # 刪除文件
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, tmp)
                print(f'SAV檔案 {ls[sel-1]} 已複製到 {DIST_FOLDER_PATH}...')
        else:
            print("-"*60+"\nSAV還原失敗! 你輸入的NO編號超出列表範圍，請重新執行並輸入正確NO編號...")
    except:
        pass
    input("按Enter結束本程式")
