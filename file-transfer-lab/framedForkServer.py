#! /usr/bin/env python3
import sys
sys.path.append("../lib")       # for params

import os, socket, params


switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)
print("waiting for connections")

ll = list()
while True:
    sock, addr = lsock.accept() #Establish connection
    print("connected to address", addr)
    
    from framedSock import framedSend, framedReceive

    if not os.fork():
        print("new child process handling connection from", addr)
        while True:
            payload = framedReceive(sock, debug)
            
            if debug: print("rec'd: ", payload)
            if not payload:
                if debug: print("child exiting")
                sys.exit(0)
            payload += b"!"             # make emphatic!
            framedSend(sock, payload, debug)
            if(sys.getsizeof(payload) > 100):
                print("i dont like it ")
       
           
           
            ll.append(payload.decode())
            print(ll)
            filer = open("theFile.txt","w")
            for item in ll:
                print(item)
                filer.write(item)
                filer.write("\n")
            filer.close()
            
         
    sock.close()           
            
           
           
