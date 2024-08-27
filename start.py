import os
import sys
import subprocess
import venv

import time

def start_ollama_server():
    """Start the Ollama server in the background."""
    try:
        # Start the Ollama server in the background
        server_process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("Ollama server started with PID:", server_process.pid)
        return server_process
    except Exception as e:
        print(f"Failed to start Ollama server: {e}")
        return None

def create_venv(venv_path):
    """Create a virtual environment at the specified path."""
    venv.create(venv_path, with_pip=True)
    print(f"Created virtual environment at {venv_path}")

def activate_venv(venv_path):
    """Activate the virtual environment."""
    if os.name == "nt":  # Windows
        activate_script = os.path.join(venv_path, "Scripts", "activate")
    else:  # Unix or MacOS
        activate_script = os.path.join(venv_path, "bin", "activate")
    
    if not os.path.exists(activate_script):
        raise FileNotFoundError(f"Activation script not found: {activate_script}")

    # Activate the environment
    print(f"Activating virtual environment from {activate_script}")
    activate_command = f". {activate_script}" if os.name != "nt" else activate_script
    os.system(activate_command)

def install_dependencies(venv_path):
    """Install dependencies from requirements.txt into the virtual environment."""
    pip_executable = os.path.join(venv_path, "bin", "pip") if os.name != "nt" else os.path.join(venv_path, "Scripts", "pip")
    subprocess.check_call([pip_executable, "install", "-r", "requirements.txt"])

def main(include_ollama=True):

    if include_ollama:
        # Start the Ollama server
        print("Starting Ollama server...")
        server_process = start_ollama_server()
        if server_process is None:
            print("Failed to start Ollama server. Exiting...")
            sys.exit(1)
    else:
        print("Skipping Ollama initialization")

    # Define the path to the virtual environment
    venv_path = os.path.join(os.getcwd(), "venv")

    # Check if the virtual environment already exists
    if not os.path.exists(venv_path):
        print("Virtual environment not found, creating...")
        create_venv(venv_path)
        install_dependencies(venv_path)
    else:
        print("Virtual environment already exists.")


    # Run the main application logic
    # For example, you might import and run your main application module here:
    # from src.main import main as run_app
    # run_app()
    print("Running the application...", "\n")
    application_process = subprocess.Popen([os.path.join(venv_path, "bin", "python"), "ui.py"])

    time.sleep(3)
    print("--------------------------------------------------")
    input("Press Enter to exit...")

    if include_ollama:
        # Terminate the Ollama server
        print("Terminating Ollama server...")
        server_process.terminate()

    # Terminate the application
    print("Terminating the application...")
    application_process.terminate()
    print("--------------------------------------------------")
    print("Shutdown complete.")

if __name__ == "__main__":
    main()
