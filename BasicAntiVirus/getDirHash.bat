@echo off
Rem Getting all files in 'Downloads' folder and getting their hash values for python scrypt 

Rem deleting and re-creating result.txt & result.html
del result.txt
break > result.txt
del result.html
break > result.html

Rem Iterates all files in dir
dir %userprofile%\Downloads /b > dirchk.txt

Rem adding path to 'dirNhash.txt'
echo %userprofile%\Downloads > dirNhash.txt

Rem Create array using 'dirchk.txt' and to get hash
setlocal EnableDelayedExpansion
set i=1
for /F %%a in (dirchk.txt) do (
   set /A i+=1
   set array[!i!]=%%a
)
set n=%i%
for /L %%i in (1,1,%n%) do Certutil -hashfile "%userprofile%\Downloads\!array[%%i]!" SHA256 >> dirNhash.txt

exit /B