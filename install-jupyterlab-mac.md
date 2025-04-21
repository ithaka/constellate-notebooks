# Installing JupyterLab on your Mac OS X computer

These directions are aimed at helping Mac users install JupyterLab on a Mac OS X computer. Every machine is set up a little differently, but the process should be similar to this. If you run into issues, it may be helpful to check the official [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) and/or work with a chatbot such as ChatGPT or Claude to troubleshoot. This guide installs the following:

* [git](https://git-scm.com/)- command line software for uploading and downloading your files from GitHub
* [Python](https://www.python.org/)- the Python progamming language we will use for writing code
* [JupyterLab](https://jupyter.org/)- a local version that runs on your machine to view and edit your notebooks and other files

# Apple OS X Installation Directions
**NOTE:** If you have an older installation of Python (such as Python 2.7), you may run into issues with symbolic links. See the section at the end of this document for help.

## Install git (Apple Mac OS X)

1. **Open terminal.** Terminal is included in Mac OS X by default Press command (⌘) and spacebar to launch spotlight search. (Alternatively, you can launch spotlight by clicking the magnifying glass in the upper righthand corner of OS X.) Type in "terminal" and hit enter. (You can also launch terminal by navigating to your Applications folder.)
2. **Check if Brew is installed** Type or copy and paste the following code into your terminal, then press *return*.
    ```
    brew --version
    ```
   If you receive a brew version, then it is already installed on your machine. You may skip the next step.
3. **Install Brew if not installed** First we install xcode, copy and paste the following code into your terminal, then press *return*.
    ```
    xcode-select --install
    ```
   This will install Xcode on your machine.
   **NOTE:** If you have trouble getting xcode to install, you can [download it directly from the Apple Developer Tools Site](https://developer.apple.com/downloads/index.action). You will need to create an Apple Developer account.

    To [install Brew](https://brew.sh/), copy and paste the following into your terminal, then press *return*.
    ```   
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
4. **Install git** Type (or copy and paste) the following code into your terminal, then press *return*.
    ```
    brew install git
    ```
5. **Confirm successful installation** Type (or copy and paste) the following code into your terminal then press *return*.
    ```
    git --version
    ```
    You should receive a version number in return such as:
    ```
    git version 2.33.0
    ```

**NOTE:** You may also install git without using the command line by [installing from a binary](https://git-scm.com/download/mac).


## Install Python (Apple Mac OS X)

1. **Install Python from terminal** Assuming you have Brew installed, type (or copy and paste) the following code into your terminal.
    ```
    brew install python3
    ```
    Then press *return*. Your installation should now start.
2. **Confirm successful installation** Type (or copy and paste) the following code into your terminal.
    ```python --version```
    Then press *return*. You should receive a version number in return such as:
    ```python version 3.13.3```

**NOTE:** You may also install Python without using the command line by [installing from a binary](https://www.python.org/downloads/mac-osx/). Only install Python 3; Python 2 is no longer being used.

## Install JupyterLab (Apple Mac OS X)

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in the terminal and pressing *return*. You should receive a version number in return such as:
    ```
    pip 24.1.2 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
    ```
    If you do not receive confirmation, you can also try: ```pip3 --version```.
2. **Install Jupyter Notebook** type the following into your terminal.
    ```
    pip install jupyterlab
    ```
    Then press *return*. Your installation should now start.
3. **Confirm successful installation** type:
    ```
    jupyterlab --version
    ```
    Then press *return*. You should receive a version number in return such as:
    ```
    4.0.2
    ```

Congratulations, you've installed all the necessary software for Apple Mac OS X!

# Opening JupyterLab

In your terminal, type:

```jupyter lab```

A window will open in your browser with JupyterLab running. Note that closing the terminal will also terminate the process running JupyterLab. You can minimize the window, but do not close it until you wish stop using JupyterLab. If you wish to terminate the process, you can select the terminal window and type **control+c** on your keyboard. Type `y` and enter to confirm you want to shutdown the Jupyter server.

# Troubleshooting Symbolic Link Issues

Older versions of software, such as Python may cause symbolic link issues. When you type `python` into the terminal, it may reference the old version of the software instead of the newer version we want. 

## To confirm a symbolic issue exists

1. Open terminal using either Spotlight (the magnifying glass in the upper righthand corner) or navigating to
       **Macintosh HD > Applications > Terminal**
2. Try the following command to verify the old version of Python is being recognized:
    ```
    python --version
    ```
    If an old version of Python, such as Python 2.7, is returned, you'll need to update your symbolic links.

## To fix the symbolic link

1. Verify where your new installation is installed. The following command will search your computer for where there are existing Python installations:
    ```
    ls -l /usr/local/bin/python*
    ```
    The terminal should return a list of places where Python is installed. Find the location for the version of Python you would like to use, such as:
    ```
    /usr/local/bin/python3.13
    ```
2. Finally, we will create the symbolic link. Assuming the link is at `/usr/local/bin/python3.13`, enter:
    ```
    ln -s -f /usr/local/bin/python3.13 /usr/local/bin/python
    ```
3. Close your terminal session and open a new one. Enter:
    ```
    python --version
    ```
   You should receive the correct version in response. 