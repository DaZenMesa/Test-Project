from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/index")
def render_index():
    return render_template('index.html')

@app.route("/heatsink")
def render_heatsink():
    return render_template('heatsink.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
