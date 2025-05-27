from flask import Flask, render_template
import webbrowser

import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def open_browser():
    # macOS specific browser call
    try:
        webbrowser.get("macosx").open("http://127.0.0.1:5000/")
    except:
        webbrowser.open("http://127.0.0.1:5000/")  # fallback

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
    
for i in range(10):
    print(i)