#!/usr/bin/python3
__author__ = 'kaidyan'

import sys,os,time
import optparse
import commands
import pexpect
import utils


def copy_datacheck_scripts(host_ip, host_pw, autodir, folder):
    print('Copy datacheck scripts to server: %s ...'%(host_ip))
    c = utils.connect_to_host(host_ip, host_pw)
    fout = open ("logs/copy_datacheck_scripts_%s.log"%(host_ip), "wb")
    c.logfile = fout
    c.sendline('rm -rf %s/%s'%(autodir, folder))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('mkdir -p %s'%(autodir))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('cd %s'%(autodir))
    c.expect([pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)

    cwd = os.getcwd()
    utils.scp_to_host(host_ip, host_pw, autodir, '%s/end2end/%s'%(cwd, folder))

    c = utils.connect_to_host(host_ip, host_pw)
    fout = open ("logs/copy_datacheck_scripts_%s.log"%(host_ip), "ab")
    c.logfile = fout
    c.sendline('cd %s/%s'%(autodir, folder))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('ls -l')
    c.expect([pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)


def copy_mse_replay_handler(host_ip, host_pw, autodir, folder, config1, config2):
    print('Copy mse replay handler code to server: %s ...'%(host_ip))
    c = utils.connect_to_host(host_ip, host_pw)
    fout = open ("logs/copy_mse_replay_handler_%s.log"%(host_ip), "wb")
    c.logfile = fout
    c.sendline('rm -rf %s/%s'%(autodir, folder))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('mkdir -p %s'%(autodir))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('cd %s'%(autodir))
    c.expect([pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)

    cwd = os.getcwd()
    utils.scp_to_host(host_ip, host_pw, autodir, '%s/tools/%s'%(cwd, folder))

    c = utils.connect_to_host(host_ip, host_pw)
    fout = open ("logs/copy_mse_replay_handler_%s.log"%(host_ip), "ab")
    c.logfile = fout
    c.sendline('cd %s/%s'%(autodir, folder))
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('ls -l')
    c.expect([pexpect.TIMEOUT, '#'])
    c.sendline('./rewrite_properties.sh %s %s'%(config1, config2))
    time.sleep(60)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])

    fout.close()
    c.close(force=True)


def rewrite_pacp(host_ip, host_pw, script_path, pcap, dest_ip):
    print('Start to rewrite pcap for %s ...'%dest_ip)
    #get dest mac
    (status, output) = commands.getstatusoutput('grep -P "..:..:..:..:..:.." logs/get_mac_%s.log | sed "s/^M//g"'%(dest_ip))
    print(status, output)

    fout = open("logs/rewrite_pacp_%s.log"%(dest_ip), "wb")
    c = utils.connect_to_host(host_ip, host_pw, time_out=600)
    c.logfile = fout
    c.sendline('cd %s'%script_path)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('ls -l')
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('rm -rf ./%s_%s'%(dest_ip,pcap))
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('./rewrite_pcap.sh ../pcap/%s ./%s_%s %s %s %s'%(pcap,dest_ip,pcap,dest_ip,host_ip,output))
    time.sleep(60)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)
    print('Finish to rewrite pcap for %s'%(dest_ip))


def replay_pacp(host_ip, host_pw, script_path, pcap, dest_ip):
    print('Start to send traffic to %s ...'%dest_ip)
    fout = open("logs/replay_pacp_%s.log"%(dest_ip), "wb")
    c = utils.connect_to_host(host_ip, host_pw, time_out=600)
    c.logfile = fout
    c.sendline('cd %s'%script_path)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('./send_traps.sh ./%s_%s'%(dest_ip,pcap))
    time.sleep(600)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)
    print('Finish to send traffic to %s'%(dest_ip))


def run_queries(host_ip, host_pw, script_path, ops):
    print('Start to run query on %s ...'%host_ip)
    fout = open ("logs/run_query_%s.log"%(host_ip), "wb")
    c = utils.connect_to_host(host_ip, host_pw, time_out=600)
    c.logfile = fout
    c.sendline('cd %s'%script_path)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    c.sendline('./sanity_check.sh %s'%(ops))
    time.sleep(180)
    c.expect([pexpect.EOF, pexpect.TIMEOUT, '#'])
    fout.close()
    c.close(force=True)

    #sftp the result
    utils.sftp_file(host_ip, host_pw, '%s/sanity-check-*.log'%(script_path))
    os.system("mv sanity-check-*.log end2end/actual_output/")

    print('Finish to run query on %s'%(host_ip))


