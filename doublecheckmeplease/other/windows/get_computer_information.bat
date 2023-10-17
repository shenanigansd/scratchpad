rem This is a script to get the computer name, the user name, and the product key

set /p ip="IP (Ex: 10.0.0): "

FOR /L %%i IN (1,1,254) DO (ping -n 1 %ip%.%%i && call :test %%i) || echo Failed to ping %ip%.%%i >> failed.csv
goto END

:test
wmic.exe /node:%ip%.%1 computersystem get name,username >> computers.csv
wmic.exe /node:%ip%.%1 os get caption >> computers.csv
wmic.exe /node:%ip%.%1 path softwarelicensingservice get OA3xOriginalProductKey >> computers.csv

:END
