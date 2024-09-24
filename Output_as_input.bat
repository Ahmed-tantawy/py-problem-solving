@echo off
:: Capture the hostname value into a variable
for /f %%i in ('hostname') do set HOSTNAME=%%i

:: Display the value of the hostname
echo The hostname is: %HOSTNAME%

:: Use the value of the hostname as a parameter (example usage)
call another_script.bat %HOSTNAME%

:: Or pass it to any other command or tool
