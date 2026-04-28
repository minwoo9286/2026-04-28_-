@echo off
cd /d "C:\Users\minwo\minwoo\VibeCoding\Study-04"

set DATESTAMP=%date:~0,4%-%date:~5,2%-%date:~8,2%

git add .
git commit -m "수업 내용 업데이트 - %DATESTAMP%"
git push origin main

echo.
echo [완료] GitHub 업로드 성공: %DATESTAMP%
timeout /t 3
