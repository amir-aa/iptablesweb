from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

# Action page to open or close ports
@app.route('/action', methods=['POST'])
def action():
    port = request.form['port']
    action = request.form['action']
    
    # execute iptables command to open or close port
    if action == 'open':
        command = f'sudo iptables -A INPUT -p tcp --dport {port} -j ACCEPT'
    elif action == 'close':
        command = f'sudo iptables -D INPUT -p tcp --dport {port} -j ACCEPT'
    else:
        return 'Invalid action'
    
 
    output = subprocess.check_output(command, shell=True)
    
 
    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
