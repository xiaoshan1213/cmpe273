import psutil
import socket
import sys
from thread import *
import operator
import os

class TcpCheckTool:
    def check(self):
        # p = psutil.Process(os.getpid())
        # nametuple = p.connections(kind = 'tcp')
        nametuple = psutil.net_connections(kind = 'tcp')
        # print type(nametuple)
        # print nametuple
        l = []
        dic = {}
        for t in nametuple:
            # print type(t)
            t_sec = ()
            if t[4] != ():
                # print t
                t_sec = (t[6], t[3][0]+"@"+str(t[3][1]), t[4][0]+"@"+str(t[4][1]), t[5])
                l.append(t_sec)
                if dic.has_key(t[6]):
                    dic[t[6]] = dic.get(t[6])+1
                else:
                    dic[t[6]] = 1
                #print t[3], t[4], t[5], t[6]
        sort_dic = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
        print sort_dic
        for item_dic in sort_dic:
            for item_l in l:
                if item_l[0] == item_dic[0]:
                    print '\"'+str(item_l[0])+'\"'+item_l[1]+'\"'+item_l[2]+'\"'+item_l[3]



