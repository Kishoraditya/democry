import json
import csv
from datetime import datetime

def analyze_transaction_details(details, eth_to_usd_rate=2700):
    transaction_hash = details["hash"]
    to_address = details["to_address"]
    from_address = details["from_address"]

    decoded_call = details.get("decoded_call", {})
    if decoded_call is None:
        decoded_call = {}

    token_type = decoded_call.get("label", "Unknown")

    value = details.get("value", 0)
    token_value = eth_to_usd_rate * float(value) / 1e18  # Convert from Wei to ETH
    token_amount_usd = token_value  # Assuming ETH value is equal to USD

    transaction_time = datetime.strptime(details["block_timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
    transaction_type = "Internal" if "internal_transactions" in details else "External"
    gas_consumed = int(details["gas"])

    return [
        transaction_hash,
        to_address,
        from_address,
        token_type,
        token_value,
        token_amount_usd,
        transaction_time,
        transaction_type,
        gas_consumed
    ]

def main():
    # Input JSON file
    input_json_file = "transaction_details.json"

    # Output CSV file
    output_csv_file = "transaction_analysis.csv"

    # ETH to USD conversion rate
    eth_to_usd_rate = 2700

    # Read transaction details from JSON file
    with open(input_json_file, "r") as json_file:
        transaction_details_list = json.load(json_file)

    # Analyze each transaction and store the results
    analyzed_transactions = []
    for transaction_details in transaction_details_list:
        analyzed_transaction = analyze_transaction_details(transaction_details, eth_to_usd_rate)
        analyzed_transactions.append(analyzed_transaction)

    # Save the results to a CSV file
    with open(output_csv_file, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            "Transaction Hash",
            "To Address",
            "From Address",
            "Token Type",
            "Token Value (ETH)",
            "Token Amount (USD)",
            "Transaction Time",
            "Transaction Type",
            "Gas Consumed"
        ])
        csv_writer.writerows(analyzed_transactions)

    print(f"Analysis results saved to {output_csv_file}")

if __name__ == "__main__":
    main()
