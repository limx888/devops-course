#-*- coding: utf-8 -*-
#!/usr/bin/python 

import paramiko


def ssh_sample(ip, username, passwd, cmd):
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username,passwd,timeout=5)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    #stdin.write("Y")   #简单交互，输入 ‘Y’ 

    #屏幕输出
    print stdout.read(),
    ssh.close()
  except :
    print '%s\tError\n'%(ip)



if __name__=='__main__':
  cmd = 'ls'      #你要执行的命令列表
  username = ""  #用户名
  passwd = ""    #密码
  ip = '192.168.1.x'
  ssh_sample(ip,username,passwd,cmd)






