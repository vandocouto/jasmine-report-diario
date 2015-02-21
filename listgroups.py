#!/usr/bin/python
#-=- encoding: latin-1 -=-

import os, commands



def listgroups(group):
    group=group
    user='admin'
    password='pass'
    host='tgl.com'
    comando=(commands.getoutput("ldapsearch -x -b 'ou=%s,ou=USER,ou=MATRIZ,dc=tgl,dc=com' \
    -D 'cn=%s,cn=Users,dc=tgl,dc=com' -w '%s' -h %s | \
    grep sAMAccountName | egrep -v TI | egrep -v relacionamento | awk '{print $2}' | sort" %(group,user,password,host)))
    
    comando = comando.split()
    return comando

