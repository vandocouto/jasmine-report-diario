#!/usr/bin/python
#-=- encoding: latin-1 -=-

import smtplib
from email.MIMEText import MIMEText
from bd_select import bd_select


def envia_email(dep,relt,email1):
    SMTP    =   "smtp.dominio.com.br"
    PORTA   =   "26"
    LOGIN   =   "sysadmin@dominio.com.br"
    EMAIL   =   "sysadmin@dominio.com.br"
    PASS    =   "pass"
    SMTPSERVER = smtplib.SMTP
    PORTA = str(PORTA)
    ASSUNTO="[RELT. DE IMPR. DIÁRIO] Departamento: %s" %dep
    MENSAGEM="%s" %(bd_select(relt))
    FROM=EMAIL
    TO1=email1
    serv=SMTPSERVER()
    serv.connect(SMTP,PORTA)
    serv.starttls()
    serv.login(LOGIN,PASS)
    msg1 = MIMEText(MENSAGEM.decode('utf-8'),'html','latin-1')
    msg1['Subject']=(ASSUNTO)
    msg1['From']=FROM
    msg1['To']=TO1
    msg1['Content-type']="text/html"
    serv.sendmail(FROM,TO1, msg1.as_string())
    serv.quit()



