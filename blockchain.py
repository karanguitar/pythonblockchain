from block import Block


class Blockchain:
    """
    Blockchain is a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'


def main():

    blockchain = Blockchain()
    blockchain.add_block('karan')
    blockchain.add_block('dhanoya')
    blockchain.add_block('singh')
    print(blockchain)


if __name__ == '__main__':
    main()
