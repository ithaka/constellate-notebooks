# Installing JupyterLab on your Windows 10 computer

These directions are aimed at helping Windows users install JupyterLab on a Windows 10 computer. Every machine is set up a little differently, but the process should be similar to this. If you run into issues, it may be helpful to check the official [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) and/or work with a chatbot such as ChatGPT or Claude to troubleshoot. This guide installs the following:

* [git](https://git-scm.com/)- command line software for uploading and downloading your files from GitHub
* [Python](https://www.python.org/)- the Python progamming language we will use for writing code
* [JupyterLab](https://jupyter.org/)- a local version that runs on your machine to view and edit your notebooks and other files

# Windows 10 Installation Directions

**NOTE:** If you have older installations of software, that may cause path issues in Windows. See the final section for guidance on resolving path issues.

## Confirm you have administrator access

If you are using a laptop supplied by your institution, make sure you have administrative privileges to install software. To check if you are an administrator:

1. Open "Control Panel".
2. Navigate to User Accounts.
3. Examine your user account and make sure it says "Administrator" under your account.

*If your account is not an administrator, you will need to contact your IT department in order to get administrative privileges for installing the necessary software.*

## Install git (Microsoft Windows 10)

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
    git version 2.49.windows.1
    ```

**NOTE:** Git Bash and Command Prompt are different forms of the command line. For these directions, we assume you are using Git Bash rather than the Windows Command Prompt. It is possible to use Git with the Windows Command Prompt, but some of the commands will be different. To check which one you are using, look in the upper lefthand corner of the window. 

**Git Bash** will say "MINGW64" in the upper lefthand corner of the window.
**Command Prompt** will say "Command Prompt".

## Install Python (Microsoft Windows 10)

1. **Download Python** from the [Python website](https://www.python.org/downloads/). At the bottom of the page version page, choose "Windows installer 64-bit". 
2. **Start the installation** by double-clicking on the executable file. 
    **NOTE:** Make sure to select "Add Python 3.13 to PATH" before choosing "Install Now." If you do not choose this, your Python install may not be recognized! This means you will have to uninstall and re-install Python!
3. **Confirm successful installation**
    **NOTE:** If you have a Git Bash window already open, close it and then open a new one.
   Type: 
   ```
   python --version
   ``` 
   then press *Enter*. You should receive a response like: 
   ```
   Python 3.13.3
   ```

## Install The JupyterLab (Microsoft Windows 10)

1. **Check if "pip" is installed** When you installed Python, it should have also installed "pip." You can check to see if you have pip by typing:
    ```
    pip --version
    ```
    in Git Bash and pressing *Enter*. You should receive a version number in return such as:
    ```
    pip 25.0.1 from c:\users\username\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
    ```
    If you do not receive confirmation, you can also try: 
    ```
    pip3 --version
    ```
2. **Install JupyterLab** type the following into your terminal.
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
    4.4.0
    ```

Congratulations, you've installed all the necessary software for Microsoft Windows 10!

# Opening JupyterLab

In git bash, type:

```jupyter lab```

A window will open in your browser with JupyterLab running. Note that closing git bash will also terminate the process running JupyterLab. You can minimize the window, but do not close it until you wish stop using JupyterLab. If you wish to terminate the process in git bash, you can select the git bash window and type **control+c** on your keyboard. Type `y` and enter to confirm you want to shutdown the Jupyter server.

# Troubleshooting Path Issues

If you have successfully installed an application but it is not recognized in Git Bash, you may have a path issue. One of the most challenging issues on Microsoft Windows can be resolving Path Issues. A PATH helps Git Bash or the Command Line find the appropriate application to launch. For example, you might be sure you installed Python, Git, Pip, and/or The JupyterLab, but when you type something like:

```
pip --version
```

Pip is not found on your machine. This could give an error saying the application was not found or it may, puzzlingly, return nothing at all. When the command returns nothing, that may be an indication that you have an old Path that needs to be deleted. This could be caused by something like an old installation of Python.

To attempt to fix the path issue, there are a couple of recommended troubleshooting steps.
1. **Re-Install Python** If your path issue is with Python or Pip, make sure you selected "Add Python 3.7 to PATH" before choosing "Install Now" in the Python installer. You may want to use "Add/Remove Programs" to remove Python and Python Launcher then try re-installing to make sure to select that option. It is very easy to overlook.
2. **Find the application location** Open Git Bash (or the command line) in order to search for the particular application that is missing using the `where` command. For example:
    ```
    where python
    ```
    If the program has been installed on the computer, it will return a list of locations, such as:
    ```
    C:\Users\YourUserName\AppData\Local\Programs\Python\Python37\python.exe
    C:\Users\YourUserName\AppData\Local\Microsoft\WindowsApps\python.exe
   ```
    One of these is the location that we need to add to your path.
3. **Check your current existing paths** Click on the Windows Icon and type "env". Click on "Edit the system environment variables". 
    At the bottom of the "Advanced" tab, click on "Environment Variables". The top box will display the Paths that are currently available for your user. Check to make sure there are no variables pointing to old versions of the trouble software. Delete old variables, if necessary.
4. **Create a new path variable** Click "New.." under the user variables. Give it a "variable name" of your choice that will help you remember what the path is for. Instead of typing out the "variable value", it is recommended to choose "Browse File", then navigate to the appropriate file based on your above results from the `where` command. Finally, press "OK".
5. **Check to confirm the program is recognized** Close out of the system properties. Close any Git Bash and Command Prompt windows, then re-open them to confirm the program is now recognized. For example:
    ```
    python --version
    ```
    If the program is not recognized, try changing the path to match a different path listed from the `where` command. 

**NOTE:** If you know the location of a program from the `where` command, you can navigate to it in the Windows file explorer. (You may need to make invisible files visible by selecting "View" then click on the radio box for "Hidden items". 

If you have Git Bash installed, you can right-click inside the folder with the file (e.g. pip.exe) and select "Git Bash Here". That will open Git Bash in that folder. Then you should be able to launch the executable from that location by typing a "./" before the file. For example, `./pip`. 

This may serve as a momentary workaround but it will not resolve your underlying Path issue since you will need to be in the folder. Of course, you could also type out the whole address when referencing the program but this becomes a tedious experience. 

If you are unable to resolve your path issue, contact your local campus IT for help. 