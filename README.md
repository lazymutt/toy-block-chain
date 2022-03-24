# toy blockchain

A toy blockchain, now with mining, in 60 lines of code.

Based on:
https://medium.com/@mukeshmishra0381/create-your-own-blockchain-using-python-7c6a117c5f70

Which itself may or may not be heavily borrowed from:
https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54

Cleaned up the example and added proof of work



Here's an example run at proof of work set to 7:

```
*
*
*
Block index:    0
 timestamp:     2022-03-21 18:24:04.485142
 nonce:         365673038
 data:          Genesis Block
 previous hash: 0
 current hash:  00000004529416b7011dcd0100b6974e9a83891e4c611cb33b43ea19caf35636

Block index:    1
 timestamp:     2022-03-21 18:38:49.866148
 nonce:         158106747
 data:          Block 1
 previous hash: 00000004529416b7011dcd0100b6974e9a83891e4c611cb33b43ea19caf35636
 current hash:  000000033dd12e201a98e1d420ce3a8b6908d1ef6350c2f9ba9183a9f3bd7d28

Block index:    2
 timestamp:     2022-03-21 18:45:26.447984
 nonce:         51644834
 data:          Block 2
 previous hash: 000000033dd12e201a98e1d420ce3a8b6908d1ef6350c2f9ba9183a9f3bd7d28
 current hash:  0000000e88466655ec52a380b97707760de96336bcf76df827e51af7a154df09

Block index:    3
 timestamp:     2022-03-21 18:47:36.435977
 nonce:         60966362
 data:          Block 3
 previous hash: 0000000e88466655ec52a380b97707760de96336bcf76df827e51af7a154df09
 current hash:  0000000bd8a4321fa1ebe6f9a2a02cfc2a6b43c32ffdbec57632b9a85f9a9d53

```