def result_compare(host_ip, host_pw, pkg_path):
    print('Start to compare output files ...')
    (status, output) = commands.getstatusoutput("diff end2end/actual_output/sanity-check-*.log end2end/expect_output/sanity-check-*.log > logs/data_check.log")
    print(status, output)
    print('Finished compare output files')
    if status != 0:
        sys.exit(2)


def ReadOptions():
    parser=optparse.OptionParser(usage="usage: %prog [options]", version="1.0",conflict_handler="resolve")
    parser.add_option('-n','--nimbus',action="store_true",dest="mode",default=True,help="install on nimbus(4 vms)")
    parser.add_option('-l','--local',action="store_false",dest="mode",default=True,help="install on local(2 vms)")
    parser.add_option('--config1',action="store",dest="config1",default='10.79.57.21',help="IP of config1")
    parser.add_option('--config2',action="store",dest="config2",default='10.79.57.80',help="IP of config2")
    parser.add_option('--config3',action="store",dest="config3",default='10.79.57.60',help="IP of config3")
    parser.add_option('--config4',action="store",dest="config4",default='10.79.57.65',help="IP of config4")
    parser.add_option('--password1',action="store",dest="password1",default='cisco123',help="Password of root on config1")
    parser.add_option('--password2',action="store",dest="password2",default='cisco123',help="Password of root on config2")
    parser.add_option('--password3',action="store",dest="password3",default='cisco123',help="Password of root on config3")
    parser.add_option('--password4',action="store",dest="password4",default='cisco123',help="Password of root on config4")
    parser.add_option('--tcpreplay',action="store",dest="traffic",default='10.79.57.56',help="IP of tcpreplay server")
    parser.add_option('--tcpreplaypassword',action="store",dest="trafficpassword",default='cisco123',help="Password of root on tcpreplay server")

    options,args=parser.parse_args()
    return (options,args)


def data_check(options):

    mode = options.mode
    pcap_path = '/home/cae_e2e/pcap'
    script_path = '/home/cae_e2e'
    config1 = options.config1
    config2 = options.config2
    config3 = options.config3
    config4 = options.config4
    traffic = options.traffic
    config1_pw = options.password1
    config2_pw = options.password2
    config3_pw = options.password3
    config4_pw = options.password4
    traffic_pw = options.trafficpassword

    try :

        if mode :
            #prepare the env
            copy_datacheck_scripts(config3, config3_pw, script_path, 'datacheck')
            copy_datacheck_scripts(traffic, traffic_pw, script_path, 'tcpreplay')
            copy_mse_replay_handler(config1, config1_pw, script_path, 'MSE_REPLAY', config1, config2)

            #replay pcap
            rewrite_pacp(traffic, traffic_pw, '%s/tcpreplay'%(script_path), 'javits_5hour_all.pcap', config1)
            replay_pacp(traffic, traffic_pw, '%s/tcpreplay'%(script_path), 'javits_5hour_all.pcap', config1)

            #run query
            time.sleep(60)
            run_queries(config3, config3_pw, '%s/datacheck'%(script_path), 'queries.current.sql -a')

            #result check
            result_compare(config1, config1_pw, script_path)

        else :
            #prepare the env
            copy_datacheck_scripts(config2, config2_pw, script_path, 'datacheck')
            copy_datacheck_scripts(traffic, traffic_pw, script_path, 'tcpreplay')
            copy_mse_replay_handler(config1, config1_pw, script_path, 'MSE_REPLAY', config1, config1)

            #replay pcap
            utils.get_mac(config1,config1_pw)
            rewrite_pacp(traffic, traffic_pw, '%s/tcpreplay'%(script_path), 'javits_5hour_all.pcap', config1)
            replay_pacp(traffic, traffic_pw, '%s/tcpreplay'%(script_path), 'javits_5hour_all.pcap', config1)

            '''
            #run query
            time.sleep(60)
            run_queries(config2, config2_pw, '%s/datacheck'%(script_path), 'queries.current.sql -a')

            #result check
            result_compare(config1, config1_pw, script_path)
            '''

    except Exception as e :
        print(sys.stderr, e)
        raise

if __name__ == '__main__':
    (options,args)=ReadOptions()
    sys.exit(data_check(options))

