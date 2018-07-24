#!/usr/bin/env python3
# deprec script used to process dada, creates a nu dadabase placing IMG dir into its own field split from 'title' field


import json
import sys

dada_dir="../dada/"
filen=dada_dir+"data.ole"
data=json.loads(open(filen,"r").read())
bcnt=0
cnt=1
lda=len(data)
while cnt<lda:
  art=list(data[cnt].keys())[0]
  for ea in data[cnt][art]:

    splDsc=ea["desc"].split(",back(")
    splTag=ea["tags"].split("back")
    if len(splDsc)>1: # or len(splTag)>1:
      print(ea["title"])
      bckImg=splDsc[1].split(",")
      print("  desc:",ea["desc"])
      print(splDsc)
      print("  imag:",bckImg[0])
      print("    imag desc:",bckImg[1][:-1])
      ea["desc"]=splDsc[0]
      """

      back={}
      back["date"]=ea["date"]
      back["location"]=ea["location"]
      back["dim"]=ea["dim"]
      back["image"]=bckImg[0]
      back["desc"]=bckImg[1][:-1]
      back["title"]=back["desc"]
      bcnt+=1
      print("    : ",bckImg[0])
      for i in ["tags","media","pallette"]:
        print(" "*6,"enter "+i+":")
        ri=sys.stdin.readline()[:-1]
        if ri=="i":
          back["tags"]="sketch"
          back["media"]="ink on paper"
          back["pallette"]="black ink"
          break
        else:
          back[i]=ri
      print(json.dumps(back,sort_keys=True,indent=2))
      ea["back"]=back
      ea["desc"]=splDsc[0]
      """

    try:
      print(ea["back"])
    except:
      ea["back"]={"image":"blank"}
  cnt+=1
outf=open("tmp.data","w")
outf.write(json.dumps(data,sort_keys=True,indent=2))
outf.close()
print(bcnt)
print("..01x17")
#./dada_proc_spl_TitleImage.py
