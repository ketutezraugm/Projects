import hashlib as hasher
import datetime as date
import json
import requests
from flask import Flask, request, jsonify, Response

# Blockchain name
blockchain_name = "Coin Ketut"

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()  # Create hash

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, date.datetime.now(), {"proof-of-work": 1, "transactions": []}, "0")

    @staticmethod
    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = {
            "proof-of-work": last_block.data['proof-of-work'] + 1,
            "transactions": this_nodes_transactions[:]
        }
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

# Initialize blockchain
blockchain = [Block.create_genesis_block()]
previous_block = blockchain[0]

# Flask app
node = Flask(__name__)
this_nodes_transactions = []
peer_nodes = ["http://localhost:5001", "http://localhost:5002"]
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

# New transaction
@node.route('/txion', methods=['POST'])
def transaction():
    new_txion = request.get_json()

    if not new_txion:
        return jsonify({"error": "Invalid JSON data"}), 400
    required_fields = ["from", "to", "amount"]
    for field in required_fields:
        if field not in new_txion:
            return jsonify({"error": f"Missing field: {field}"}), 400

    if not isinstance(new_txion["from"], str) or not isinstance(new_txion["to"], str):
        return jsonify({"error": "Fields 'from' and 'to' must be strings"}), 400
    if not isinstance(new_txion["amount"], (int, float)) or new_txion["amount"] <= 0:
        return jsonify({"error": "'amount' must be a positive number"}), 400

    this_nodes_transactions.append(new_txion)
    print("New transaction")
    print("FROM: {}".format(new_txion['from']))
    print("TO: {}".format(new_txion['to']))
    print("AMOUNT: {}\n".format(new_txion['amount']))

    return jsonify({"message": "Transaction submission successful"}), 201


# Proof of work
def proof_of_work(last_proof):
    if last_proof == 0:
        last_proof = 1
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor

# Mine new block
@node.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain[-1]
    last_proof = last_block.data['proof-of-work']
    proof = proof_of_work(last_proof)
    this_nodes_transactions.append({"from": "network", "to": miner_address, "amount": 1})
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    this_nodes_transactions[:] = []
    mined_block = Block(new_block_index, new_block_timestamp, new_block_data, last_block_hash)
    blockchain.append(mined_block)
    return json.dumps({
        "blockchain_name": blockchain_name,
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash
    }, indent=4) + "\n"

# Get blockchain
@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = []
    for block in blockchain:
        block_data = {
            "index": block.index,
            "timestamp": str(block.timestamp),
            "data": block.data,
            "hash": block.hash
        }
        chain_to_send.append(block_data)
    response_data = {
        "blockchain_name": blockchain_name,
        "chain": chain_to_send
    }
    response = Response(json.dumps(response_data, indent=4), mimetype='application/json')
    return response

# Homepage
@node.route('/', methods=['GET'])
def home():
    return f"Welcome to {blockchain_name} Node! Available endpoints: /txion, /mine, /blocks"

# Run app
if __name__ == "__main__":
    node.run()
