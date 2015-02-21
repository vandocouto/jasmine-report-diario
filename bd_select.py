#!/usr/bin/python
#-=- encoding: latin-1 -=-

# INSTALE O MODULO python-mysqldb
import MySQLdb
import re
from acesso_bd import acesso_bd
from listgroups import listgroups
import datetime as DT


# Recebendo as variaveis de acesso no banco
host        =   acesso_bd()[0]
user        =   acesso_bd()[1]
password    =   acesso_bd()[2]
bd_name     =   acesso_bd()[3]
today       =   DT.date.today()
today       =   today - DT.timedelta(days=1)


# função select 
def bd_select(group):
    group=group
    select = '<html><style>\
    .border {font-family: Arial, Sans-Serif; font-size:12px;}\
    .copy, .copy a {width: 660px; margin:0 auto; color: #DD8888;}\
    .formresult {background-color:#FFFF99;display:block;padding:10px;}\
    .seletor {font-family: Arial, Sans-Serif; font-size:6px;}</style>'

    select +='<table class="border" align="center" valign="top" width="1024">'
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    lista1=[]
    lista2=[]
    cont=0
    total=0
    date=''
    
    for a in listgroups(group):
        sql = ("select user,title,date,copies,pages from jobs_log where user='%s' and date>='%s 00:00:00' and date<='%s 23:59:59'" \
        %(a,today,today))
        cursor.execute(sql)
        resultado = cursor.fetchone()

        if resultado != None:
            try:
                while (resultado):
                    lista1.append(resultado)
                    resultado = cursor.fetchone()
            
                select+='<tr>\
                <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Usu&aacute;rio</font></td>\
                <td align="center" width="300" bgcolor="#EEC900"><font size="2px">T&iacute;tulo</font></td>\
                <td align="center" width="180" bgcolor="#EEC900"><font size="2px">Data</font></td>\
                <td align="center" width="50" bgcolor="#EEC900"><font size="2px">C&oacute;pias</font></td>\
                <td align="center" width="50" bgcolor="#EEC900"><font size="2px">P&aacute;ginas</font></td>\
                </tr>'
            
                while cont < len(lista1):
                    if cont % 2 == 0:
                        select+='<tr>\
                        <td align="center" bgcolor="#FFFAFA">%s</td>\
                        <td align="center" bgcolor="#FFFAFA">%s</td>\
                        <td align="center" bgcolor="#FFFAFA">%s</td>\
                        <td align="center" bgcolor="#FFFAFA">%s</td>\
                        <td align="center" bgcolor="#FFFAFA">%s</td>\
                        </tr>' \
                        %(str(lista1[cont][0]),str(lista1[cont][1]),str(lista1[cont][2]),str(lista1[cont][3]),str(lista1[cont][4]))
                    else:
                        select+='<tr>\
                        <td align="center" bgcolor="#EEE9E9">%s</td>\
                        <td align="center" bgcolor="#EEE9E9">%s</td>\
                        <td align="center" bgcolor="#EEE9E9">%s</td>\
                        <td align="center" bgcolor="#EEE9E9">%s</td>\
                        <td align="center" bgcolor="#EEE9E9">%s</td>\
                        </tr>' \
                        %(str(lista1[cont][0]),str(lista1[cont][1]),str(lista1[cont][2]),str(lista1[cont][3]),str(lista1[cont][4]))
                    cont +=1
        
                sql = ("select user,sum(pages) from jobs_log where user='%s' and date>='%s 00:00:00' and date<='%s 23:59:59'" \
                %(a,today,today))
                cursor.execute(sql)
                resultado = cursor.fetchone()
                lista2.append(resultado[1])
                if lista2[-1] != None:
                    select+='<tr>\
                    <td bgcolor="#FFFAFA"></td>\
                    <td bgcolor="#FFFAFA"></td>\
                    <td bgcolor="#FFFAFA"></td>\
                    <td align="center" bgcolor="#D3D3D3"><b>Total</b></td>\
                    <td align="center" bgcolor="#D3D3D3"><b>%s</b></td>\
                    </tr>' %(str(resultado[1]))
                    total+=int(resultado[1])
            
            except:
                continue
            
    select+='</table>'
    select+='<table class="border" align="center" valign="top" width="1024">'
    select+='<tr>\
    <td align="center" bgcolor="#FFFFFF"><b><font size="3px">Total de folhas impressas %s</font></b></td>\
    </tr>\
    </table>'\
    %total
    select+="</table>"
    cursor.close()
    if total != 0:
        return select
    else:
        return 0

#print bd_select('RH')


 
