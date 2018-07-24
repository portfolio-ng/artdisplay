#!/usr/bin/env python3
#naive cli json datastore to quickly archive works


import json
import sys
import readline
import time
import meta #meta.py
import dqwork #dqwork.py

#open existing database or create anew
## save old data in case of error

#filen="tmp.data" #testing
filen="data.nu"


try:
  fin=open(filen,"r")
  data=json.loads(fin.read())
  fin.close()
  print("..found data")
except:
  print("corrupt data store")
  print("  copy of old file saved to corrupt.TIMESTAMP.data")
  corrupt="corrupt."+time.strftime("%Y.%m.%d.%H.%M.%S")+".data"  #import time
  import subprocess
  subprocess.call(["cp","data",corrupt])
  data=[]
  print("data =",data)



#general commands
commands={
    "ref":"reference",
    "done":"exit",
    "pprint":"pretty print the entire datastore",
    "pmeta":"print meta data"
    }

#specific commands
spcomm={
  "dnew": "add a new artiste",
  "nwork":"add a new work to artiste",
  "wcount":"print number of works in artist's data store",
  "nitem":"add a new work item, this will step through existing works without the item",
  "qwork":"quickly add new work with recurring characteristics",
  "swork":"reuse specified properties in similar works"
  }


def dpmeta(data):
  print(json.dumps(data[0],sort_keys=True,indent=2))

def dpref(): #print reference
  print(" "*6+"______________________")
  print(" "*6+"|__ general commands :")
  for i in commands.keys():
    print(" "*6+"|",i,":",commands[i])
  print(" "*6+"|__ specific commands :")
  for i in spcomm.keys():
    print(" "*6+"|",i,":",spcomm[i])
  print(" "*6+"|_____________________")


def tofile(data):
  fout=open(filen,"w")
  fout.write(json.dumps(data,sort_keys=True,indent=2))
  fout.close()


def dpprint(data):
  print("_"*17)
  print(json.dumps(data,sort_keys=True,indent=2))
  print("_"*17)
def dnew(data): # data, insert new
  print(" ..enter artist name:   '!c' to cancel")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  if ri!="!c":
    data.append({str(ri):[]})
  return data


def fandb(obj,data):
  tags=obj["tags"].split(',')
  found=1
  for et in tags:
    if et=="front and back":
     found=0
  if found==0:
    print("  curr :")
    print(json.dumps(obj,sort_keys=True,indent=2))
    print("  back :")
    #bobj=workobj(data)
    bobj={}
    for bc in ["title","desc","tags","media","image","pallette"]:
      if bc=="image":
        print(" "*6+"| enter "+bc+":  IMG_201507...jpg")
        bri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        andform="201507"
        bobj[bc]="IMG_"+andform+str(bri)+".jpg"
      else:
        print(" "*6+"| enter "+bc+":")
        bri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        bobj[bc]=bri
    for bs in ["date","location","dim"]:
      bobj[bs]=obj[bs]
    bobj["ledger"]=obj["ledger"]+"b"
  else:
    bobj={"image":"blank"}
  obj["back"]=bobj
  return obj

def chklst(it,lplst):
  for lt in lplst:
    if str(lt)==str(it):
      return 0
  return 1

def ledgerinc(ri,data):
  #so far only for bill,check artist
  try:
    cur=data[0]["meta"]["ledgercount"]["bf"][ri]
  except:
    print(" created a new ledger:"+ri)
    data[0]["meta"]["ledgercount"]["bf"][ri]=0
    cur=data[0]["meta"]["ledgercount"]["bf"][ri]
  nxt=int(cur)+1
  zer=3-len(str(nxt))
  ldg=str(ri)+"."+"0"*zer+str(nxt)
  return ldg

