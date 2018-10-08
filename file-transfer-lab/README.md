# nets-tcp-framed-echo
The Following lab conducts a file transfer with the following criteria





* be in the file-transfer-lab subdir
* work with and without the proxy
* support multiple clients simultaneously using `fork()`
* gracefully deal with scenarios such as: 
    * zero length files
    * user attempts to transmit a file which does not exist
    * file already exists on the server
    * the client or server unexpectedly disconnect
* optional (unless you're taking this course for grad credit): be able to request ("get") files from server

To rung the program first type 
$python3 framedServer.py

then open a new terminal and type

$ python3 framedClient.py

