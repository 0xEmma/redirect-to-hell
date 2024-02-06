from flask import Flask, redirect
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
URL  = str(os.environ.get('URL', "https://ash-speed.hetzner.com/10GB.bin"))
file = "/app/data/stats.txt"
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/stats')
def show_stats():
    with open(file, 'r') as files:
        return files.read()
@app.route('/wp-login.php')
def wp_login():
    stats = open(file, "r")
    number = int(stats.read().split(" ")[1]) + 1
    stats.close()
    stats = open(file, "w")
    stats.write(f"wp_login {number}")
    stats.close()
    return redirect(URL)



Flask.run(app, host="0.0.0.0", port=port)