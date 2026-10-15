$ErrorActionPreference = "Stop"

$userDir = $env:USERPROFILE
$jdkDir = "$userDir\AppData\Local\Programs\jdk-17"
$androidDir = "$userDir\AppData\Local\Android\Sdk"
$cmdlineDir = "$androidDir\cmdline-tools\latest"
$tempDir = "$userDir\AppData\Local\Temp\android_cli_install"

Write-Host "=== Setting up Lightweight Android Environment ===" -ForegroundColor Cyan
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

# 1. Download & Extract OpenJDK 17
if (-not (Test-Path "$jdkDir\bin\java.exe")) {
    Write-Host "[1/4] Downloading Microsoft OpenJDK 17..." -ForegroundColor Yellow
    $jdkUrl = "https://download.visualstudio.microsoft.com/download/pr/58dca6c6-c3c9-4daa-8e17-b7d0df501afc/667a0e2c93e1aab8df0707a31c42d190/microsoft-jdk-17.0.12-windows-x64.zip"
    $jdkZip = "$tempDir\jdk17.zip"
    curl.exe -L -s -o $jdkZip $jdkUrl

    Write-Host "[1/4] Extracting OpenJDK 17..." -ForegroundColor Yellow
    $jdkExtract = "$tempDir\jdk_extract"
    New-Item -ItemType Directory -Path $jdkExtract -Force | Out-Null
    tar.exe -xf $jdkZip -C $jdkExtract

    $extractedInner = Get-ChildItem -Path $jdkExtract -Directory | Select-Object -First 1
    New-Item -ItemType Directory -Path (Split-Path $jdkDir -Parent) -Force | Out-Null
    if (Test-Path $jdkDir) { Remove-Item -Path $jdkDir -Recurse -Force }
    Move-Item -Path $extractedInner.FullName -Destination $jdkDir
    Write-Host "OpenJDK 17 installed at: $jdkDir" -ForegroundColor Green
} else {
    Write-Host "[1/4] OpenJDK 17 is already installed at: $jdkDir" -ForegroundColor Green
}

# 2. Download & Extract Android Command-Line Tools
if (-not (Test-Path "$cmdlineDir\bin\sdkmanager.bat")) {
    Write-Host "[2/4] Downloading Google Android Command-Line Tools..." -ForegroundColor Yellow
    $cmdlineUrl = "https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip"
    $cmdlineZip = "$tempDir\cmdline.zip"
    curl.exe -L -s -o $cmdlineZip $cmdlineUrl

    Write-Host "[2/4] Extracting Command-Line Tools..." -ForegroundColor Yellow
    $cmdlineExtract = "$tempDir\cmdline_extract"
    New-Item -ItemType Directory -Path $cmdlineExtract -Force | Out-Null
    tar.exe -xf $cmdlineZip -C $cmdlineExtract

    New-Item -ItemType Directory -Path (Split-Path $cmdlineDir -Parent) -Force | Out-Null
    if (Test-Path $cmdlineDir) { Remove-Item -Path $cmdlineDir -Recurse -Force }
    Move-Item -Path "$cmdlineExtract\cmdline-tools" -Destination $cmdlineDir
    Write-Host "Android Command-line tools installed at: $cmdlineDir" -ForegroundColor Green
} else {
    Write-Host "[2/4] Command-line tools already installed at: $cmdlineDir" -ForegroundColor Green
}

# 3. Environment Variables
Write-Host "[3/4] Configuring persistent Environment Variables..." -ForegroundColor Yellow
[Environment]::SetEnvironmentVariable("JAVA_HOME", $jdkDir, "User")
[Environment]::SetEnvironmentVariable("ANDROID_HOME", $androidDir, "User")
[Environment]::SetEnvironmentVariable("ANDROID_SDK_ROOT", $androidDir, "User")

$env:JAVA_HOME = $jdkDir
$env:ANDROID_HOME = $androidDir
$env:ANDROID_SDK_ROOT = $androidDir
$env:PATH = "$jdkDir\bin;$cmdlineDir\bin;$androidDir\platform-tools;$env:PATH"

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
$pathsToAdd = @("$jdkDir\bin", "$cmdlineDir\bin", "$androidDir\platform-tools")
foreach ($p in $pathsToAdd) {
    if ($userPath -notlike "*$p*") {
        $userPath = "$p;$userPath"
    }
}
[Environment]::SetEnvironmentVariable("Path", $userPath, "User")

# Configure Flutter SDK
$flutterBat = "$userDir\flutter\bin\flutter.bat"
if (Test-Path $flutterBat) {
    & $flutterBat config --android-sdk $androidDir
}

# 4. Install platform-tools, build-tools, and platforms via sdkmanager
Write-Host "[4/4] Installing Android SDK components (platform-tools, build-tools, android-34)..." -ForegroundColor Yellow
$sdkmanager = "$cmdlineDir\bin\sdkmanager.bat"

# Accept licenses
Write-Host "Accepting Android licenses..." -ForegroundColor Yellow
"y`ny`ny`ny`ny`ny`ny`n" | & $sdkmanager --sdk_root=$androidDir --licenses 2>&1 | Out-Null

# Install required packages
& $sdkmanager --sdk_root=$androidDir "platform-tools" "build-tools;34.0.0" "platforms;android-34"

Write-Host "=== Lightweight Android SDK Setup Finished Successfully ===" -ForegroundColor Green
