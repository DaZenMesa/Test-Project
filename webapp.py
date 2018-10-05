from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/index")
def render_index():
    return render_template('index.html')

@app.route("/heatsink")
def render_heatsink():
    return render_template('heatsink.html')

@app.route("/motherboard")
def render_motherboard():
    return render_template('motherboard.html')

@app.route("cpu")
def render_cpu():
    return render_template('cpu.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
