@echo off
setlocal enabledelayedexpansion

:: B1�s�ɸ�Ƨ����|
set save_dir="L:\Games\Steam\steamapps\common\BlackMythWukong\b1\Saved\SaveGames\123456789"

:: ���o��e����M�ɶ�
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

:: ����M�ɶ��� yyyymmddHHmmss
set timestamp=%year%%month%%day%%hour%%minute%%second%

:: �إ߷s��Ƨ�
set newfolder=%~dp0%timestamp%
mkdir "%newfolder%"

:: �ƻs��r�ɨ�s��Ƨ�
xcopy "%save_dir%\ArchiveSaveFile.*.sav" "%newfolder%"

echo �Ҧ�SAV�ɤw�ƻs�� %newfolder%
pause