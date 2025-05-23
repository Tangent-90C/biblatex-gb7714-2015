#!/usr/bin/env python3
#_∗_coding: utf-8 _∗_

import os
import shutil
import pathlib
import re
import subprocess


def compileall(task='all'): #'all','compare'
    print(os.linesep)#这些都是字符串
    print(os.sep)
    print(os.pathsep)
    print(os.curdir)
    print(os.pardir)
    print(os.getcwd())
    print(os.listdir(path='.'))

    if task=='all':
        pwd=os.getcwd()
        filesneedcopy=['gb7714-CCNU.bbx','gb7714-CCNU.cbx','gb7714-NWAFU.bbx','gb7714-NWAFU.cbx','gb7714-SEU.bbx','gb7714-SEU.cbx',
        'chinese-erj.bbx','chinese-erj.cbx','chinese-css.bbx','chinese-css.cbx','gb7714-CCNUay.bbx','gb7714-CCNUay.cbx',
        'chinese-jmw.bbx','chinese-jmw.cbx','chinese-cajhss.bbx','chinese-cajhss.cbx','chinese-cajhssay.bbx','chinese-cajhssay.cbx',
        'example.bib', 'gb7714-1987.bbx', 'gb7714-1987.cbx', 
        'gb7714-1987ay.bbx', 'gb7714-1987ay.cbx', 'gb7714-2005.bbx', 'gb7714-2005.cbx', 'gb7714-2005ay.bbx',
        'gb7714-2005ay.cbx', 'gb7714-2015-gbk.def', 'gb7714-2015.bbx', 'gb7714-2015.cbx', 'gb7714-2015ay.bbx',
        'gb7714-2015ay.cbx', 'gb7714-2015ms.bbx', 'gb7714-2015ms.cbx', 'gb7714-2015mx.bbx', 'gb7714-2015mx.cbx']


        filelatexext=[".aux", ".bbl", ".blg", ".log", ".out", ".toc", ".bcf", 
        ".xml", ".synctex", ".nlo", ".nls", ".bak", ".ind", ".idx", 
        ".ilg", ".lof", ".lot", ".ent-x", ".tmp", ".ltx", ".los", 
        ".lol", ".loc", ".listing", ".gz", ".userbak", ".nav", ".snm", ".vrb",
        ".fls", ".xdv", ".fdb_latexmk"]

        
        #复制相关文件
        dirlst=os.listdir()
        subdirlst=[]
        for elem in dirlst:
            #print('elem=',elem)
            if os.path.isdir(elem) and elem != ".git" and elem != "tool":
                subdir=pwd+os.sep+elem
                subdirlst.append(subdir)
                for file in filesneedcopy:
                    shutil.copyfile(pwd+os.sep+file,subdir+os.sep+file)
                    print(subdir+os.sep+file+' ... copied')
        

        #进入相关文件夹进行编译
        for dirname in ["egphoto","egfigure"]: #
            subdir=pwd+os.sep+dirname
            os.chdir(subdir)
            pwd=os.getcwd()
            print('pwd=',pwd)
            print(os.listdir())


            #--------编译latex---------
            fileuniset=["test*.tex","cls*.tex","opt*.tex","code*.tex","eg*.tex","tgb*.tex","thesis*.tex","gbt*.tex"]

            for fileuni in fileuniset:
                pf1=pathlib.Path('.').glob(fileuni)
                pf=[str(x) for x in pf1]
                print('pf=',pf)
                if pf:
                    for file in pf:
                        print('---------compile new file:---------')
                        print('file=',file)
                        print('file=',os.path.splitext(file))
                        jobname=os.path.splitext(file)[0]

                        '''
                        if dirname=="egphoto" and jobname not in [
                            'opt-gbalign-right',
                            'opt-gbalign-left',
                            'opt-gbalign-center',
                            'opt-gbalign-gb',
                            'opt-gbpub-false',
                            'opt-gbpub-true',
                            'opt-gbnoauthor-true',
                            'opt-gbnoauthor-false',
                            'opt-gbbiblabela',
                            'opt-gbbiblabelb',
                            'opt-gbbiblabelc',
                            'opt-gbbiblabeld',
                            'opt-gbbiblabele',
                            'opt-gbbiblabelf',
                            'opt-gbnamefmt-a',
                            'opt-gbnamefmt-b',
                            'opt-gbnamefmt-c',
                            'opt-gbnamefmt-d',
                            'opt-gbnamefmt-e',
                            'opt-gbnamefmt-f',
                            'opt-gbtype-true',
                            'opt-gbtype-false',
                            'opt-gbmedium-true',
                            'opt-gbmedium-false',
                            'opt-gbfieldtype-true',
                            'opt-gbfieldtype-false',
                            'opt-gbpunctin-true',
                            'opt-gbpunctin-false',
                            'opt-gbtitlelink-true',
                            'opt-gbtitlelink-false',
                            'opt-gblocal-gb',
                            'opt-gblocal-chinese',
                            'opt-gblocal-english',
                            'opt-mergedate-a',
                            'opt-mergedate-b',
                            'opt-mergedate-c',
                            'opt-mergedate-d',
                            'opt-gblanorder-chineseahead',
                            'opt-gblanorder-englishahead',
                            'opt-gblanorder-udf',
                            'opt-citexref-true',
                            'opt-citexref-false',
                            'opt-gbannote-true',
                            'opt-gbannote-false']:
                            continue
                        '''
                        
                        if dirname=="egfigure" and jobname not in [
                            'egmwe',
                            'egciteaytab',
                            'egcontentfmtc',
                            'egparfmt',
                            'egcontentfmt',
                            'egcontentfmtb',
                            'egmsinabiblio',
                            'egmsindfrefsec',
                            'egmultilan',
                            'egdoublelan',
                            'egdoublelanb',
                            'egfootstyle']:
                            continue

                        #删除辅助文件
                        for fileext in filelatexext:
                            fileaux=pwd+os.sep+jobname+fileext
                            if os.path.exists(fileaux):
                                os.remove(fileaux)
                        #latex编译
                        latexcmd="xelatex"
                        subprocess.run([latexcmd,"-no-pdf",file])
                        subprocess.run(["biber",jobname])
                        subprocess.run([latexcmd,file])

            #--------编译latex结束---------
            os.chdir(os.pardir)
            pwd=os.getcwd()
            print('pwd=',pwd)

        #主目录文档编译
        jobname="biblatex-gb7714-2015"
        subprocess.run(["xelatex","-no-pdf",jobname])
        subprocess.run(["biber",jobname])
        subprocess.run(["xelatex","--synctex=-1",jobname])
        

        #删除相关文件
        dirlst=os.listdir()
        subdirlst=[]
        for elem in dirlst:
            #print('elem=',elem)
            if os.path.isdir(elem):
                subdir=pwd+os.sep+elem
                os.chdir(subdir)
                pwd=os.getcwd()
                print('pwd=',pwd)

                if elem=="tool":
                    fileextadd=[".bbx",".cbx",".def"]
                else:
                    fileextadd=[".bbx",".cbx",".def",".bib"]

                for fileext in filelatexext+fileextadd:
                    pf1=pathlib.Path('.').glob("*"+fileext)
                    pf=[str(x) for x in pf1]
                    print('pf=',pf)
                    if pf:
                        for file in pf:
                            fileaux=pwd+os.sep+file
                            os.remove(fileaux)
                            print(fileaux+" ... removed")
                
                os.chdir(os.pardir)
                pwd=os.getcwd()
                print('pwd=',pwd)
        
        print("compile all ended!")

    return None


if __name__ == '__main__':
    compileall()
    #compileall('all')
    #compileall('compare')