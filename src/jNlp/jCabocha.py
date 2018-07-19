#! /usr/bin/env python                                                        
# -*- coding: utf-8 -*-
import sys, subprocess, os
from subprocess import call
from tempfile import NamedTemporaryFile

def formdamage(sent):
    rectify = []
    for ch in sent:
        try: rectify.append(ch.encode('utf-8'))
        except: pass
    return ''.join(rectify)
        
def cabocha(sent):
    if os.path.exists('/home_lab_local/s1010205/tmp/'):
        temp = NamedTemporaryFile(delete=False, dir='/home_lab_local/s1010205/tmp/')
    else:
        temp = NamedTemporaryFile(delete=False)
    try: sent = sent.encode('utf-8')
    except: sent = formdamage(sent)
    temp.write(sent)
    temp.close()
    command = ['cabocha', '-f', '3']
    process = subprocess.Popen(command, stdin=open(temp.name,'r'), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    os.unlink(temp.name)
    return unicode(output, 'utf-8')

def main():
    pass

if __name__ == '__main__':
    input_sentence = u'ＰＲ情報等(本質をズバリ！本当に必要なことを的確に指摘する濱口善幸のタロット占い～１月28日（月）より「幸福の切札」をYahoo!公式サイトにて配信開始～)'
    print cabocha(input_sentence).encode('utf-8')


    
    
    
