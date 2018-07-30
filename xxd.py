f=open("nn.txt","r")
l=0
while True:
    cont=f.read(16)
    d=cont
    if not cont:
        break
    
    step=('%07x'%(l*16))
    
    ehex=d.encode('hex') 
    nehex=ehex
    dehex=[nehex[n:n+4] for n in range(0,len(nehex),4)]
    cc=' '.join(map(str,dehex))

    b=ehex.decode('hex')
    
    print('{0}: {1:<39} {2}'.format(step,''.join(cc),''.join(b)))
    l=l+1
    
