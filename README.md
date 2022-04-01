# toy blockchain

A toy blockchain, now with mining, in 60 lines of code.

Based on:
https://medium.com/@mukeshmishra0381/create-your-own-blockchain-using-python-7c6a117c5f70

Which itself may or may not be heavily borrowed from:
https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54

Cleaned up the example and added proof of work.



Here's an example run at proof of work set to 5 and adding 7 blocks, plus the origin block:

```
$ ./toy_blockchain.py -b7 -p5
*
*
*
<<<<<<< Updated upstream
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
=======
*
*
*
*
Block index:    0
 timestamp:     2022-03-31 16:00:19.331386
 nonce:         333454
 data:          Genesis Block
 previous hash: 0
 current hash:  00000ca0fc3fd823dd02b30d0d8c74fca18ef49c80a2471941373d00aa789515

Block index:    1
 timestamp:     2022-03-31 16:00:20.668755
 nonce:         1869544
 data:          The sky above the port was the color of television, tuned to a dead channel.
 previous hash: 00000ca0fc3fd823dd02b30d0d8c74fca18ef49c80a2471941373d00aa789515
 current hash:  00000b0ef65d8235d7c7292dcb0f453af079673a94498ba66b23c26444100ebc

Block index:    2
 timestamp:     2022-03-31 16:00:29.115289
 nonce:         955028
 data:          It was a Sprawl voice and a Sprawl joke.
 previous hash: 00000b0ef65d8235d7c7292dcb0f453af079673a94498ba66b23c26444100ebc
 current hash:  0000026c355a1184e2db1d5c3c68342a0fb55cd23168fea73571d2195004d9bf

Block index:    3
 timestamp:     2022-03-31 16:00:33.458395
 nonce:         1755610
 data:          You are the artiste of the slightly funny deal.
 previous hash: 0000026c355a1184e2db1d5c3c68342a0fb55cd23168fea73571d2195004d9bf
 current hash:  00000e748269c1c9579a9d1bc953e05f0433f721431cf0365ef59062fe6fc975

Block index:    4
 timestamp:     2022-03-31 16:00:40.430512
 nonce:         74439
 data:          You I let work here for entertainment value.
 previous hash: 00000e748269c1c9579a9d1bc953e05f0433f721431cf0365ef59062fe6fc975
 current hash:  00000faa33a917668cd683c0b05d7155480620cf74dddeb429ba7af144a9d842

Block index:    5
 timestamp:     2022-03-31 16:00:40.713924
 nonce:         408200
 data:          She was wearing faded French orbital fatigues and new white sneakers.
 previous hash: 00000faa33a917668cd683c0b05d7155480620cf74dddeb429ba7af144a9d842
 current hash:  000002e0a59b92338507e2dc74837301b096dd11503cc9ec1143cd5c1940628d

Block index:    6
 timestamp:     2022-03-31 16:00:42.290681
 nonce:         3810910
 data:          Iffy, he said, it's all looking very iffy tonight.
 previous hash: 000002e0a59b92338507e2dc74837301b096dd11503cc9ec1143cd5c1940628d
 current hash:  00000cd7a9f5bc9edf100ead4873c323f72ddbc0a6f8b121e062022812bc5533

Block index:    7
 timestamp:     2022-03-31 16:00:57.681075
 nonce:         87276
 data:          The sky above the port was the color of television, tuned to a dead channel.
 previous hash: 00000cd7a9f5bc9edf100ead4873c323f72ddbc0a6f8b121e062022812bc5533
 current hash:  00000a7274f4ca8f2534d542f203d4774dcc64cf761ff4201ce57c1a85e82341
>>>>>>> Stashed changes

```

