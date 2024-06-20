import subprocess
import sys
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    required_packages = [
        "requests",
        "beautifulsoup4"
    ]
    
    for package in required_packages:
        install(package)

    print("Setup Complete")
    time.sleep(2)

if __name__ == "__main__":
    main()
