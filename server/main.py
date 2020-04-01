from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/stats/cputemp')
def index():
    print(psutil.cpu_temperature())
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 