import sys
import math
import numpy as np
import gzip
import sqlite3
import collections
import json
def main():
    text,c=setup()
    dictlist=dictget(c[0],c[1],c[2])
    dictlist=dualparsall(dictlist)
    dictlist=infoget(dictlist)
    print(dictlist)
def setup():
    filename=sys.argv[1]
    conn=sqlite3.connect(filename)
    cur=conn.cursor()
    cur1=conn.cursor()
    cur2=conn.cursor()
    text=getext(cur)
    c=cur,cur1,cur2
    return text,c
def dictget(cur,cur1,cur2):
    refddict={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
    "locdict":{"level":"","name":"","supers":'',"sub":[],"ref":0}}
    dictlist={}
    for row in cur.execute('SELECT * FROM text ORDER BY id'):
        id1=row[5]+0.1
        id2=row[2]+0.2
        id3=round(row[7]+0.3+(id2/10000),5)
        id4=row[0]+0.4
        sct=row[2]
        if id1 not in dictlist:
            dictlist[id1]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
            "locdict":{"level":"book","name":"book {}".format(id1),"supers":0,"sub":[],"ref":id1}}
        if id2 not in dictlist:
            dictlist[id1]["locdict"]["sub"].append(id2)
            dictlist[id1]["infodict"]['nsub']+=1
            dictlist[id2]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"section","name":"","supers":[id1,0],"sub":[],"ref":id2}}
            for row1 in cur1.execute('SELECT * FROM section ORDER BY id'):
                if row1[0]==sct:
                    dictlist[id2]["locdict"]['name']=row1[1]
        if id3 not in dictlist:
            if id3 in dictlist[id2]["locdict"]["sub"]:
                print('oh no')
                print(id3)
            dictlist[id2]["locdict"]["sub"].append(id3)
            dictlist[id2]["infodict"]['nsub']+=1
            dictlist[id3]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"passage","name":"{}/{}".format(id2,int(id3)),"supers":[id2,id1,0],"sub":[],"ref":id3}}
        if id4 not in dictlist:
            if id4 in dictlist[id3]["locdict"]["sub"]:
                print('oh no')
                print(id4)
            dictlist[id3]["locdict"]["sub"].append(id4)
            dictlist[id3]["infodict"]['nsub']+=1
            dictlist[id4]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"textunit","name":row[1],"supers":[id3,id2,id1,0],"sub":"NONE","ref":id4}}
    #----------------------------------------------------------------------------------------------------------
    dictlist[0]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                 "locdict":{"level":"digest","name":"digest","supers":"NONE","sub":[],"ref":0}}
    for x in range(50):
        dictlist[0]["locdict"]["sub"].append(x+1.1)
    for x in range(12):
        dictlist[0]["locdict"]["sub"].append(-x-1.1)
    jref={28:[-1.1,"125bc-100bc"],29:[-1.1,"125bc-100bc"],14:[-2.1,"75bc-50bc"],0:[-3.1,"50bc-25bc"],2:[-3.1,"50bc-25bc"],27:[-4.1,"50-75"],11:[-5.1,"100-125"],6:[-5.1,"100-125"],22:[-5.1,"100-125"],12:[-6.1,"125-150"],17:[-6.1,"125-150"],26:[-6.1,"125-150"],35:[-6.1,"125-150"],18:[-6.1,"125-150"],1:[-7.1,"150-175"],31:[-7.1,"150-175"],9:[-7.1,"150-175"],36:[-7.1,"150-175"],24:[-7.1,"150-175"],30:[-7.1,"150-175"],20:[-8.1,"175-200"],7:[-8.1,"175-200"],4:[-8.1,"175-200"],23:[-8.1,"175-200"],33:[-9.1,"200-225"],5:[-9.1,"200-225"],8:[-9.1,"200-225"],13:[-9.1,"200-225"],25:[-9.1,"200-225"],34:[-9.1,"200-225"],32:[-9.1,"200-225"],19:[-10.1,"225-250"],16:[-10.1,"225-250"],21:[-10.1,"225-250"],15:[-10.1,"225-250"],3:[-11.1,"300-325"],10:[-12.1,"325-350"]}
    read=0
    #----------------------------------------------------------------------------------------------------------
    for row in cur.execute('SELECT * FROM text ORDER BY id'):
        id4=row[10]
        a=0
        read+=1
        for row1 in cur1.execute("SELECT * FROM book ORDER BY id"):
            if row1[0]==id4:
                id3=row1[1]
                name1=row1[3]
                break
        for row2 in cur2.execute('SELECT * FROM work ORDER BY id'):
            if id3==row2[0]:
                id2=row2[1]
                jur=row2[1]
                name2=row2[2]
                a=1
                break
        id1=(jref[id2][0])
        if id1 not in dictlist:
            dictlist[id1]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
            "locdict":{"level":"time","name":jref[id2][1],"supers":0,"sub":[],"ref":id1}}
        id2=-(id2+0.2)
        id3=-(id3+0.3)
        id4=-(id4+0.4)
        if id2 not in dictlist:
            dictlist[id1]["locdict"]["sub"].append(id2)
            dictlist[id1]["infodict"]['nsub']+=1
            dictlist[id2]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"jurist","name":"","supers":[id1,0],"sub":[],"ref":id2}}
            for row1 in cur1.execute('SELECT * FROM jurist ORDER BY id'):
                if row1[0]==jur:
                    dictlist[id2]["locdict"]["name"]=row1[1]
                    break
        if id3 not in dictlist:
            dictlist[id2]["locdict"]["sub"].append(id3)
            dictlist[id2]["infodict"]['nsub']+=1
            dictlist[id3]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"work","name":name2.format(id2,id3),"supers":[id2,id1,0],"sub":[],"ref":id3}}
        if id4 not in dictlist:
            if id3 in dictlist[id3]["locdict"]["sub"]:
                print('oh no')
                print(id3)
            dictlist[id3]["locdict"]["sub"].append(id4)
            dictlist[id3]["infodict"]['nsub']+=1
            dictlist[id4]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":"referance book","name":name1,"supers":[id3,id2,id1,0],"sub":[],"ref":id4}}
        if round(row[7]+0.3+(row[2]+0.2)/10000,5) not in dictlist[id4]["locdict"]["sub"]:
            if round(row[7]+0.3+(row[2]+0.2)/10000,5) in dictlist[id4]["locdict"]["sub"]:
                print('somethings wrong')
            dictlist[id4]["locdict"]["sub"].append(round(row[7]+0.3+(row[2]+0.2)/10000,5))
            dictlist[id4]["infodict"]['nsub']+=1
            dictlist[round(row[7]+0.3+(row[2]+0.2)/10000,5)]["locdict"]['supers'].extend([id4,id3,id2,id1])
    return dictlist
