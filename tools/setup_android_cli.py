import os
import sys
import zipfile
import urllib.request
import subprocess
import shutil

USER_DIR = os.path.expanduser("~")
JDK_DIR = os.path.join(USER_DIR, "AppData", "Local", "Programs", "jdk-17")
ANDROID_DIR = os.path.join(USER_DIR, "AppData", "Local", "Android", "Sdk")
CMDLINE_DIR = os.path.join(ANDROID_DIR, "cmdline-tools", "latest")
TEMP_DIR = os.path.join(USER_DIR, "AppData", "Local", "Temp", "android_setup")

JDK_URL = "https://aka.ms/download-jdk/microsoft-jdk-17.0.12-windows-x64.zip"
CMDLINE_URL = "https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip"

def download_file(url, target_path):
    print(f"Downloading {url} ...")
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    urllib.request.urlretrieve(url, target_path)
    print(f"Saved to {target_path} ({os.path.getsize(target_path) / (1024*1024):.1f} MB)")

def setup_jdk():
    java_exe = os.path.join(JDK_DIR, "bin", "java.exe")
    if os.path.exists(java_exe):
        print(f"JDK already present at {JDK_DIR}")
        return JDK_DIR
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    zip_path = os.path.join(TEMP_DIR, "jdk17.zip")
    download_file(JDK_URL, zip_path)
    
    print("Extracting JDK...")
    extract_temp = os.path.join(TEMP_DIR, "jdk_extracted")
    os.makedirs(extract_temp, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_temp)
    
    # Locate the inner folder (e.g., jdk-17.0.12+7)
    subdirs = [os.path.join(extract_temp, d) for d in os.listdir(extract_temp) if os.path.isdir(os.path.join(extract_temp, d))]
    source_dir = subdirs[0] if subdirs else extract_temp
    
    if os.path.exists(JDK_DIR):
        shutil.rmtree(JDK_DIR)
    shutil.move(source_dir, JDK_DIR)
    print(f"JDK successfully installed at {JDK_DIR}")
    return JDK_DIR

def setup_cmdline_tools():
    sdkmanager_bat = os.path.join(CMDLINE_DIR, "bin", "sdkmanager.bat")
    if os.path.exists(sdkmanager_bat):
        print(f"Command-line tools already present at {CMDLINE_DIR}")
        return CMDLINE_DIR
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    zip_path = os.path.join(TEMP_DIR, "cmdline-tools.zip")
    download_file(CMDLINE_URL, zip_path)
    
    print("Extracting cmdline-tools...")
    extract_temp = os.path.join(TEMP_DIR, "cmdline_extracted")
    os.makedirs(extract_temp, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_temp)
    
    # Inside the zip is a folder named 'cmdline-tools'
    inner_dir = os.path.join(extract_temp, "cmdline-tools")
    if not os.path.exists(inner_dir):
        inner_dir = extract_temp
    
    os.makedirs(os.path.dirname(CMDLINE_DIR), exist_ok=True)
    if os.path.exists(CMDLINE_DIR):
        shutil.rmtree(CMDLINE_DIR)
    shutil.move(inner_dir, CMDLINE_DIR)
    print(f"Command-line tools installed at {CMDLINE_DIR}")
    return CMDLINE_DIR

def set_env_vars():
    print("Setting Windows user environment variables...")
    # Set JAVA_HOME, ANDROID_HOME, ANDROID_SDK_ROOT
    subprocess.run(["setx", "JAVA_HOME", JDK_DIR], check=True)
    subprocess.run(["setx", "ANDROID_HOME", ANDROID_DIR], check=True)
    subprocess.run(["setx", "ANDROID_SDK_ROOT", ANDROID_DIR], check=True)
    
    # Configure flutter directly
    flutter_bat = os.path.join(USER_DIR, "flutter", "bin", "flutter.bat")
    if os.path.exists(flutter_bat):
        subprocess.run([flutter_bat, "config", "--android-sdk", ANDROID_DIR], check=True)
        print("Flutter android-sdk path configured.")

if __name__ == "__main__":
    print("=== Standalone Lightweight Android Setup ===")
    jdk_path = setup_jdk()
    cmdline_path = setup_cmdline_tools()
    set_env_vars()
    print("Setup completed successfully.")
