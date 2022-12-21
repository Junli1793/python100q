import optparse

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