def loopobj(lplst,obj,data):
  for it in obj.keys():
      if it=="dim":
        print(" "*6+"| enter "+it+":")
        for dt in obj["dim"]:
          sim=chklst(dt,lplst)
          if sim==1: #asimilar requires ammending, similar goes unaffected
            print(" "*8+"-| "+str(dt)+":"+str(obj["dim"][dt]))
            ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
            if ri=="":
              lplst.append(dt)
            else:
              if dt=="hei" or dt=="wid":
                obj["dim"][dt]=ri+"in"
              else:
                obj["dim"][dt]=ri
      elif it=="ledger":
        print(" "*6+"| enter "+it+":")
        ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        if ri=="":
          ri=obj["ledger"].split(".")[0]
        obj["ledger"]=ledgerinc(ri,data)
      elif it=="back":
        obj["back"]={"image":"blank"}
      elif it=="tags":
        print(" "*6+"|  "+str(it)+":"+str(obj[it]))
        ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        if ri=="":
          continue
        else:
          obj[it]=ri
      elif it=="image":
        print(" "*6+"| enter "+it+":  IMG_201507...jpg")
        ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        andform="201507"
        obj[it]="IMG_"+andform+str(ri)+".jpg"
      else:
        sim=chklst(it,lplst)
        if sim==1: #asimilar requires ammending, similar goes unaffected
          print(" "*6+"|  "+str(it)+":"+str(obj[it]))
          ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
          if ri=="":
            lplst.append(it)
          else:
            obj[it]=ri
  obj["lplst"]=lplst
  return obj


def loopentry(lplst,obj,data):
  if obj=={}:
    obj=workobj(data)
    obj["lplst"]=lplst
  else:
    obj=loopobj(lplst,obj,data)
  return obj

def swork(data):
  print(" "*6+"how many similar works?       ae to loop")
  ae=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  print(" "*8+"::"+ae)
  cnt=0
  if ae=="ae":
    ea=1
  else:
    ea=int(ae)
  obj={}
  lplst=[]
  while cnt<ea:
    data=meta.dmeta(data)
    print(" ..looping "+str(cnt+1)+" of "+str(ea))
    ole=json.loads(json.dumps(obj))
    obj=loopentry(lplst,ole,data)
    lplst=obj["lplst"]
    del obj["lplst"]
    nuw=json.loads(json.dumps(obj))
    obj=fandb(nuw,data)
    data[1]["bf"].append(obj) #for bf
    tofile(data)
    print(" ..ledger count: "+obj["ledger"])
    if ae=="ae":
      print(" ..another entry?   0::for similar 1:: for asimilar ")
      ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
      if ri=="0" or ri=="0:" or ri=="0::" or ri=="0:: ":
        cnt=0
      else:
        cnt=1
    else:
      cnt+=1
  return data


def qwork(data):
  bg=1
  group="G"

  print(" "*6+"qwork group: "+group)
  if group=="A":
    obj=dqwork.qworkA(data)
  elif group=="B":
    obj=dqwork.qworkB(data)
  elif group=="C":
    obj=dqwork.qworkC(data)
  elif group=="D":
    obj=dqwork.qworkD(data)
  elif group=="E":
    obj=dqwork.qworkE(data)
  elif group=="F":
    obj=dqwork.qworkF(data)
  elif group=="G":
    obj=dqwork.qworkG(data)
  else:
    print(" ?? bad group in qwork")
    bg=0
  if bg==1:
    obj=fandb(obj,data)
    data[1]["bf"].append(obj) #for bf
  return data


def workobj(data):
  obj={}
  print("\n")
  print(" "*6+"_"*17)
  for item in data[0]["meta"]["workitems"]:
    if item=="dim":
      obj[item]={}
      print(" "*6+"| enter "+item+":    ..units in inches")
      for td in ["hei","wid","dep","wei"]:
        print(" "*8+"-| enter "+td+":")
        ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
        if td=="hei" or td=="wid":
          obj[item][td]=ri+"in"
        else:
          obj[item][td]=ri
    elif item=="image":
      print(" "*6+"| enter "+item+":  IMG_201507...jpg")
      ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
      #andform=time.strftime("%Y%m%d") #import time
      andform="201507"
      obj[item]="IMG_"+andform+str(ri)+".jpg"
    elif item=="ledger":
      print(" "*6+"| enter "+item+":")
      ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
      obj["ledger"]=ledgerinc(ri,data)
    else:
      print(" "*6+"| enter "+item+":")
      ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
      obj[item]=ri
  print(" "*6+"_"*17)
  return obj

