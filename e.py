import subprocess
import os

def run_command(command, shell=True):
    try:
        print(f"Menjalankan: {command}")
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Gagal menjalankan perintah: {command}")
        print(f"Error: {e}")

def main():
    # Update & upgrade sistem
    run_command("apt update")
    run_command("apt upgrade -y")

    # Download & install Google Chrome
    run_command("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    run_command("dpkg -i google-chrome-stable_current_amd64.deb")
    run_command("apt --fix-broken install -y")
    run_command("dpkg -i google-chrome-stable_current_amd64.deb")

    # Download & setup ChromeDriver
    run_command("wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.68/linux64/chromedriver-linux64.zip")
    run_command("unzip chromedriver-linux64.zip")
    run_command("chmod +x chromedriver-linux64/chromedriver")
    run_command("mv chromedriver-linux64/chromedriver /usr/local/bin/")

    # Install Selenium dan update pip
    run_command("pip install selenium --break-system-packages --ignore-installed")
    run_command("pip install --upgrade pip")

    # Download script Python dan jalankan
    run_command("wget -O ipay.py https://pastebin.com/raw/D2Jj1BBZ")
    run_command("python ipay.py")

if __name__ == "__main__":
    main()