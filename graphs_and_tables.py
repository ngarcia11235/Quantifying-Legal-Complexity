import sys
import matplotlib.pyplot as plt
import math
def main():
    f=open(sys.argv[1])
    dictlist=eval(f.read())
    graphmaker(dictlist)
    a=input('do you want to make a histogram(y): ')
    while a=='y':
        histmaker(dictlist)
        a=input('do you want to make a histogram(y): ')
    a=input('do you want to make a table(y): ')
    if a=='y':
        tablemaker(dictlist)
def graphmaker(dictlist):
    c1=input('do you want a graph(y): ')
    while c1=='y':
        c2=input('first variable?')
        c3=input('second variable?')
        mult=input('multilevel?')
        c4=input('level')
        g1=[]
        g2=[]
        if mult=='multilevel':
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            g1=[]
            g2=[]
            col=input('color')
            mar=input('shape')
            for x in dictlist:
                if dictlist[x]['locdict']['level']==c4:
                    g1.append(math.log(dictlist[x]['infodict'][c2]+1))
                    g2.append((dictlist[x]['infodict'][c3]))
            ax1.scatter((g1),(g2),s=10,c=col,marker=mar)
            c4=input('level')
        elif c4=='all':
            for x in dictlist:
                g1.append(math.log(dictlist[x]['infodict'][c2]+1))
                g2.append((dictlist[x]['infodict'][c3]))
            plt.scatter((g1),(g2),s=10,c='r',marker='*')
        else:
            for x in dictlist:
                if dictlist[x]['locdict']['level']==c4:
                    g1.append(math.log(dictlist[x]['infodict'][c2]+1))
                    g2.append((dictlist[x]['infodict'][c3]))
            plt.scatter((g1),(g2),s=10,c='r',marker='*')
        plt.show()
        c1=input('do you want a new graph(y): ')
    if c1=='all':
        var=['words','awl','nve','cfc','nsub']
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        level={'digest':['r','*'], 'time':['g','*'], 'jurist':['g','o'], 'work':['g','s'], 'referance book':['g','+'], 'book':['y','^'], 'section':['y','s'], 'passage':['b','>']}
        for c2 in var:
            for c3 in var:
                g1=[]
                g2=[]
                for x in level:
                    print(x)
                    for y in dictlist:
                        if dictlist[y]['locdict']['level']==x:
                            g1.append(dictlist[y]['infodict'][c2])
                            g2.append(dictlist[y]['infodict'][c3])
                    ax1.scatter((g1),(g2),s=10,c=level[x][0],marker=level[x][1])
        plt.show()
def histmaker(dictlist):
    level=input('level: ')
    data=input('data: ')
    name=[]
    a=1
    stat=[]
    for x in dictlist:
        if dictlist[x]['locdict']['level']==level:
            name.append(dictlist[x]['locdict']['ref'])
            stat.append(dictlist[x]['infodict'][data])
            a+=1
    plt.bar(name,stat)
    plt.show()
def tablemaker(dictlist):
    print('ref','|','level','|','words','|','awl','|','nsub','|','nve','|','cfc')
    for x in dictlist:
        print(dictlist[x]['locdict']['ref'],(' '*(10-len(str(dictlist[x]['locdict']['ref'])))),'|',dictlist[x]['locdict']['level'],(' '*(15-len(str(dictlist[x]['locdict']['level'])))),'|',dictlist[x]['infodict']['words'],(' '*(7-len(str(dictlist[x]['infodict']['words'])))),'|',dictlist[x]['infodict']['awl'],(' '*(7-len(str(dictlist[x]['infodict']['awl'])))),'|',dictlist[x]['infodict']['nsub'],(' '*(3-len(str(dictlist[x]['infodict']['nsub'])))),'|',dictlist[x]['infodict']['nve'],(' '*(7-len(str(dictlist[x]['infodict']['nve'])))),'|',dictlist[x]['infodict']['cfc'],(' '*(7-len(str(dictlist[x]['infodict']['cfc'])))))
        print('------------+------------------+----------+----------+------+----------+----------')
main()
