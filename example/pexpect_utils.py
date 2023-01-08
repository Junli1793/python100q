#!/usr/bin/python3
__author__ = 'kaidyan'

import sys,os,time
import optparse
import commands
import pexpect


def connect_to_host(host_ip, host_pw, uname='root', time_out=180):
    print('Connect to server %s with %s ...'%(host_ip, uname))
    c = pexpect.spawn('ssh -l %s %s'%(uname, host_ip), timeout=time_out)
    i = c.expect([pexpect.TIMEOUT, 'yes', 'password: ', '#'])
    if i == 0: # Timeout
        print('ssh login time out')
    elif i == 1: # SSH does not have the public key. Just accept it.
        c.sendline ('yes')
        i = c.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            print('password input timeout')
        c.sendline(host_pw)
    elif i == 2:
        c.sendline(host_pw)
    elif i == 3:
        c.sendline('pwd')
    else :
        sys.exit(1)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    return c


def scp_to_host(host_ip, host_pw, dest_path, files):
    #cwd = os.getcwd()
    print('Start to scp file %s to server %s ...'%(files, host_ip))
    c = pexpect.spawn('scp -r %s root@%s:%s'%(files, host_ip, dest_path), timeout=600)
    #c = pexpect.spawn('scp -r %s/%s root@%s:%s'%(cwd, file, host_ip, dest_path), timeout=600)
    #c = pexpect.spawn('scp %s/%s root@%s:%s'%(folder, file, host_ip, dest_path), timeout=600)
    i = c.expect([pexpect.TIMEOUT, 'yes', 'password: ', ']#'])
    if i == 0: # Timeout
        print('scp login time out')
    elif i == 1: # SSH does not have the public key. Just accept it.
        c.sendline ('yes')
        i = c.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            print('password input timeout')
        c.sendline(host_pw)
    elif i == 2:
        c.sendline(host_pw)
    elif i == 3:
        c.sendline('ls -l')
    else:
        sys.exit(1)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, ']#'])
    c.close(force=True)
    print('Finish to scp files to server %s'%(host_ip))


def sftp_file(host_ip, host_pw, files, uname='root'):
    print('Start to sftp file %s from %s ...'%(files, host_ip))
    c = pexpect.spawn('sftp %s@%s'%(uname, host_ip), timeout=600)
    i = c.expect([pexpect.TIMEOUT, 'yes', 'password: ', 'sftp>'])
    if i == 0: # Timeout
        print('sftp login time out')
    elif i == 1: # SSH does not have the public key. Just accept it.
        c.sendline ('yes')
        i = c.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            print('password input timeout')
        c.sendline(host_pw)
    elif i == 2:
        c.sendline(host_pw)
    elif i == 3:
        c.sendline('pwd')
    else:
        sys.exit(1)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, 'sftp>'])
    c.sendline('get %s'%(files))
    c.expect([pexpect.TIMEOUT, 'sftp>'])
    c.sendline('!ls -l')
    c.expect([pexpect.TIMEOUT, 'sftp>'])
    c.sendline('bye')
    c.expect([pexpect.TIMEOUT, '$'])
    c.close(force=True)
    print('Finish to sftp files from server %s'%(host_ip))

def change_date(host_ip, host_pw, date):
    print('Start to change date on %s ...'%host_ip)
    fout = open ("logs/change_date_%s.log"%(host_ip), "wb")
    c = connect_to_host(host_ip, host_pw)
    c.logfile = fout
    c.sendline('date %s'%(date))
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('date')
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)
    print('Finish to change date on %s'%host_ip)

def get_mac(host_ip, host_pw, inet='eth0'):
    print('Try to get mac of %s ...'%host_ip)
    fout = open ("logs/get_mac_%s.log"%(host_ip), "wb")
    c = connect_to_host(host_ip, host_pw)
    c.logfile = fout
    c.sendline("ifconfig %s | grep -i HWaddr | awk '{print $5}'"%(inet))
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)
    print('Finish to change date on %s'%host_ip)
