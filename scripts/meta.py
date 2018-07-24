#!/usr/bin/env python3
# dada meta processing lib for base.py


def ledgercount(data):
  #imagine,loop the artists

  #check
  found=1
  for md in data[0]["meta"].keys():
    if md=="ledgercount":
      found=0
  if found==0:
    for chk in ["unknown","bf"]:
      found=1
      for al in data[0]["meta"]["ledgercount"].keys():
        if al==chk:
          found=0
      if found==1:
        if chk=="unknown":
          data[0]["meta"]["ledgercount"][chk]=[]
        else:
          data[0]["meta"]["ledgercount"][chk]={}
      else:
        if chk=="unknown":
          data[0]["meta"]["ledgercount"][chk]=[]

  else:
    data[0]["meta"]["ledgercount"]={}
    data[0]["meta"]["ledgercount"]["bf"]={}
    data[0]["meta"]["ledgercount"]["unknown"]=[]


  #addend
  cnt=1 #skip meta
  while cnt<len(data):
    for artist in data[cnt].keys():
      for ea in data[cnt][artist]:
        ledger=ea["ledger"]
        try:
          spl=ledger.split(".")
          led=str(spl[0])
          num=int(spl[1])
          try:
            cur=data[0]["meta"]["ledgercount"][artist][led]
          except:
            cur=0
          if num>cur:
            data[0]["meta"]["ledgercount"][artist][led]=num
        except:
          data[0]["meta"]["ledgercount"]["unknown"].append(ea["title"]) #id numb?
    cnt+=1
  return data


def dmeta(data):
  data=ledgercount(data)
  return data

#lib | base.py
