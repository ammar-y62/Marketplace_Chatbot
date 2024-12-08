from flask import Flask, request, jsonify  # Flask components for building the API
import pandas as pd  # Pandas for reading and processing Excel files

app = Flask(__name__)  # Initialize the Flask app

# Path to your Excel file stored in OneDrive
FILE_PATH = "C:/Users/amzef/OneDrive/Documents/Inventory.xlsm"

@app.route('/api/respond', methods=['POST'])
def respond():
    """
    API endpoint to respond to client requests with product details based on Item ID.
    """
    # Parse the incoming JSON request
    data = request.json
    client_message = data.get("message", "").strip()  # Get the 'message' field from the request JSON

    # Load the inventory data from the second sheet of the Excel file
    try:
        inventory = pd.read_excel(FILE_PATH, sheet_name="Marketplace Orders", engine="openpyxl")
    except Exception as e:
        # Handle errors while reading the file (e.g., file not found, permission issues)
        return jsonify({
            "response": "Failed to load inventory data. Please check the file path or format.",
            "error": str(e)
        }), 500

    # Search for the row in the inventory where the Item ID matches the client input
    matching_row = inventory[inventory['Item ID'] == client_message]

    if not matching_row.empty:
        # If a match is found, extract the first matching row as a dictionary
        item_data = matching_row.iloc[0].to_dict()

        # Ensure the 'Stock Remaining' value is converted to an integer
        stock_remaining = int(item_data.get("Stock Remaining", 0))

        # Construct a success response with product details
        response_message = f"Item: {item_data['Product Name']} (ID: {client_message}) has {stock_remaining} units remaining."
        if stock_remaining == 0:
            response_message += " Unfortunately, this item is out of stock."

        response_data = {
            "Item ID": client_message,
            "Product Name": item_data["Product Name"],
            "Stock Remaining": stock_remaining
        }
    else:
        # If no match is found, construct an error response
        response_message = f"Sorry, no product was found with Item ID '{client_message}'."
        response_data = {}

    # Return the response as a JSON object
    return jsonify({"response": response_message, "data": response_data})

if __name__ == "__main__":
    # Run the Flask app in debug mode for easy development and testing
    app.run(debug=True)
