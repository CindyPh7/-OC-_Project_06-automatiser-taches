#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
print("Content-Type: text/plain\n")
oldDeviceNum = form['oldDeviceNumber'].value
oldMACAddr = form['oldMACAddress'].value
oldNetSocket = form['oldNetworkSocket'].value
oldIPAddr = form['oldIPAddress'].value
oldSwitchPort = form['oldSwitchPort'].value

newNetSocket = form['newNetworkSocket'].value
newIPAddr = form['newIPAddress'].value
newSwitchPort = form['newSwitchPort'].value


scopeID = "10.50.2.20"
run_powershell = 'powershell -command ';
powershell_cmd_rm_DHCP = 'Remove-DhcpServerv4Reservation -ComputerName "SERV-DHCP" -IPAddress ' + oldIPAddr;
powershell_cmd_add_DHCP = 'Add-DhcpServerv4Reservation -Name ' + oldDeviceNum + ' -ScopeID ' + scopeID + ' -ClientId ' + oldMACAddr + ' -Description ' + oldDeviceNum;
print(run_powershell + powershell_cmd_rm_DHCP + "\n" + run_powershell + powershell_cmd_add_DHCP)




def change_DHCP_Config(oldIPAddr,oldMACAddr,oldDeviceNum,newIPAddr):
	scopeID = "10.50.2.20"
	host = "10.50.2.10"
	port = 22
	username = "Administrateur"
	password = "Admin777"
	run_powershell = "powershell -command "
	powershell_cmd_rm_DHCP = 'Remove-DhcpServerv4Reservation -ComputerName "SERV-DHCP" -IPAddress ' + oldIPAddr
	powershell_cmd_add_DHCP = 'Add-DhcpServerv4Reservation -Name ' + oldDeviceNum + ' -ScopeID ' + scopeID + '-ClientId ' + oldMACAddr + '-Description ' + oldDeviceNum  
	#ssh = paramiko.SSHClient()
	#ssh.connect(host, port, username, password)
	#stdin, stout, stderr = ssh.exec_command(run_powershell + powershell_cmd_rm_DHCP + "\n" + powershell_cmd_add_DHCP + "\n" + "exit" 
	return "OK"