def infoget(dictlist):
    i=0
    for x in dictlist:
        dictlist[x]['infodict']['textunits']=0
        i+=1
        text=''
        subs=[]
        a=0
        subs2=[]
        skip=0
        if dictlist[x]["locdict"]["sub"]=='NONE':
            text+=dictlist[x]["locdict"]['name']
            text+=' '
        elif x==0:
            dictlist[0]["infodict"]={'words':805042,'awl':6.649753677447885,'nsub':50,'nve':0.77835244855424,'cfc':3.130901366621497}
            skip=1
        else:
            subs=dictlist[x]["locdict"]["sub"]
            while a==0:
                i2=0
                for y in subs:
                    i2+=1
                    if dictlist[y]["locdict"]["sub"]=='NONE':
                        dictlist[x]['infodict']['textunits']+=1
                        text+=dictlist[y]["locdict"]['name']
                        text+=' '
                        a=1
                    else:
                        subs2.extend(dictlist[y]["locdict"]['sub'])
                subs=subs2.copy()
                subs2=[]
        if len(clearn(text))==0:
            skip=1
        if skip!=1:
            words=clearn(text)
            newfreq(words.copy())
            dictlist[x]["infodict"]["words"]=len(words)
            dictlist[x]["infodict"]["awl"]=round(len(text)/len(words),5)
            dictlist[x]["infodict"]["nve"]=round(entropy(newfreq(words.copy()),words),5)
            dictlist[x]["infodict"]["cfc"]=round(compcalc(words),5)
    return dictlist
    #for each level for each sub...collect base level units->save in text variable... run analysis on text -> alter infodict -> 
