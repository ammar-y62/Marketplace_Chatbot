from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
FILE_PATH = "C:/Users/amzef/OneDrive/Documents/Inventory.xlsm"

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unanswered_queries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model
class UnansweredQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()


# Route to log unanswered queries
@app.route('/api/log_unanswered', methods=['POST'])
def log_unanswered_query():
    data = request.json
    message = data.get('message', '')
    if message:
        query = UnansweredQuery(message=message)
        db.session.add(query)
        db.session.commit()
        return jsonify({"status": "success", "message": "Logged successfully"}), 200
    return jsonify({"status": "error", "message": "Message is empty"}), 400

# Route to retrieve unanswered queries
@app.route('/api/get_unanswered', methods=['GET'])
def get_unanswered_queries():
    queries = UnansweredQuery.query.all()
    result = [{"id": q.id, "message": q.message, "timestamp": q.timestamp} for q in queries]
    return jsonify(result), 200

# Route to render the dashboard UI
@app.route('/')
def dashboard():
    return render_template('index.html')
# Path to your Excel file

@app.route('/api/respond', methods=['POST'])
def respond():
    """
    API endpoint to respond to client requests with product details based on Item ID.
    """
    data = request.json
    client_message = data.get("message", "").strip()

    try:
        inventory = pd.read_excel(FILE_PATH, sheet_name="Marketplace Orders", engine="openpyxl")
        matching_row = inventory[inventory['Item ID'] == client_message]

        if not matching_row.empty:
            item_data = matching_row.iloc[0].to_dict()
            stock_remaining = int(item_data.get("Stock Remaining", 0))

            response_message = f"Item: {item_data['Product Name']} has {stock_remaining} units remaining."
            if stock_remaining == 0:
                response_message += " Unfortunately, this item is out of stock."

            response_data = {
                "Item ID": client_message,
                "Product Name": item_data["Product Name"],
                "Stock Remaining": stock_remaining,
            }
        else:
            response_message = f"Sorry, no product was found with Item ID '{client_message}'."
            response_data = {}

        return jsonify({"response": response_message, "data": response_data})

    except Exception as e:
        return jsonify({"response": "Error loading inventory data.", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
