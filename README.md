# ControlPublicacionesML

## Requirements

### 1. Selenium

```
    pip install selenium
```

### 2. Oauth2client
```
    pip install oauth2client
```

### 3. Google Api Python Client
```
    pip install google-api-python-client
```

### 4. Requests
```
    pip install requests
```

### 5. Beautiful Soup
```
    pip install beautifulsoup4
```

### 6. Yaml
```
    pip install pyyaml
```

### 7. Chromedriver

download [here](https://chromedriver.chromium.org/downloads),
it must be inside *juguetimax* directory; the path is the following: ControlPublicacionesML/juguetimax/

### 8. File with credentials to log-in to juguetimax

you must create a file inside *Todas* directory; the path is the following: ControlPublicacionesML/juguetimax/Todas/

the content must be:
```
creds:
  email: enter_here_your_email
  password: enter_here_your_password
```

**use the name creds.yaml or the code will not run. If you do so, your information will be safe; git ignores all .yaml files.** 
**if you choose another name you'll have to modified config.py file inside Todas directory**

### 9. File with google sheets credentials

you must generate your google sheets api credentials. Place the file inside *juguetimax* directory; the path is the following: ControlPublicacionesML/juguetimax/

**it must be a .json file**
**it must be named creds.json or the code will not run properly**
