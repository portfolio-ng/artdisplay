#!/usr/bin/env python3
# dada processing lib for base.py

import sys
import time
import json



def qworkA(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"
  obj["dim"]={}
  obj["dim"]["hei"]="17in"
  obj["dim"]["wid"]="12.5in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  #obj["ledger"]="1.0"+str((len(data[1]["bf"])+1))
  obj["ledger"]="1.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["1"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags","media","pallette"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj





def qworkB(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  obj["dim"]={}
  for item in ["hei","wid"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj["dim"][item]=ri+"in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"

  #obj["ledger"]="1.0"+str((len(data[1]["bf"])+1))
  obj["ledger"]="1.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["1"])+1)

  #andform=time.strftime("%Y%m%d") #if entering on the same day as photographed
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags","media","pallette"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj


def qworkC(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"
  obj["media"]="ink on paper"
  obj["pallette"]="black ink"
  obj["dim"]={}
  obj["dim"]["hei"]="12.5in"
  obj["dim"]["wid"]="8.5in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  obj["ledger"]="2.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["2"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj


def qworkD(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"
  obj["media"]="ink on paper"
  obj["pallette"]="black ink"
  obj["dim"]={}
  obj["dim"]["hei"]="11in"
  obj["dim"]["wid"]="4.5in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  obj["ledger"]="2.00"+str(int(data[0]["meta"]["ledgercount"]["bf"]["2"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj



def qworkE(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"
  obj["media"]="ink on paper"
  obj["pallette"]="black ink"
  obj["dim"]={}
  obj["dim"]["hei"]="11in"
  obj["dim"]["wid"]="8.5in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  obj["ledger"]="2.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["2"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj



def qworkF(data):
  obj={}
  obj["date"]="1993"
  obj["location"]="San Francisco"
  obj["media"]="ink on paper"
  obj["pallette"]="black ink"
  obj["dim"]={}
  obj["dim"]["hei"]="12in"
  obj["dim"]["wid"]="10in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  obj["ledger"]="2.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["2"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj


def qworkG(data):
  obj={}
  obj["date"]="1953-1954"
  obj["location"]="Spain"
  obj["media"]="ink on paper"
  obj["pallette"]="black ink"
  obj["dim"]={}
  for item in ["hei","wid"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj["dim"][item]=ri+"in"
  obj["dim"]["dep"]="lsp"
  obj["dim"]["wei"]="lsp"
  obj["ledger"]="2.0"+str(int(data[0]["meta"]["ledgercount"]["bf"]["2"])+1)

  item="image"
  print(" "*6+"| enter "+item+":  IMG_201507...jpg")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  #andform=time.strftime("%Y%m%d")
  andform="201507"
  obj[item]="IMG_"+andform+str(ri)+".jpg"

  for item in ["title","desc","tags"]:
    print(" "*6+"| enter "+item+":")
    ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    obj[item]=ri

  print("  ..ledger:",obj["ledger"])
  return obj

#lib | base.py
