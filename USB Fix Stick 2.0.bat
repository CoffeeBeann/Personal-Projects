:start
@echo off
color 03
title USB Fix Stick 2.0
cls
echo ----------#######--------------#######---------------#################--------------#############----------------------
echo ----------#######--------------#######------------######################------------##############---------------------
echo ----------#######--------------#######-----------#######--------------####----------####--------####-------------------
echo ----------#######--------------#######---------######-----------------#####---------####--------####-------------------
echo ----------#######--------------#######---------######-------------------------------####--------####-------------------
echo ----------#######--------------#######----------######------------------------------####-------####--------------------
echo ----------#######--------------#######------------######################------------#############----------------------
echo ----------#######--------------#######---------------#####################----------###############--------------------
echo -----------#######------------#######-------------------------------########--------###--------######------------------
echo ------------#######----------#######---------------------------------#######--------###----------####------------------
echo -------------######----------######---------------------------------######----------###---------#####------------------
echo --------------####################--------------#####-------------#####-------------###--------####--------------------
echo ----------------###############-----------------#####################---------------#############----------------------
echo -----------------#############----------------------##############------------------###########------------------------
echo -----------------------------------------------------------------------------------------------------------------------
echo ------------------------------------#############---------------------------------###################------------------
echo --------------------------------#####################---------------------------########-------########----------------
echo -------------------------------#####------------######--------------------------######--------##-######----------------
echo -------------------------------####--------------######-------------------------######-------##--######----------------
echo ------------------------------------------------#####---------------------------######------##---######----------------
echo ---------------------------------------------######-----------------------------######-----##----######----------------
echo -------------------------------------------######-------------------------------######----##-----######----------------
echo -------------------------------################---------------------------------######---##------######----------------
echo -----------------------------#########---------------------------###------------#######-##-----########----------------
echo ----------------------------###########################----------###--------------###################------------------
pause
:TE
echo ------------------------------------------------------------------------------------------------------
echo Welcome To The Usb Fix Stick 2.0.
echo Enter Digits Acording To The Chart Below To Choose Desired Scan.
echo ------------------------------------------------------------------------------------------------------
echo Enter 1 = System Scan
echo Enter 2 = File Scan
echo Enter 3 = Details
echo Enter 4 = Exit Program
echo ------------------------------------------------------------------------------------------------------
echo Note: If You Want More Detail Into What These Scans Do Enter 3.
echo ------------------------------------------------------------------------------------------------------
set /p input=
if %input% ==1 goto :a
if %input% ==2 goto :b
if %input% ==3 goto :c
if %input% ==4 goto :d

:a
cls
cd\
cd program files
cd windows defender
mpcmdrun -scan -1
cls
echo BOT: Scan Complete. All Malware Has Been Terminated.
pause
goto :TEM

:b
cd\
attrib -s -h *-* /s
cls
echo BOT: Scan Complete. All Malware Has Been Terminated.
pause
goto :TEM

:c
cls
echo BOT: SYSTEM SCAN. This scan checks all aspects of the computer in it's critical systems such as "system 32".
echo This scan is only for checking critical systems that the computer needs to be fully functional. This does not include;
echo Any Malware that doesn't affect critical system, but may damage other aspects of the computer. 
pause
cls
echo BOT: FILE SCAN. This scan is responsibe for checking all other aspects of the computer not regarding 
echo critical systems. This scan digs deep in program files to find imbedded malware within. Program files
echo are often the main suspect if malware is imbedded in a file on the computer. When malware is detected
echo the system locates it's PID number and uses it to taskill the program.
pause
cls
goto :TEM

:d
cls
echo BOT: Are You Sure You Would Like to exit This Program. (yes,no)
set /p yes=
if %yes% == no goto :TEM
if %yes% == yes
cls
exit

:TEM
cls
goto :TE