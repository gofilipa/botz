# how to make a twitter bot

## 1. set up twitter API 

### create a twitter dev account

1. Create a new Twitter account for the bot) -
   NOTE: It's important that you Label this account as 'Automated' or
   specify in its Bio that it's a bot: https://x.com/i/flow/signup 
2. Go to the Twitter Dev Account to access the Twitter API:
   https://developer.twitter.com/en/apply-for-access
3. Create a project in your Twitter Dev Portal:
   https://developer.twitter.com/en/portal/projects-and-apps 
4. Create a new App under that Twitter Dev Project.
5. Generate the API key and secret, and the access token key and secret. When they appear on the page, make sure to copy them immediately into a separate file (you can open a plain text file), as you will not be able to see those keys again, but will only generate new (different) ones.

![image showing where to generate keys on twitter dev portal](generate_keys.jpg)

### save your keys to `.env`:

Now, open a new (empty folder) on VS Code. 

In that folder, create a file called `.env`, and copy and paste your keys using the below
format:

```
# Consumer Keys > API Key and Secret
API_KEY=your-API-key
API_SECRET=your-API-secret

# Authentication Tokens > Access Token and Secret
ACCESS_TOKEN=your-access-token
ACCESS_TOKEN_SECRET=your-access-token-secret
```

## 2. configure a python environment

### install python 3.10
*note: these instructions are written for Mac OS; if you are using Windows you will need to look up the equivalent commands*

Python 3.10 is the best version of Python to run for this project. So, we are going to create a
virtual environment just for running Python 3.10. We need to do this to make sure we have the right versions of our python packages for when we deploy them later on github's servers.

