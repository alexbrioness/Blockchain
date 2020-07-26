#This Code looks to simplify the basic idea behind programing a block from the blockchain in python, it is just a simple representation to help with the understanding of the technology

# 1) You will need to import hashlib´s Library to encrypt the blocks data

# 2) You will also want to import the libary datetime to create a date stamp on each block
import hashlib
import datetime

# We will create a class called Block which will contain all the elments necesary for a block in the blockchain this is:
# 1. The Blocknumber
# 2. The previous hash
# 3. The Data which is included in the block
# 4. The timestamp of the block

class Block:

    # In the __init__ function we present the information relevant for each block
    def __init__(self,number,previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
        self.number = number

    # The genesis Block is the inital block in the blockchain therefore this fucntion will only be called to start the blockchain.
    def genesis_block():
        return Block("0","0","0",datetime.datetime.now())

    # The function get hash is the function which will encrypt the blocks information and generate a hash for that block. for more documentation on the hashlib library visit https://docs.python.org/3.7/library/hashlib.html#creating-hash-objects

    def get_hash(self):

        header_bin = (str(self.previous_block_hash) +
                      str(self.data) +
                      str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        return inner_hash
