# Quick Start

## Prereqs
* An OpenAI API Key: https://platform.openai.com/api-keys
* Install MacAdmins python: https://github.com/macadmins/python/releases
* Install Swift Dialog: https://github.com/swiftDialog/swiftDialog/releases
* Install Munki: https://github.com/macadmins/munki-builds/releases

## Install and setup Python
Create symlink for python3 to managed_python3 so venvs work as expected
```bash
sudo ln -s /usr/local/bin/managed_python3 /usr/local/bin/python3
```
Clone the repo and go into the dir
```bash
git clone https://github.com/natewalck/mdoyvr2024.git
cd mdoyvr2024
```
Create a venv and install all requirements
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Try it out!
Set your OpenAI key as a env var
```
export OPENAI_API_KEY="YOUR_KEY_GOES_HERE"
```
Ask for a swift dialog window with random test, fonts and colors:
```
./macadmin.py "Show me a window with random text, font and colors"
```
You'll see your own version of something like this:
<img width="932" alt="Screenshot 2024-06-02 at 10 23 10" src="https://github.com/natewalck/mdoyvr2024/assets/867868/fe2b8569-2955-4cbc-b807-e02b9c18f0c3">

Or let's get system info and munki version and ask for that in the window:
```
./macadmin.py "Get system info and the munki version then show me the versions in a window"
```
<img width="932" alt="Screenshot 2024-06-02 at 10 24 36" src="https://github.com/natewalck/mdoyvr2024/assets/867868/96e3fe22-4f70-408e-bcbd-15707e10d982">


Ask for it to be more pretty using markdown
```
./macadmin.py "Get system info and the munki version then show me the versions in a window using markdown"
```
<img width="932" alt="Screenshot 2024-06-02 at 10 25 39" src="https://github.com/natewalck/mdoyvr2024/assets/867868/9276d183-fd3c-4ed1-8d5b-921b56352c19">
