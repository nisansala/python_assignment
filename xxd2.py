import sys
import string
import os.path

def xxd_file(file_path):
    fle=open(file_path,"r")
    count=0
    
    while True:
        cont=f.read(16)
        data=cont
        if not cont:
            break
    
        col1=('%08x'%(count*16))
    
        ehex=d.encode('hex') 
        new_hex=ehex
        dehex=[new_hex[n:n+4] for n in range(0,len(new_hex),4)]
        col2=' '.join(map(str,dehex))

        col3=ehex.decode('hex')
		
    
        print('{0}: {1:<39} {2}'.format(col1,''.join(col2),''.join([col3 if col3 in string.printable[:-5] else '.' for col3 in data])))

        count += 1

if not os.path.exists(sys.argv[1]):
    print('Invalid File Path')
    sys.exit(1)
xxd_file(sys.argv[1])
