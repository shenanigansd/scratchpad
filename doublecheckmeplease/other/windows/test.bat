@echo off

wmic.exe computersystem get name >> computers.txt
wmic.exe computersystem get username >> computers.txt
wmic.exe os get caption >> computers.txt
wmic.exe path softwarelicensingservice get OA3xOriginalProductKey >> computers.txt
