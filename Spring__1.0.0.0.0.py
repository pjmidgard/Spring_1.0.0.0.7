import os
import binascii
zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("c for compress u for extract? ")
if namez=="u":
    name = input("What is name of file? ")
    namea="file.Spring"
    namem=name+"/"
    namema="?"
    namemas="<"
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        
        lenf1=len(data)
        szx=""
        sda=bin(int(binascii.hexlify(data),16))[2:]
        szx=""
        lenf=len(sda)
        xc=8-lenf%8
        z=0
        if xc!=0:
            if xc!=8:
                while z<xc:
                    szx="0"+szx
                    z=z+1
        sda=szx+sda     
        lenf=len(sda)
        lenfaq=len(sda)
        szx=""
            
        adda=0
        asss=0
        add=0
        qwss=""
        qqqe=5
        qqs=5
        for byte in data:
                
                 
            if byte==47 and qqs!=1 and qqs!=2:
                asss=1
                qqqe=0
                qqs=1
                
            elif byte==60 and qqs!=1 and qqs!=3:
                asss=1
                qqqe=2
                qqs=2

            elif byte==63 and qqs!=2 and qqs!=1:
                asss=1
                qqqe=1
                qqs=3
                       
                        
            if asss==0:
                add=add+1
        saqqraz=byte
        aqwe1=""
        zaaqa=0
        zaaqaz=0
        zaaqa=lenf1-2
        zaaqaz=lenf1-1
        aqwe1=data[zaaqa:zaaqaz]
        aaa1=""        
        ##print(add)
        with open(name, "rb") as za:     
            dataa = za.read()
        add=add
        sss1=add-2
        aaa1=dataa[0:add]
        ##print(aaa1)
        aaa2=aaa1.decode("utf-8")
        ##print(aaa2)
        s=""
        if qqqe==0:
            with open(aaa2, "w") as f11:
                f11.write(s)

        elif qqqe==2:
            with open("file.Angel", "w") as f12:
                f12.write(s)
        elif qqqe==1:
            with open("filea.Spring", "w") as f13:
                f13.write(s)
        ##print(qqqe)
        
        howtimeoncompress=data[lenf1-1:lenf1]
        for byte in howtimeoncompress:    
            
           howtimeoncompressshow=byte
        ##print(howtimeoncompressshow)
        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(howtimeoncompressshow/8)
        lenfq2=lenf1-1
        lenfq3=lenfq2-bbs
        aqwe=data[lenfq3:lenfq2]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        howtimeoncompressshow2=cvz3
        ##print(howtimeoncompressshow2)
        nulliidinici=data[lenfq3:lenfq2]
        lenfq4=lenfq3
        lenfq5=lenfq4-1
        nulliidinicisix1=0
        nulliidinicisix=data[lenfq5:lenfq4]
        for byte in nulliidinicisix:
            nulliidinicisix1=byte
        ##print(nulliidinicisix1)

        
        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(nulliidinicisix1/8)
        lenfq6=lenfq5
        lenfq7=lenfq6-bbs
        aqwe=data[lenfq7:lenfq6]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        nulliidinicisix2=cvz3
        ##print(nulliidinicisix2)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(nulliidinicisix2/8)
        lenfq8=lenfq7
        lenfq9=lenfq8-bbs
       
        aqwe=data[lenfq9:lenfq8]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        nulliidinicisix3=cvz3
        ##print(nulliidinicisix3)

         
        lenfq11=lenfq9
        lenfq12=lenfq11-1
        
        n1000r=0
        ss=data[lenfq12:lenfq11]
        for byte in  ss:
            n1000r=byte
        ##print(n1000r)


        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(n1000r/8)
        lenfq13=lenfq12
        lenfq14=lenfq12-bbs
       
        aqwe=data[lenfq14:lenfq13]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        n1000r2=cvz3
        ##print(n1000r2)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(n1000r2/8)
        lenfq15=lenfq14
        lenfq16=lenfq15-bbs
       
        aqwe=data[lenfq16:lenfq15]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        n1000r3=cvz3
        ##print(n1000r3)

        #lastbitblocksize

        lenfq17=lenfq16
        lenfq18=lenfq17-1
        
        nlastbitblocksize=0
        ssw=data[lenfq18:lenfq17]
        for byte in  ssw:
            nlastbitblocksize=byte
        ##print(nlastbitblocksize)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(nlastbitblocksize/8)
        lenfq19=lenfq18
        lenfq20=lenfq19-bbs
       
        aqwe=data[lenfq20:lenfq19]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        nlastbitblocksize2=cvz3
        ##print(nlastbitblocksize2)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(nlastbitblocksize2/8)
        lenfq21=lenfq20
        lenfq22=lenfq21-bbs
       
        aqwe=data[lenfq22:lenfq21]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        nlastbitblocksize3=cvz3
        ##print(nlastbitblocksize3)

        lenfq23=lenfq22
        lenfq24=lenfq23-1
        
        nlastbitblocksize=0
        ssw=data[lenfq24:lenfq23]
        for byte in  ssw:
            one0111=byte
        ##print(one0111)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(one0111/8)
        lenfq25=lenfq24
        lenfq26=lenfq25-bbs
       
        aqwe=data[lenfq26:lenfq25]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        two0111=cvz3
        ##print(two0111)

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(two0111/8)
        lenfq27=lenfq26
        lenfq28=lenfq27-bbs
       
        aqwe=data[lenfq28:lenfq27]
        for byte in aqwe:
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                
                
            
            cvz3=cvz3+bnks
            
            bbs=bbs-1
        
        
        three0111=cvz3
        ##print(three0111)

        lenfq29=lenfq28
        lenfq30=lenfq29-1
        
        hszxzlz1=0
        ssw=data[lenfq30:lenfq29]
        for byte in  ssw:
            hszxzlz1=byte
        ##print(hszxzlz1)
        
        #szxzlz1
        hszxzlz1=hszxzlz1-10
        lenfq31=lenfq30*8
        lenfq32=lenfq31-hszxzlz1
        wq=lenfq32
        rtsda=sda[lenfq32:lenfq31]
        asqrtsda=str(rtsda)
        ##print(asqrtsda)
        longofrtsa=len(asqrtsda)
        ##print(longofrtsa)
        
        lenfq33=lenfq32-1
        bit11sda=sda[lenfq33:lenfq32]
        bit11sdas=str(bit11sda)
        ##print(bit11sdas)
        ##print(add)
        


        zxy=0
        #start
        wer=""
        while howtimeoncompressshow2>zxy:
            zxy=zxy+1
            if zxy==1:
                ssqadd=add+1
                jlz=""
            else:
                ssqadd=0+1
                jlz=""
            ssqaddq=ssqadd*8
            ssqaddq1=(ssqadd*8)+8
            aaq=sda[ssqaddq:lenfq33]
            ##print(aaq)
            aaq=str(aaq)
            aql=len(aaq)
            
            d=1
            a=0
            p=0
            while p<1:
                                             
                aaqql=aaq[a:d]
                                                    
                if aaqql=="0":
                                            
                    a=a+1
                    d=d+1
                if aaqql=="1":
                    p=p+1
        
            qw=a+1
            wq=wq-hszxzlz1
            wq1=wq-1
            qweq=sda[wq:]
            
            ##print("qweq")
            ##print(qweq)
            ##print(howtimeoncompressshow2)
            ##print(zxy)
            qsww=len(qweq)
            ##print(qsww)

           

                     
            ##print(nulliidinicisix3)
            ##print(n1000r3)
            ##print(nlastbitblocksize3)
            ##print(three0111)
            
            # wer="1"+wer+aaqwsmovefirst0111+moveafter1000+asaaq1110006+"1"
            nulliidinicisix3minus=aql-nulliidinicisix3
            
            q1qweq1=aaq[nulliidinicisix3minus:]

            ##print(q1qweq1)
            ##print("1")

            nlastbitblocksize3minus=nulliidinicisix3minus-n1000r3
            q2qweq1s=aaq[nlastbitblocksize3minus:nulliidinicisix3minus]

            ##print(q2qweq1s)
            ##print("2")

            n1000r3minus=nlastbitblocksize3minus-three0111
            q3qweq1=aaq[n1000r3minus:nlastbitblocksize3minus]

            ##print(q3qweq1)
            ##print("3")

            nulliidinicisix3minus=n1000r3minus-nlastbitblocksize3
            q4qweq1=aaq[nulliidinicisix3minus:n1000r3minus]

            ##print(q4qweq1)
            ##print("4")
            
            qtqweq1=aaq[1:nulliidinicisix3minus]

            ##print(qtqweq1)
            ##print("5")
            qtqweq1=str(qtqweq1)

            qqwp=len(qtqweq1)
            #print(qqwp)
            ao=0
            aqw=0
            ao1=0    
             
            
            
            q4qweq1s=str(q4qweq1)
            q3qweq1s=str(q3qweq1)
            q2qweq1s=str(q2qweq1s)
            q1qweq1s=str(q1qweq1)

            q4qweq1sa=len(q4qweq1s)
            q3qweq1sa=len(q3qweq1s)
            q2qweq1sa=len(q2qweq1s)
            q1qweq1sa=len(q1qweq1s)


                 
            aqw1=0
            aqw=0
            qq=0
            tranbd1=0
            #print(qtqweqw)
           # print(qqwp)
            tranbd=0
            tranbd1=1
          
            while ao<qqwp:
                
                 eo=ao
                 ao=ao+32
                 #print(ao)
                 #print(eo)
                 qtqweq2=qtqweq1[eo:ao]
                 #print(qtqweq2)
                 #print("ok")
                 qq=qq+1
                 
                 if tranbd1==qq:
                     
                     qw1=ao1
                     ao1=ao1+2
                     #print(qw1)
                     bitblockone0=q1qweq1s[qw1:ao1]
                     
                     if bitblockone0=="01":
                         qw1=ao1
                         ao1=ao1+8
                         bitblockone0w1=q1qweq1s[qw1:ao1]
                     if bitblockone0=="10":
                         qw1=ao1
                         ao1=ao1+16
                         bitblockone0w1=q1qweq1s[qw1:ao1]
                     if bitblockone0=="11":
                         qw1=ao1
                         ao1=ao1+24
                         bitblockone0w1=q1qweq1s[qw1:ao1]
                     tranbd=int(bitblockone0w1, 2)
                     tranbd1=tranbd+1
                     qw1=ao1
                     ao1=ao1+12
                     bitblockone0w2=q1qweq1s[qw1:ao1]
                     #print(tranbd)
                     #print(bitblockone0)
                     #os.system("pause")
                 if tranbd==qq:
                     if qq>1:
                         eo=ao-32
                         ao=ao-32
                     b2=bitblockone0w2+"00000000000000000000"
                     #print(b2)
                     #os.system("pause")
                     wer=wer+b2
                 else:
                     wer=wer+qtqweq2
                 

        ##print(qtqweqw)
        
        qtqweqw=""
        qtqweqw=qtqweqw+q4qweq1s
        wer=wer+qtqweqw
        qtqweqw=""
                                    
                     
        #print("wer")
        #print(wer)
        #print("wer")
        qqwslenf=len(wer)
        #print(qqwslenf)
        qqwslenf=(qqwslenf/8)*2
        qqwslenf=str(qqwslenf)
        qqwslenf="%0"+qqwslenf+"x"
        
        n = int(wer, 2)
                    
        jlz=binascii.unhexlify(qqwslenf % n)
        if qqqe==0:
            with open(aaa2, "wb") as f12:

                f12.write(jlz)
                
        elif qqqe==2:
            with open("file.Angel", "wb") as f12:
                
                f12.write(jlz)
        elif qqqe==1:
            with open("filea.Spring", "wb") as f12:
                
                f12.write(jlz)
                    
                   

           
            
            
            
