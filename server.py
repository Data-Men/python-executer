from flask import Flask, request
import subprocess
import uuid
import os
app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.json
    # code = request.args.get('code')
    print(data)
    print(data["code"])
    try:
        filename=str(uuid.uuid4())+'.py'
        with open(filename,'w') as file:
            file.write(data["code"])
        result = subprocess.check_output('python '+filename, shell=True, stderr=subprocess.STDOUT)
        os.remove(filename)
        return result
    except subprocess.CalledProcessError as e:
        os.remove(filename)
        return f"Error executing command: {e.output}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
