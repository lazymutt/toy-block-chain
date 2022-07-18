#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
A toy blockchain, now with mining, in 71 lines of code.

Based on:
https://medium.com/@mukeshmishra0381/create-your-own-blockchain-using-python-7c6a117c5f70

Which itself may or may not be heavily borrowed from:
https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54


Cleaned up the example and added proof of work

"""

# MIT License
#
# Copyright (c) 2022 Todd McDaniel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# toy_blockchain.py ############################################################
#
#   A toy blockchain, now with mining, in 71 lines of code.
#
#    1.0.0  2022.04.24      Initial release. tjm
#
#
################################################################################

# Notes: #######################################################################
#
#     Based on:
#     https://medium.com/@mukeshmishra0381/create-your-own-blockchain-using-python-7c6a117c5f70
#
#     Which itself may or may not be heavily borrowed from:
#     https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54
#
#
#     Cleaned up the example and added proof of work
#
################################################################################


import argparse
import datetime
import hashlib


class Block():
    """
    Description of individual block.
    """

    def __init__(self, index, data, previous_hash, pow_level):
        """
        object constructor.
        """
        self.index = index
        self.pow_level = pow_level
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.data = data
        self.previous_hash = previous_hash
        self.currenthash = None
        self.mine_block()

    def hash_block(self):
        """
        create hash of block's data.
        """
        hashed_block = hashlib.sha256()
        hashed_block.update((str(self.index) + str(self.timestamp) + str(self.nonce) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return hashed_block.hexdigest()

    def block_info(self):
        """
        display individual block info.
        """
        print(f"Block index:    {self.index}")
        print(f" timestamp:     {self.timestamp}")
        print(f" nonce:         {self.nonce}")
        print(f" data:          {self.data}")
        print(f" previous hash: {self.previous_hash}")
        print(f" current hash:  {self.currenthash}")
        print()

    def mine_block(self):
        """
        mine block for correct hash.
        """
        pow_string = "0" * self.pow_level
        not_mined = True

        while not_mined:
            self.currenthash = self.hash_block()
            block_header = self.currenthash[:self.pow_level]

            if block_header == pow_string:
                not_mined = False
            else:
                self.nonce += 1


def create_genesis_block(pow_level):
    """
    create initial block.
    """
    return Block(0, "Genesis Block", "0", pow_level)


def next_block(last_block, pow_level, data):
    """
    create new block
    """
    this_index = last_block.index + 1
    this_hash = last_block.currenthash
    return Block(this_index, data, this_hash, pow_level)


def provide_data(this_count):
    """
    Generator function to loop through lines of text.
    """

    lines = '''The sky above the port was the color of television, tuned to a dead channel.
It was a Sprawl voice and a Sprawl joke.
You are the artiste of the slightly funny deal.
You I let work here for entertainment value.
She was wearing faded French orbital fatigues and new white sneakers.
Iffy, he said, it's all looking very iffy tonight.'''.split('\n')

    for line_count in range(this_count):
        sub_count = line_count % len(lines)
        yield lines[sub_count]


def main():
    """
    Create inital (genesis) block and add new blocks.
    """

    parser = argparse.ArgumentParser(description='A toy blockchain with proof-of-work.')
    parser.add_argument('-p', '--pow', type=int, default=3, help='Proof of work level')
    parser.add_argument('-b', '--blocks', type=int, default=3, help='Number of additional blocks to add')

    args = parser.parse_args()

    # create genesis block
    blockchain = [create_genesis_block(args.pow)]
    previous_block = blockchain[0]
    data_source = provide_data(args.blocks)

    # create new blocks
    for _ in range(0, args.blocks):
        block_to_add = next_block(previous_block, args.pow, next(data_source))
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("*")

    # display entire block chain
    for item, _ in enumerate(blockchain):
        blockchain[item].block_info()


if __name__ == '__main__':
    main()
