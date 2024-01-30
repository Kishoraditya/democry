import json
from moralis import evm_api

def fetch_transaction_details(api_key, transaction_hash):
    params = {
        "chain": "bsc",
        "transaction_hash": transaction_hash,
    }

    result = evm_api.transaction.get_transaction_verbose(api_key=api_key, params=params)
    return result

def main():
    # Your Moralis API key
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjI2NTM2NmJmLTg0MTQtNDlmMi04NjExLTY5MzhlZmRiMGIyMSIsIm9yZ0lkIjoiMzc0NjUyIiwidXNlcklkIjoiMzg1MDE0IiwidHlwZUlkIjoiMDhhZDdiYTYtNmUyNS00NWE3LTgzZTMtZjZkZTFmYTMyODcwIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MDY0NTkzMTgsImV4cCI6NDg2MjIxOTMxOH0.S65bn14Bcx03wAPXIhr4MFwKAVwRg8TX1pZ9bHm8o-c"

    # File containing BSC transaction hashes, one per row
    transaction_hashes_file = "transaction_hashes_bsc.txt"

    # Output text file with the suffix _bsc
    output_file = "transaction_details_bsc.txt"

    # List to store transaction details
    transaction_details_list = []

    # Read BSC transaction hashes from the file
    with open(transaction_hashes_file, "r") as file:
        transaction_hashes = [line.strip() for line in file]

    # Fetch details for each BSC transaction
    for transaction_hash in transaction_hashes:
        transaction_details = fetch_transaction_details(api_key, transaction_hash)
        transaction_details_list.append(transaction_details)

    # Save the details to a text file with the suffix _bsc
    with open(output_file, "w") as text_file:
        json.dump(transaction_details_list, text_file, indent=2)

    print(f"BSC Transaction details saved to {output_file}")

if __name__ == "__main__":
    main()
