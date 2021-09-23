import paramiko
from getpass import getpass

host = "10.10.0.4"
port = 22
username = (input("Enter Username: "))
password = getpass("Enter password: ")
command = "show config"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)

stdin, stdout, stderr, = ssh.exec_command(command)
lines = stdout.readlines()

resp = " ".join(lines)

print(f"{resp}")

ssh.close()

