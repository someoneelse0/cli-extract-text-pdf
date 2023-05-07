#!/usr/bin/python3
#-*- coding:utf8 -*-
import PyPDF2 as pdf

def f0(o,f):
	p=pdf.PdfReader(f+".pdf")
	oo=open(o,"w")
	for i in p.pages:
		oo.write(i.extract_text())

f=input("Introduce the pdf file name to read (without extension): ")
o=input("Introduce the new name of file to write: ")
f0(o,f)