if namez=="c":
    name = input("What is name of file? ")
    namea="file.Spring"
    namem=name+"/"
    namema="?"
    namemas="<"
    blockw=5
    blockw1=4
    
    s=""
    if name=="file.Angel":
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namemas)
    elif name=="filea.Spring":
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namema)
    else:    
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namem)
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        lenf1=len(data)

        if lenf1<6:
            ##print("This file is too small");
            raise SystemExit
        if lenf1>(2**24)-1:
            ##print("This file is too big");
            raise SystemExit

        while assx<10:
            if qqqwz>1:
                lenf1=sssssw
            a=0
            ass=0
            asss=0
            b=0
            aaqw=""
            aaqws=""
            l=""
            j=0
            b=0
            aq=0
            qfl=0
            t=0
            h=0
            byteb=""
            notexist=""
            lenf=0
            numberschangenotexistq = []
            numberschangenotexistqz = []
            qwa=0
            m = []
            p=0
            
            d=1
            a=0
            asd=""
            b=0
            szx=""
            asf2="0b"
            while b<1790:
                m+=[-1]
                b=b+1
            k = []
            wer=""
            numberschangenotexist = []
            numbers = []
            assa=0
            asaaq=""
            szxzzzas=""
            s=""
            blockw=4
            blockw1=3
            sdaa=""
            aas=0
            asaaq=""
            en=0
            ###print(blockw)
            
           
            with open(namea, "ab") as f2:
                sda=bin(int(binascii.hexlify(data),16))[2:]
                lenf=len(sda)
                xc=(lenf1*8)-lenf
                z=0
                if xc!=0:
                    while z<xc:
                        sda="0"+sda
                        z=z+1
                      
                for byte in sda:
                    sda=str(sda)
                    sdaa=sdaa+byte
                  
                    aas=aas+1
                   
                    if aas==8:
                        a=a+1
                        aas=0
            
                    if a == blockw:
                        
                        szxx=""
                        szxx=sdaa
             
                        wqwe=""
                        p=0
                        aaqq=""
                        d=1
                        a=0
                        da=0
                        aaqw=""
                        aaqql=""
                        assa=assa+1
                        if assa==(2**32)-1:
                           assaz="0"
                           assa="0"
                           #asaaq=asaaq+assaz
                        qqw1q="0"
                        
                        n=0
                        sssq=0
                        enx=0
                        if blockw==4:
                            
                            if szxx[12:]=="00000000000000000000":
                                qqw1q="10"
                                    

                                szxzzzas=""
                                szxzzzas=bin(assa)[2:]
                                dd=len(szxzzzas)
                                xc=8-dd%8
                                z=0
                                if xc!=0:
                                    while z<xc:
                                        szxzzzas="0"+szxzzzas
                                        z=z+1
                                szxzzzasaa=""        
                                dd=len(szxzzzas)
                                xc=dd/8
                                xc=int(xc)
                                if xc==1:
                                    szxzzzasaa="01"
                                if xc==2:
                                    szxzzzasaa="10"
                                if xc==3:
                                    szxzzzasaa="11"
                                  
                                qqqs=szxzzzasaa+szxzzzas+szxx[0:12]
                               
                                asaaq=asaaq+qqqs
                                            
                                            
                                        
                                ###print(asaaq)
                            
                            else:
                                wer=wer+szxx
                                
                       
                            
                        
                        
                        
                        sdaa=""
                        a=0
                        numberschangenotexist = []    
                        del k[:]
                            
                        del numbers[:]
                        m = []
                        b=0
                        while b<blockw:
                            m+=[-1]
                            b=b+1
                        b=0
                        b=0
                               
                                
                    s=a%blockw
                    
                if s!=0:
                    
                    
                    p=-1
                    if s!=blockw1:
                        
                        szx=sdaa
                        aqqd1=len(zzaax1)
                        if aqqd1==0:
                            szx=szx+""
                        else:
                            szx=szx
                        szx=szx+""
                        szx=""+szx
                        asss1=len(szx)
                        asss2=asss1-1
                        qqw=szx[asss2]
                        if qqw=="1":
                            szx=szx
                        if qqw=="0":
                            szx=szx
                        wer=wer+szx
                        lenfzzz=len(szx)
                        szx=""
                        fffgjv1=""
                        fffgjv=""
                            
                        lenf=len(szx)
                        szx=""
                        zzaax1=""        
                         
                        
                a=0
                szx=""
                
                
                
                
                dd=len(aaqws)
                dda=len(zzaax)


                ddwa=len(asaaq)
                
                szxzzzq=""
                szxzzzq=bin(ddwa)[2:]
                ddwa=len(szxzzzq)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzq="0"+szxzzzq
                        z=z+1
                
                ddwa=len(szxzzzq)


                szxzzzqq=""
                szxzzzqq=bin(ddwa)[2:]
                ddwa=len(szxzzzqq)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzqq="0"+szxzzzqq
                        z=z+1
                
                dd=len(szxzzzqq)

                szxzzzqqz=""
                szxzzzqqz=bin(dd)[2:]
                ddwa=len(szxzzzqqz)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzqqz="0"+szxzzzqqz
                        z=z+1

                dd=len(szxzzzqqz)

               
                
                dd=len(aaqws)
                
                szxzzz=""
                szxzzz=bin(dd)[2:]
                dd=len(szxzzz)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzz="0"+szxzzz
                        z=z+1
                
                dd=len(szxzzz)

                szxzzza=""
                szxzzza=bin(dda)[2:]
                dda=len(szxzzza)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzza="0"+szxzzza
                        z=z+1
                
                dda=len(szxzzza)

                szxzs=""
                szxzs=bin(dda)[2:]
                dda=len(szxzs)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzs="0"+szxzs
                        z=z+1
                        
                dda=len(szxzs)
                szxzff=""
                szxzff=bin(dda)[2:]
                dda=len(szxzff)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzff="0"+szxzff
                        z=z+1

                


                
                

                

                
                szxzz=""
                szxzc=""
                szxzc=bin(lenfzzz)[2:]
                dd=len(szxzc)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzc="0"+szxzc
                        z=z+1
                        
                dd=len(szxzc)
                szxzz=""

                aqqww=10
                szxzl=""
                szxzl=bin(dd)[2:]
                dd=len(szxzl)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzl="0"+szxzl
                        aqqww=aqqww+1
                        z=z+1
                
                aqqd1=len(zzaax)
                
               
                
                dd=len(szxzzz)

                szxz=""
                szxz=bin(dd)[2:]
                dd=len(szxz)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxz="0"+szxz
                        z=z+1
                        
                dd=len(szxz)

                szxzas=""
                szxzas=bin(dd)[2:]
                dda=len(szxzas)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzas="0"+szxzas
                        z=z+1
               
                if aqqd1>0:
                    wer="1"+wer+aaqws+zzaax+asaaq+"1"
                else:
                    wer="1"+wer+aaqws+zzaax+asaaq+"1"
                zzaax=""
                    
                # wer="1"+wer+aaqwsmovefirst0111+moveafter1000+asaaq1110006+"1"
                
                aqqwwa=10    
                lenf=len(wer)
                xc=8-lenf%8
                z=0
                if xc!=0:
                    while z<xc:
                        szx="0"+szx
                        z=z+1
                        aqqwwa=aqqwwa+1
                szxzlz=""

                
                ddd=len(szxzl)
                szxzlz=bin(ddd)[2:]
                dds=len(szxzlz)
                xc=8-dds%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzlz="0"+szxzlz
                        z=z+1


                szxzlz1=bin(aqqwwa)[2:]
                dds=len(szxzlz1)
                xc=8-dds%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzlz1="0"+szxzlz1
                        z=z+1
                
                wer=wer+szx+szxzlz1+szxzzz+szxz+szxzas+szxzc+szxzl+szxzlz+szxzzza+szxzs+szxzff+szxzzzq+szxzzzqq+szxzzzqqz
                szx=""
		
				#szxzzz 0111 one
				#szxz 0111 two
			    #szxzas 0111 three
				#szxzc lastbitblocksize one
				#szxzl lastbitblocksize two
				#szxzlz lastbitblocksize tree
				#szxzzza+szxzs+szxzff 1000
			    #szxzzzq+szxzzzqq+szxzzzqqz 11110000 6
                
                n = int(wer, 2)
                jl=binascii.unhexlify('%x' % n)
                data=jl
                sssssw=len(jl)
                qqqwz=qqqwz+1
                szxzzza=""
                szxzs=""
               
                
                blockw=4
                blockw1=3
            
                #print(sssssw)
                    
                
                
                if lenf1<=sssssw or qqqwz==1:
                    szxzzzqqax=""
                    szxzzzqqax=bin(qqqwz)[2:]
                    dd=len(szxzzzqqax)
                    xc=8-dd%8
                    z=0
                    if xc!=0:
                        while z<xc:
                            szxzzzqqax="0"+szxzzzqqax
                            z=z+1
                    
                    dd=len(szxzzzqqax)
                    szxzzzqq=""
                    szxzzzqq=bin(dd)[2:]
                    dd=len(szxzzzqq)
                    xc=8-dd%8
                    z=0
                    if xc!=0:
                        while z<xc:
                            szxzzzqq="0"+szxzzzqq
                            z=z+1
                    zsaqq=""
                    zsaqq=zsaqq+szxzzzqqax+szxzzzqq 
                    
                    
                    szx=""
                    wer=wer+zsaqq
                
                    n = int(wer, 2)

                    qqwslenf=len(wer)
                    qqwslenf=(qqwslenf/8)*2
                    qqwslenf=str(qqwslenf)
                    qqwslenf="%0"+qqwslenf+"x"
                    
                   
                                
                    jlz=binascii.unhexlify(qqwslenf % n)
                    
                    
                    
                    assx=10
                    if assx==10:
                        f2.write(jlz)
                    
                     
                    
                
          
                   
