f=open("nn.txt","r")
l=0
while True:
    cont=f.read(16)
    d=cont
    if not cont:
        break
    
    col1=('%07x'%(l*16))
    
    ehex=d.encode('hex') 
    nehex=ehex
    dehex=[nehex[n:n+4] for n in range(0,len(nehex),4)]
    col2=' '.join(map(str,dehex))

    col3=ehex.decode('hex')
    
    print('{0}: {1:<39} {2}'.format(col1,''.join(col2),''.join(col3)))
    l=l+1
    
