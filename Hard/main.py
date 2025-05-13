import os
from flask import Flask, request
import shlex
from pathlib import Path
import subprocess

app = Flask(__name__)

# Whitelist of allowed commands
ALLOWED_COMMANDS = {'ls', 'cat'}

# Configure the base directory that can be accessed
BASE_DIR = Path.cwd()

def sanitize_path(file_path):
    """Sanitize and validate the file path to prevent directory traversal"""
    try:
        # Convert to absolute path and resolve any symlinks
        full_path = (BASE_DIR / file_path).resolve()
        # Check if the path is within BASE_DIR
        if not str(full_path).startswith(str(BASE_DIR)):
            return None
        return full_path
    except (ValueError, RuntimeError):
        return None

@app.route("/")
def home():
    return """
    <h1>Welcome to the CTF!</h1>
    <p>Use the <code>/view</code> endpoint to view files on the server.</p>
    <p>Example: <code>/view?file=filename</code></p>
    <p>Use the <code>/execute</code> endpoint to run basic commands.</p>
    <p>Example: <code>/execute?cmd=ls</code> or <code>/execute?cmd=cat filename</code></p>
    """

@app.route("/view")
def view():
    filename = request.args.get("file", "")
    if not filename:
        return "No file specified!", 400
    
    file_path = sanitize_path(filename)
    if not file_path:
        return "Invalid file path!", 400
    
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "File not found!", 404
    except PermissionError:
        return "Permission denied!", 403
    except Exception as e:
        return "An error occurred!", 500

@app.route("/execute")
def execute():
    cmd = request.args.get("cmd", "").strip()
    if not cmd:
        return "No command specified!", 400
    
    try:
        # Split command into arguments safely
        args = shlex.split(cmd)
        if not args:
            return "Invalid command!", 400
        
        # Validate the base command
        base_cmd = args[0]
        if base_cmd not in ALLOWED_COMMANDS:
            return "Command not allowed!", 400
        
        # For 'cat' command, validate the file path
        if base_cmd == 'cat' and len(args) > 1:
            file_path = sanitize_path(args[1])
            if not file_path:
                return "Invalid file path!", 400
            args[1] = str(file_path)
        
        # Execute command in a controlled manner
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=2,  # 2 second timeout
            cwd=str(BASE_DIR)
        )
        
        if result.returncode == 0:
            return f"<pre>{result.stdout}</pre>"
        else:
            return f"Command failed: {result.stderr}", 400
            
    except subprocess.TimeoutExpired:
        return "Command timed out!", 408
    except Exception as e:
        return "An error occurred!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)