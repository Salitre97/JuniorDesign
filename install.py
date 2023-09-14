import os
import sys

def install_requirements():
    # Check the major version of Python in use
    if sys.version_info[0] == 3:
        pip_command = 'pip3'
    else:
        pip_command = 'pip'
    
    os.system(f'{pip_command} install -r requirements.txt')

if __name__ == "__main__":
    install_requirements()