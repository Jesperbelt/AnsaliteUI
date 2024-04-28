import salt.client
import salt.config
import salt.loader
import salt.runner
from flask import Flask, render_template, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/minions')
def call_function():
    minions_alived = get_alived()
    return render_template('minions.html', minions=minions_alived)
    #return minion_alived

def get_alived():
    opts = salt.config.master_config('/etc/salt/master')
    runner = salt.runner.RunnerClient(opts)
    minions = runner.cmd('manage.alived', [])
    return minions
