@echo off
setlocal enabledelayedexpansion

:: B1存檔資料夾路徑
set save_dir="L:\Games\Steam\steamapps\common\BlackMythWukong\b1\Saved\SaveGames\123456789"

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