We will install Python 3.10 using `homebrew` on the command line. If you do not have `homebrew`, you can download it by [following the instructions here](https://brew.sh/). 

In VS Code, you can open the command line by toggling the icon on the top right or pressing `control` + `shift` + `~` on your keyboard. 

Then, run the following to install python 3.10 and add it to your `$PATH`, so your computer will know where to find the 3.10 version.

```console
brew install python@3.10 
```

Next, we will open an editor to tell our computer where this new version of python is located:

```console
nano ~/.zprofile
```

In the window that pops up (.zprofile file), add the following to the bottom of the page:

```console
alias python3.10=/opt/homebrew/bin/python3.10
```

Save and close the file by pressing control-x and y. 

Now, whenever you invoke the command "python3.10" (as opposed to just "python" or "python3", it will automatically grab Python version 3.10 stored in `/opt/homebrew/bin/python3.10` on your computer.

### create virtual environment
Next, we will create a virtual environment using Python 3.10, activate that environment, and download our packages (`tweepy`, `requests`, and `python-dotenv`). After that, we will save those package versions to a new file called `requirements.txt`.

Run the following commands (skipping the lines commented with #), one line at a time:

```console
# creates a virtual environment
python3.10 -m venv .venv

# activate the environment
source .venv/bin/activate

# installs packages
pip install tweepy, requests, python-dotenv

# save packages to "requirements" file
pip freeze > requirements.txt
```
There should now be a file called `requirements.txt` that has the
verions of all your packages.

Phew, that's done!

## 3. write our tweeting script

Create a new file and call it `tweet.py`. This will be where we handle
the logic of the bot tweeting.

```python
import tweepy
import requests
# allows us to use the operating system and load environment variables 
import os
from dotenv import load_dotenv
# allows the bot to choose one artwork at random
from random import randint

# pulling the keys and secrets from our .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# debugging statement: checking to see we get our correct keys and secrets
print(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# handles authentication
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# also handles authentication 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# debugging statement: making sure we have loaded the variables
print('we loaded the auth variables')

def tweet_a_woman(tweepy_client):
    # debugging: checking to see that the function is running
    print('fetching women from the MET...')

    r1 = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?q=woman")
    parsed = r1.json()

    # grabbing a random work from the top 6000
    number = randint(1, 6000)

    # grabbing data about the individual work
    obj_id = parsed['objectIDs'][number]
    r2 = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
    parsed = r2.json()

    # getting title, artist, gender, url
    if parsed['title'] != '':
       title = f"Title: {parsed['title']}"
    else:
        title = f"Title: Unknown"
    if parsed['artistDisplayName'] != '':
       artist = f"Artist: {parsed['artistDisplayName']}"
    else:
       artist = 'Artist: Unknown'
    if parsed['artistGender'] != '':
        gender = parsed['artistGender']
    else:
        gender = 'Artist Gender: Not marked'
    url = parsed['objectURL']

    # getting image (have to use the other auth)
    image_url = parsed['primaryImage']
    img = requests.get(image_url)
    img_content = img.content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_content)
    media = api.media_upload(filename='image.jpg')
    media_id = media.media_id

    # setting up the tweet text
    tweet_text = f"{title}, {artist}, {gender}. See more: {url}"
    print('tweeting women from the MET...')
    tweepy_client.create_tweet(text=tweet_text, media_ids=[media_id])
 
# calling the function with the auth data as parameter
tweet_a_woman(client)
```

### test your bot

Now is the exciting part! 

Run the following in your command line and check twitter to see the results.

```console
python3.10 tweet.py
```

## 4. automate the bot
As of now, we can tweet whenever we run the `python3.10 tweet.py` command. But we also want our bot to run on its own. The next steps will take care of that by using Github.com, which offers an automation service for us.

### set up git on VS Code

First, if you don't have it already, download `git`, instructions here: https://git-scm.com/downloads. (On a mac, the easiest way is through `homebrew`). 

Second, on VS Code, sign into github on the Accounts icon (if you haven't already)

Third, in the "source control" tab (looks like three dots connected by lines on the left hand side), [initialize a repository](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_initialize-a-repository-in-a-local-folder) on VS Code.

Now your project folder is set up for being tracked by github. 

### create `.gitignore`

Before you add or push any changes, though, you want github to ignore a few files, like our API keys/secrets and our Python software (which we don't need to track with git). 

To do that, we will create a new file, `.gitignore`. In the `.gitignore` file, type then save:

```
__pycache__
.env*
.venv*
```

This tells git not to pay attention to these files and folders. 

### create `actions.yml`

Now we will write the automation logic. Create a new directory, `.github/workflows`. 

Inside that directory, create a
file called `actions.yml`. In that file, paste the following code:

```
name: run tweet.py

on:
  schedule:
#    - cron: '0 * * * *' # at top of every hour
    - cron: '0 0 * * *' # At 00:00 every day
  
  push: 

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

      - name: checkout repo content
        uses: actions/checkout@v2 # checkout the repository content

      - name: setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10' # install the python version needed

      - name: install python packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: run scrupt 
        run: python tweet.py
        env: 
            API_KEY: ${{ secrets.API_KEY }}
            API_SECRET: ${{ secrets.API_SECRET }}
            ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
            ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}
        
  ```

## 5. deploy the bot on github 
### add repostory secret to github.com

Go to your github repository settings (on
`github.com/your_username/your_repo_name`). Once you're there, add
your keys and secrets (all four of them) to your repository under:

```
Settings -> Secrets -> GitHub Actions -> New repository secret
```

### push to github.com
In the "source control" icon (on the left, it has three dots connected by lines), you can add your changes by pressing the plus (+) button, then commit them and push them. This will update your remote repository (which is stored on github.com) with the updated version. 

## 6. 🚀 go bot go!

Go twitter and see your bot go!

## tutorials and helpful links

- [How to Build a Twitter (X) Bot in Python
  tutorial](https://thepythoncode.com/article/make-a-twitter-bot-in-python)
- [Adding secrets to github
  actions](https://www.python-engineer.com/posts/run-python-github-actions/)
- [Automating a Twitter bot with GitHub Actions part 1 of
  3](https://medium.com/@gabrielbelolima/a-step-by-step-tutorial-part-1-3-71a7a8444b0cAutomating)
- [Automating a twitter bot with Github Actions
  repository](https://github.com/gabrielbelolima/ttBot)
- 
