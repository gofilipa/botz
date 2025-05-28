# introduction to git

The purpose of `git` (and VCS generally) is to track changes so that
one can more easily manange their own projects and collaborate with
others. Version control means we can keep track of who does what in a
project, and revert files to previous forms (this is super useful in
software development, where minor changes in code can break an entire
app!).

## Step 1: Make sure you have Git installed on you machine.

To use git, you need to first install the software. [Read here to
install
Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Step 2: Set up your account on Github (you likely already did this)

You need to set up an account on github, following the steps in the
previous lesson.

## Step 3: Configure user info via Command Line

Then, you need to configure your user information locally. Copy and
paste the following into your terminal or command line application 

```console
git config --global user.name "YOUR_USERNAME"
git config --global user.email "im_satoshi@musk.com"
```

## Step 4: Authenticating

For Mac users, follow these instructions: https://dev.to/shafia/support-for-password-authentication-was-removed-please-use-a-personal-access-token-instead-4nbk

For Windows users, follow these instructions: https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed 

## Step 5: Clone a repo

Get the link to your repo from Github.com. Go to your repo homepage,
press the green "Code" button, and copy the `https` URL there (which
is the URL to your repo).

Then, go to your terminal and use the clone command to cone the
repo. Make sure you're on your desktop or wherever you want the
project file to exist on your computer.

```console
cd ~/Desktop
git clone https://github.com/your_user_name/your_repo_name.git
```
## Step 6: Make some changes!

Do some work on the repo.

## Step 7: Adding & committing

When you're done working, you need to add and commit your changes. In
the quotes, you can include a short message summarizing your
changes. This creates a very useful log of every commit. 

```console
git add .
git commit -m 'write a short message about your changes here'
```

## Step 8: Push your changes All the changes we made in the file are
updated in the local repository. Now to update the changes to the
remote repo, which exists on Github.com:

```console
git push
```

For more on git:
https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/