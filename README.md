# 黑神話悟空-遊戲存檔-快速備份 (B1-SAVE.bat) 使用說明

-----

## 基本需求:
1. Windows作業系統
2. Steam版的黑神話悟空

-----

## 實作:
1. 在桌面按"右鍵"，點擊"新增 > 資料夾"，並命名為"B1-SAVE"。
2. 開啟Windows內建的 "記事本"。(可以按快捷鍵 "Win+R" 然後輸入 notepad 再按 "Enter")
3. 開啟記事本後，直接點左上的 "檔案(File)" > "另存新檔(Save as)"，在另存新檔的對話視窗中把路徑指到我們在步驟1新增在桌面的 B1-SAVE 資料夾，並把 "存檔類型(Save as type)" 設為 "所有檔案(All files)"，檔案名稱設為 "B1-SAVE.bat"，"編碼(Encoding)"要設為"ANSI"，最後按 "儲存(Save)"。
4. 在 "記事本-B1-SAVE.bat" 裡貼上下列文字:
```
@echo off
setlocal enabledelayedexpansion

:: B1存檔資料夾路徑
set save_dir="黑神話悟空存檔路徑"

:: 取得當前日期和時間
set t=%time:~0,8%
::set mt=%t: =0%
for /f "tokens=1,2,3,5,6,7 delims=/-:. " %%a in ('echo %date% %t: =0%') do (
set year=%%a
set month=%%b
set day=%%c
set hour=%%d
set minute=%%e
set second=%%f
)

:: 日期和時間為 yyyymmddHHmmss
set timestamp=%year%%month%%day%%hour%%minute%%second%

:: 建立新資料夾
set newfolder=%~dp0%timestamp%
mkdir "%newfolder%"

:: 複製文字檔到新資料夾
xcopy "%save_dir%\ArchiveSaveFile.*.sav" "%newfolder%"

echo 所有SAV檔已複製到 %newfolder%
pause
```
然後點左上的 "檔案(File)" > "存檔(Save)"，或按 "Ctrl+S"
5. 步驟4裡面只有一個地方需要修改("黑神話悟空存檔路徑")，所以我們先不要把記事本關掉，將它最小化，然後進到 Steam 裡面黑神話悟空的頁面，點右側的 "尺輪 > 管理 > 瀏覽本機檔案"，然後點進 "B1 > Saved > SaveGames > 一串數字"，進到這裡看到多個 .sav 的檔案就對了(這裡就是你玩黑神話的遊戲存檔位置)，我們點一下上面的路徑，將它反白然後按 "右鍵 > 複制"(或按 "Ctrl+C")。
6. 回到 "記事本-B1-SAVE.bat"， 將 "黑神話悟空存檔路徑" 這串文字刪掉並貼上我們剛才複制的路徑，修改後的內容應該會像這樣:
```
set save_dir="L:\Games\Steam\steamapps\common\BlackMythWukong\b1\Saved\SaveGames\12345678987654321"
```
最後別忘了: "檔案(File)" > "存檔(Save)"，或按 "Ctrl+S"。

-----

## 如何使用 B1-SAVE.bat
* 直接對它點兩下滑鼠左鍵，它就會自動將黑神話存檔(ArchiveSaveFile.*.sav)複制到 用當前的"年月日時分秒(yyyyMMddHHmmSS)"為名新建的資料夾裡。
* 請特別注意，在遊戲進行中勿執行 B1-SAVE.bat
* 可以執行 B1-SAVE.bat 的時機:
1. 未執行黑神話悟空。
2. 黑神話遊戲在執行中，畫面停在遊戲選單(未進行遊戲)
* 舉個例子，我現在玩到準備打某個BOSS之前的土地廟，點土地廟調息之後，按"ESC > 離開遊戲 > 返回遊戲選單"，確定畫面切到遊戲選單後，按一下"Win"鍵，開啟檔案總管進到 "B1-SAVE資料夾"，對 "B1-SAVE.bat"點兩下左鍵執行，就會看到SAVE複制成功的訊息，這樣就備份完成了，接著可以切回黑神話按繼續遊戲挑戰BOSS，結果打著打著我把藥水資源都耗光了BOSS也沒打過，這時可以把存檔備份還原回去，讓耗光的藥水重新變回來。
* 備份還原很簡單，就是先把遊戲結束，或回到遊戲選單，然後進到檔案總管把我們備份的(ArchiveSaveFile.*.sav)複制到 黑神話的遊戲存檔位置，然後重新進入遊戲你就會看到時光倒流了!
