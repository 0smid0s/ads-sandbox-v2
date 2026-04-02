"""
System dependency installer for thor_main.py / xvfbwrapper support.
Run once before starting the main script.
"""
import subprocess, sys

def apt_install(*packages):
    subprocess.run(["apt-get", "install", "-y", *packages], check=True)

def pip_install(*packages):
    subprocess.run([sys.executable, "-m", "pip", "install", *packages], check=True)

if __name__ == "__main__":
    print("[~] Installing system dependencies...")
    apt_install("xvfb", "xauth", "libxi6", "libgconf-2-4")

    print("[~] Installing Python dependencies...")
    pip_install("-r", "requirements.txt")

    print("[~] Installing Playwright browsers...")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install-deps"], check=True)

    print("[✓] All dependencies installed. You can now run thor_main.py")
