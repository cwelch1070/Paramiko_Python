import Paramiko
from getpass import getpass
import time

host = "test"
username = (input("Enter Username: ") or "user1")
password = getpass("Enter password: ")

session = Paramiko.SSHClient()

session.set_missing_host_key_policy(Paramiko.AutoAddPolicy())

session.connect(hostname = host,
                username = username,
                password = password)

stdin, stdout, stderr, = session.exec.command('hostname')
time.sleep(.5)
print(f"Host name is {stdout.read().decode()}")

session.close()

