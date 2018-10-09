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

@app.route("/harddrive")
def render_hardrive():
    return render_template('harddrive.html')

@app.route("/motherboard")
def render_motherboard():
    return render_template('motherboard.html')

@app.route("/opticaldrive")
def render_opticaldrive():
    return render_template('opticaldrive.html')

@app.route("/powersupply")
def render_powersupply():
    return render_template('powersupply.html')

@app.route("/ram")
def render_ram():
    return render_template('ram.html')

@app.route("/systemfan")
def render_systemfan():
    return render_template('systemfan.html')

@app.route("/cpu")
def render_cpu():
    return render_template('cpu.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
