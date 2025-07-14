
Used to encrypt packets. Consist of a TCP connection (not sure what that is) and then each packet consist of a Packet length ( 4 bytes), padding amount( 1 byte) , payload (actual data , size varies), padding, Message authentication code ( this is to show if the messsage was tampered with. THis works because payload + padding = a unique code so some tampering would result in a different code.

As well as we can open several channels between machine an server. Which allows for multiple connections. 