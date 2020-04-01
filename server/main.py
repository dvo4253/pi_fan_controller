from flask import Flask

app = Flask(__name__)

@app.route('/stats/cputemp')
def index():
    # Read CPU temperature
    cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
    cpuTemp = float(cpuTempFile.read()) / 1000
    cpuTempFile.close()
    print(cpuTemp)
    return str(cpuTemp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 