# Fetches one cat fact from Ninja Cat Fact API 

from flask import Flask, render_template, jsonify
import requests, logging, os


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Route for homapage/index 
@app.route("/")
def home():
    return render_template("index.html")


CAT_API_URL = os.getenv("CAT_API_URL", "https://catfact.ninja/fact")

# API endpoint to fetch (called through JS)
@app.route("/get-fact")
def get_fact():

    # Try and request for cat fact from APi
    try:
        response = requests.get(CAT_API_URL, timeout=5)

        # raises error to go to except block for for failed HTTPS  
        response.raise_for_status()

        # get the json fact as a dictionary 
        info = response.json()

        # return the fact and length of the fact, if none found, fallback
        return jsonify({
            "fact": info.get("fact", "No fact found"), 
            "length": info.get("length", 0)
            })
    except Exception as e:
        logging.error(f"Cat Fact API failed: {e}")
        return jsonify({
            "error":str(e),
            "message": "Opps! Couldn't fetch cat fact! Try again later."

            # HTTPS standard failure error
            }), 500

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
