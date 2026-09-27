import os
from flask import Flask, jsonify
app = Flask(__name__)
DB_PASSWORD = os.getenv("DB_PASSWORD")
@app.get("/")
def home():
return jsonify(app="InventoryHub", version="2.0.0")
@app.get("/health")
def health():
return jsonify(status="ok"), 200
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=False)