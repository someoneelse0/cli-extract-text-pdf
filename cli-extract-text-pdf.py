#!/usr/bin/python3

import PyPDF2 as ppdf

def f0(o,f):
    f=f+".pdf"
    ff=open(f,"rb")
    pp=ppdf.PdfFileReader(ff)
    i=pp.numPages
    oo=open(o,"w")
    for x in range(0,i):
        xd=pp.getPage(x)
        oo.write(xd.extractText())
    ff.close()
    oo.close()
    print("Writted")

f=input("Introduce the pdf file name to read (without extension): ")
o=input("Introduce the new name of file to write: ")
f0(o,f)
