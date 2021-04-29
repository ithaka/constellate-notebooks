# Installing Software on your Local Machine

You have successfully created an account on GitHub, forked our project, and created a website. Now you're ready to start modifying the website to meet your needs for teaching. You can think of GitHub as the place where we will store the latest version of your site. Each time you make an improvement to your site, we will "save" a version to GitHub. Not only will GitHub save your latest changes, but every change you make to your site and lessons! 

In order to make changes to your site, we will download your files to your local machine. On your own machine, you can make changes and test them out before "saving" them back to GitHub and updating your website to make the changes "live." To edit your site on your local machine, you will need some software:

* [git](https://git-scm.com/)- command line software for uploading and downloading your files from GitHub
* [Python](https://www.python.org/)- the Python progamming language we will use for writing code
* [The Jupyter Notebook](https://jupyter.org/)- a local version that runs on your machine to view and edit your notebooks and other files
* [Jupyter Book](https://jupyterbook.org/intro.html)- command line software to convert your notebooks and markdown files into HTML website files

Let's install each of these.
**Note:** The order of these installations does matter. Some of these installation methods will not work if you run them out of order.

## Apple OS X Installations

[Skip to Windows installation Instructions ->](#windows)

### Install git (Apple Mac OS X)

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
    ```{Note}
    If you have trouble getting xcode to install, you can [download it directly from the Apple Developer Tools Site](https://developer.apple.com/downloads/index.action). You will need to create an Apple Developer account.
    ```
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
    git version 2.92.2
    ```

```{note}
You may also install git without using the command line by [installing from a binary](https://git-scm.com/download/mac).
```

### Install Python (Apple Mac OS X)

1. **Install Python from terminal** Assuming you have Brew installed, type (or copy and paste) the following code into your terminal.
    ```
    brew install python3
    ```
    Then press *return*. Your installation should now start.
2. **Confirm successful installation** Type (or copy and paste) the following code into your terminal.
    ```python --version```
    Then press *return*. You should receive a version number in return such as:
    ```python version 3.9```

```{note}
You may also install Python without using the command line by [installing from a binary](https://www.python.org/downloads/mac-osx/). Only install Python 3; Python 2 is no longer being used.
```

### Install The Jupyter Notebook (Apple Mac OS X)

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in the terminal and pressing *return*. You should receive a version number in return such as:
    ```
    pip 20.1.1 from /opt/anaconda3/lib/python3.8/site-packages/pip (python 3.8)
    ```
    If you do not receive confirmation, you can also try: ```pip3 --version```.
2. **Install Jupyter Notebook** type the following into your terminal.
    ```
    pip install notebook
    ```
    Then press *return*. Your installation should now start.
3. **Confirm successful installation** type:
    ```
    jupyter-notebook --version
    ```
Then press *return*. You should receive a version number in return such as:
    ```
    6.0.3
    ```

### Install Jupyter Book (Apple Mac OS X)

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in the terminal and pressing *return*. You should receive a version number in return such as:
    ```
    pip 20.1.1 from /opt/anaconda3/lib/python3.8/site-packages/pip (python 3.8)
    ```
    If you do not receive confirmation, you can also try: ```pip3 --version```.
2. **Install Jupyter Book** type the following into your terminal.
    ```
    pip install jupyter-book
    ```
    Then press *return*. Your installation should now start.
3. **Confirm successful installation** type:
    ```
    jupyter-book --version
    ```
    Then press *return*. You should receive a version number in return such as:
    ```
    Jupyter Book: 0.10.0
    MyST-NB: 0.11.1
    Sphinx Book Theme: 0.0.39
    MyST-Parser: 0.13.3
    Jupyter-Cache: 0.4.2
    NbClient: 0.5.1
    ```
Congratulations, you've installed all the necessary software for Apple Mac OS X!

## Microsoft Windows 10 Installations
<a id="windows"></a>
```{warning}
**Order Matters** The order of these installations matters! Earlier installations are used in order to complete later installations.
**Administrator Access Required** If you are using a laptop supplied by your institution, make sure you have administrative privileges to install software. [How can I check?](windows-installation-help.md)
```

### Install git (Microsoft Windows 10)

1. **Download Git** Go to the [git website](https://git-scm.com/download/win). Download the "64-bit Git for Windows Setup". 
2. **Install Git** For each setting, choose the default. You may, optionally, wish to change the default editor from Vim (an advanced text editor) to something simpler like Notepad. *This is not necessary for our purposes but it may be easier for you if the command line is intimidating.*
3. **Confirm successful installation** Click on the Windows icon in the lower left corner. Type the following:
    ```
    git bash
    ```
    Then press "Enter." This will launch Git Bash, allowing you to use git.
4. **Confirm successful installation** Type (or copy and paste) the following code into Git Bash.
    ```
    git --version
    ```
    Then press *return*. You should receive a version number in return such as:
    ```
    git version 2.31.1.windows.1
    ```

```{note}
Git Bash vs. Command Prompt
For these directions, we assume you are using Git Bash rather than the Windows Command Prompt. It is possible to use Git with the Windows Command Prompt, but some of the commands will be different. To check which one you are using, look in the upper lefthand corner of the window. 

**Git Bash** will say "MINGW64" in the upper lefthand corner of the window.
**Command Prompt** will say "Command Prompt".
```

### Install Python (Microsoft Windows 10)
```{Note}
Jupyter Book has [an incompatibility](https://jupyterbook.org/advanced/windows.html#working-on-windows) with Python 3.8. We will use Python 3.7 for better compatibility.
```

1. **Download Python 3.7.9** from the [Python website](https://www.python.org/downloads/release/python-379/). At the bottom of the page, choose "Windows x86-64 executable installer". 
2. **Start the installation** by double-clicking on the executable file. 
    ```{warning}
    Make sure to select "Add Python 3.7 to PATH" before choosing "Install Now."
    ```
3. **Confirm successful installation**
    ```{note}
    If you have a Git Bash window already open, close it and then open a new one.
    ```
   Type: 
   ```
   python --version
   ``` 
   then press *Enter*. You should receive a response like: 
   ```
   Python 3.7.9
   ```

### Install The Jupyter Notebook (Microsoft Windows 10)

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in Git Bash and pressing *Enter*. You should receive a version number in return such as:
    ```
    pip 20.1.1 from c:\users\username\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
    ```
    If you do not receive confirmation, you can also try: 
    ```
    pip3 --version
    ```
2. **Install Jupyter Notebook** type the following into your terminal.
    ```
    pip install notebook
    ```
Then press *return*. Your installation should now start.
3. **Confirm successful installation** type:
    ```
    jupyter-notebook --version
    ```
Then press *return*. You should receive a version number in return such as:
    ```
    6.3.0
    ```

### Install Jupyter Book (Microsoft Windows 10)

```{note}
Jupyter Book has [compatibility issues with Python 3.8](https://jupyterbook.org/advanced/windows.html#working-on-windows). Please make sure you have installed Python 3.7.
```

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in Git Bash and pressing *Enter*. You should receive a version number in return such as:
    ```
    pip 20.1.1 from c:\users\username\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
    ```
    If you do not receive confirmation, you can also try: ```pip3 --version```.
2. **Install Jupyter Book** type the following into your terminal.
    ```
    pip install jupyter-book
    ```
    Then press *Enter*. Your installation should now start.
3. **Confirm successful installation** type:
    ```
    jupyter-book --version
    ```
    Then press *Enter*. You should receive a version number in return such as:
    ```
    Jupyter Book: 0.10.2
    MyST-NB: 0.12.3
    Sphinx Book Theme: 0.1.0
    MyST-Parser: 0.13.7
    Jupyter-Cache: 0.4.2
    NbClient: 0.5.3
    ```
Congratulations, you've installed all the necessary software for Microsoft Windows 10!