def getext(cur):# extracts and returns text from database 
    s=''
    for row in cur.execute('SELECT * FROM text ORDER BY book_no'):
        s+=row[1]
        s+=' '
    return s
def clearn(text):
    # cleans up the input and returns a more usable text
    newword=''
    wordlist=[]
    v=0
    for x in text:
        a=0
        v+=1
        if 64<ord(x)<91:
            a=1
            newword+=x
        if 96<ord(x)<123:
            a=1
            newword+=x
        if a==0:
            if newword!='':
                wordlist.append(newword)
            newword=''
    return wordlist
def newfreq(word3):
    word3.sort()
    worf=collections.Counter(word3)
    worf1=[]
    for x in worf:
        worf1.append(worf[x])
    return worf1
def entropy(worf,words):
    # does  entropy calculation and returns normalized shannon entropy
    wordent=[]
    shanent=0
    normshanent=0
    for x in worf:
        y=x/len(words)
        z=-y*(math.log2(y))
        wordent.append(z)
    for x in wordent:
        shanent+=x
        if len(worf)>1:
            normshanent+=x/math.log2(len(worf))
        else: normshanent=0
    return normshanent
def compcalc(words):
    # compresses the text and returns compression factor
    x=''
    for y in words:
        x+=y
        x+=' '
    bytx=x.encode()
    lenword=len(bytx)
    lencomp=len(gzip.compress(bytx))
    compfact=lenword/lencomp
    return compfact
def dualparse(dictlist):
    #level1=int(input('0=section,1=book:'))
    #level2=int(input('3=ref book,4=work,5=jurist,6=time:'))
    expdict={3:4,4:3,5:2,6:2}
    namedict={0:'section',1:'book',3:'refbook',4:'work',5:'jurist',6:'time'}
    level=namedict[level1]+'/'+namedict[level2]
    newdict=dictlist.copy()
    for x in dictlist:
        if dictlist[x]['locdict']['level']=='passage':
            id1=dictlist[x]['locdict']['supers'][level1]
            id2=-dictlist[x]['locdict']['supers'][level2]
            id0=((int(id1)*(10**expdict[level2]))+int(id2)+(id1-int(id1)+(id2-int(id2))/10))
            name=dictlist[id1]['locdict']['name']+'/'+dictlist[-id2]['locdict']['name']
            if id0 not in newdict:
                newdict[id0]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":level,"name":name,"supers":[],"sub":[x],"ref":id0}}
                newdict[id0]['locdict']['sub'].append(x)
                newdict[x]['locdict']['sub'].append(id0)
            elif x not in newdict[id0]['locdict']['sub']:
                newdict[id0]['locdict']['sub'].append(x)
                newdict[x]['locdict']['sub'].append(id0)
    newdict=dict(sorted(newdict.items()))
    return newdict
def dualparsall(dictlist):
    expdict={3:4,4:3,5:2,6:2}
    namedict={0:'section',1:'book',3:'refbook',4:'work',5:'jurist',6:'time'}
    newdict=dictlist.copy()
    for level1 in range(1):
        level1+=1
        for level2 in range(3,7):
            level=namedict[level1]+'/'+namedict[level2]
            for x in dictlist:
                if dictlist[x]['locdict']['level']=='passage':
                    id1=dictlist[x]['locdict']['supers'][level1]
                    id2=-dictlist[x]['locdict']['supers'][level2]
                    id0=((int(id1)*(10**expdict[level2]))+int(id2)+(id1-int(id1)+(id2-int(id2))/10))
                    name=dictlist[id1]['locdict']['name']+'/'+dictlist[-id2]['locdict']['name']
                    if id0 not in newdict:
                        newdict[id0]={"infodict":{"words":0,"awl":0, "nsub":0, "nve":0, "cfc":0},
                          "locdict":{"level":level,"name":name,"supers":[],"sub":[x],"ref":id0}}
                        newdict[id0]['locdict']['sub'].append(x)
                        newdict[x]['locdict']['sub'].append(id0)
                    elif x not in newdict[id0]['locdict']['sub']:
                        newdict[id0]['locdict']['sub'].append(x)
                        newdict[x]['locdict']['sub'].append(id0)
        newdict=dict(sorted(newdict.items()))
    return newdict
main()
