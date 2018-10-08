from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template('index.html')
@app.route("/floppy")
def render_floppy():
    return render_template('floppy.html')

@app.route("/heatsink")
def render_heatsink():
    return render_template('heatsink.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