def nwork(data):
  print("  ..add new work to which artiste?:")
  print("                   'ls' to list")
  print("                   '!c' to cancel")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  if ri!="!c":
    if ri=="ls":
      for ai,a in enumerate(data):
        if ai>0:
          print(" _"+str(ai)+" '"+str(list(a.keys())[0])+"'")
      data=nwork(data)
    else:
      artist="fail"
      for ai,a in enumerate(data):
        if list(a.keys())[0]==ri:
          artist=ai
      if artist=="fail":
        print(" ??unknown artist:",ri,"\n")
        data=nwork(data)  #fuck, infinite failures create infinite recursion chain
      else:
        art=data[artist][str(ri)]
        aobj=workobj(data)
        obj=fandb(aobj,data)
        art.append(obj)
  return data

def nitem(data):
  print("  ..add new item to work items list:")
  print("                   'ls' to list")
  print("                   '!c' to cancel")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  if ri!="!c":
    if ri=="ls":
      for ea in data[0]["meta"]["workitems"]:
        print(" _"+ea)
      data=nitem(data)
    else:
      data[0]["meta"]["workitems"].append(ri)
  return data

def wcount(data):
  print("  ..which artiste?:")
  print("                   'ls' to list")
  print("                   '!c' to cancel")
  ri=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
  if ri!="!c":
    if ri=="ls":
      for ai,a in enumerate(data):
        if ai>0:
          print(" _"+str(ai)+" '"+str(list(a.keys())[0])+"'")
      wcount(data)
    else:
      artist="fail"
      for ai,a in enumerate(data):
        if list(a.keys())[0]==ri:
          artist=ai
      if artist=="fail":
        print(" ??unknown artist:",ri,"\n")
        wcount(data)
      else:
        print(" # of works:",len(data[artist][ri]))



def checkmeta(data):
  if len(data)==0:
    data.append({"meta":{}})
  else:
    found=1
    for sm in data[0]: #search for meta property
      if sm=="meta":
        found=0
        break
    if found==1:
      #insert meta in 0 index
      meta=[{"meta":{}}] #create meta in 0 ind
      meta.append(data)  #append data to meta
      data=meta #update data with meta
  return data

def checkworkitems(data):
  #artist work schema
  found=1
  for ea in data[0]["meta"]:
    if ea == "workitems":
      found=0
  if found==1:
    data[0]["meta"]["workitems"]=["title","desc","tags","media","date","location","dim","ledger","image","pallette"]
  return data

def check(data):
  data=checkmeta(data)
  data=checkworkitems(data)
  return data


def onit(data):
  data=check(data)
  readin=17
  while str(readin)!="done":
    data=meta.dmeta(data)
    tofile(data)
    print("  enter command :     'ref' for reference")
    readin=sys.stdin.readline()[:-1] #[:-1] removes the '\n' at the end
    #general data store commands
    if readin=="done":
      break
    elif readin=="ref":
      dpref() #print reference
    elif readin=="pprint":
      dpprint(data) #print reference
    elif readin=="pmeta":
      dpmeta(data) #print meta
    else:
      #use case specific commands
      if readin=="dnew":
        data=dnew(data)
      elif readin=="nwork":
        data=nwork(data)
      elif readin=="qwork":
        data=qwork(data)
      elif readin=="swork":
        data=swork(data)
      elif readin=="nitem":
        data=nitem(data)
      elif readin=="wcount":
        wcount(data)
      else:
        print(" ??unknown command '"+str(readin)+"', try ref to see a list of commands\n")

onit(data)

print("..01x17")
#./base  #naive cli datastore to quickly archive works: saves to data.nu
