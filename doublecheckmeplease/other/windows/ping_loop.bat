rem This is a script to ping every address in a subnet

set /p ip="IP (Ex: 10.0.0): "

FOR /L %%i IN (1,1,254) DO (ping -n 1 %ip%.%%i) || echo Failed to ping %ip%.%%i >> failed.csv
goto END
