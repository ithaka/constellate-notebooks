# Clone your repository to your local machine
Now that we have all of our software installed, we will configure *git* on our local machine to interact with *GitHub*. Our first goal is to download the materials in your *GitHub* repository to your local machine. 

When we have the files on our local machine, we can then make changes using an editor of our choice. We recommend using *The Jupyter Notebook* to edit *.ipynb* files, so you can see exactly how they will look online.

```{note}
 There are a variety of other editors that will open and edit *.ipynb* files, from the most basic tools like *TextEdit* (OS X) or *Notepad* (Windows 10) to advanced, fully-featured Integrated Development Environments (IDEs) such as *Visual Studio* and *PyCharm*. For our purposes, simple editors will be enough but you may eventually want to investigate other options that have many helpful features.
```
## Navigating folders in terminal and Git Bash
Both the terminal (Apple OS X) and Git Bash (Microsoft Windows 10) use unix for navigating and working with local folders and files. We will use some basic commands to move around in your local folders and files. 

```{note}
Our goal is mainly to be able to navigate the file system, not to do any advanced tasks with Unix commands. If you would like to learn more unix commands, we recommend:

* [Command Line lesson](https://github.com/DHRI-Curriculum/command-line/blob/v2.0/sections/01-what-is-the-command-line.md) from the [Digital Humanities Research Institute curriculum](https://www.dhinstitutes.org/curricula/)
* [The Unix Shell lesson from Software Carpentry](http://swcarpentry.github.io/shell-novice/) from [Software Carpentry](https://software-carpentry.org/)
* [Introduction to the Bash Command Line](https://programminghistorian.org/en/lessons/intro-to-bash) from [The Programming Historian](https://programminghistorian.org/)
```
We will learn three unix commands for navigating folders:

|Unix command|English meaning|purpose|
|---|---|---|
|`pwd`|Present Working Directory |outputs your current location on your computer file system|
|`ls`|list|outputs the files and directories in your current location|
|`ls -a`|list all|the addition of the -a flag includes output of hidden files and directories which begin with a period|
|`cd folderName/`|change directory|moves the user down into the folderName directory|
|`cd ..`|change directory| moves the user up one directory|
|`cd ~`|change directory|move to user's home directory|

```{note}
On *Apple OS X*, the user's home directory is `/Users/UserName`.
On *Microsoft Windows 10*, the user's home directory is usually `/c/Users/UserName`
```

Open either terminal and Git Bash to try out each of these commands. Explore your file system for practice. Finally, navigate to the directory where you would like to make a copy of your website on your local machine.

```{note}
When you are navigating to a particular file or directory using `cd`, you usually do not need to type out the whole name. Simply type out a few letters then press *tab*. If there is a single match in the current directory, the full name will be completed automatically! If the name is not auto-completed, press tab twice to show all matching results for the letters typed so far. You can then type a few more letters to make your selection clear before tabbing one more time to automatically complete the name.
```

## Setting up git on your local machine
We will use the following git commands to set up git. We will only use them a single time. They are important for setup, but you will not use them again unless you set up git on another machine or need to re-install git.

|git setup commands|English meaning|purpose|
|---|---|---|
|`git config --global user.name "Judith Cohen"`|Configure the global git user with this name| Sets the user name in git. *Only needs to be run once.*|
|`git config --global user.email "username@gmail.com"`|Configure the global git user with this email address|  Sets the user email for git. Use the same email address as your GitHub account. *Only needs to be run once.*|

## Cloning your repository
The `clone` command helps us copy a repository from GitHub to our local machine. First, however, we need to grab an address from GitHub to clone our repository. Open your web browser and log into GitHub. Click on your repository. Then click on the large, green "Code" button. Finally click on the clipboard to copy the "HTTPS" address. 
![the clone address](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/clone-address.png)
The address will look like `https://github.com/yourGitHubUserName/yourRepoName.git`

Return to your terminal or Git Bash. Use the `pwd` command to confirm you are in the directory where you would like to make a local copy of your repository. If everything looks good, run `git clone` followed by the address you copied. It should look something like:
```
git clone https://github.com/yourGitHubUserName/yourRepoName.git
```
```{warning}
The familiar shortcut for paste in Windows (Ctrl + V) does not work in Git Bash. To paste in Git Bash, you can use the keyboard key "Insert" or right-click then select "paste".
```
Congratulations! You've copied your repository to your local machine. Now let's learn how to make changes.