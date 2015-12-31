#!/usr/bin/env python
#-*- coding: utf-8 -*-
import argparse

def get_argument():
    '''
    parse the cmd line,get the arguments 
    '''
    parser = argparse.ArgumentParser(description='Mongodb scanner')
    parser.add_argument('-u','--target',help='scan target ip,for example: 192.168.1.1 or 192.168.1.0/24')
    parser.add_argument('-p','--port',default='27017',help='mongodb server port,for example:27017,28017,default is 27017')
    parser.add_argument('-t','--threads',default=1,type=int,help='thread numbers,default is 1')
    parser.add_argument('-o','--timeout',default=5,type=int,help='timeout second,default is 5')
    parser.add_argument('-f','--file',help='read target from a logfile of scanned log file,the target is like ip:port,xxx(targetinfo)')
    parser.add_argument('-l','--logfile',help='output the result to logfile,default logfile name is by datetime')
    parser.add_argument('--nmap',default=False,action='store_true',help='use libnamp do scan (install nmap first,and maybe the ctrl+c has problem)')

    args = parser.parse_args()
    if args.target == None and args.file == None:
        parser.print_help()
        print "You must set the target(-u) or file (-f) to run !"
        #exit(0)
    return args

def main():
    args = get_argument()
    print args

if __name__ == '__main__':
    main()
