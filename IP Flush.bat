title IP Flush
@echo off
color 03
cls
cd/

ipconfig /all
ipconfig /renew
ipconfig /release
ipconfig /flushdns

netsh wlan show networks mode = BSSID
netsh wlan show profiles name = "Coffey Grounds-5g" key = clear
netsh wlan connect name = "Coffey Grounds-5g"


