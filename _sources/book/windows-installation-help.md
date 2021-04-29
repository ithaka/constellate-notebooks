# Common Microsoft Windows 10 Installation Issues

* [Checking if you are an administrator](#check)
* [Resolving Path Issues](#resolve-path)

<a id="check"></a>
## Checking if you are an administrator

1. Open "Control Panel".
2. Navigate to User Accounts.
3. Examine your user account and make sure it says "Administrator" under your account.

*If your account is not an administrator, you will need to contact your IT department in order to get administrative privileges for installing the necessary software.*

<a id="resolve-path"></a>
## Resolving Path Issues

One of the most challenging issues on Microsoft Windows can be resolving Path Issues. A PATH helps Git Bash or the Command Line find the appropriate application to launch. For example, you might be sure you installed Python, Git, Pip, or The Jupyter Notebook, but when you type something like:

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
3. **Check your current existing paths** Click on the Windows Icon and type "env". Click on "Edit the system environment variables". At the bottom of the "Advanced" tab, click on "Environment Variables". The top box will display the Paths that are currently available for your user. Check to make sure there are no variables pointing to old versions of the trouble software. Delete old variables, if necessary.
4. **Create a new path variable** Click "New.." under the user variables. Give it a "variable name" of your choice that will help you remember what the path is for. Instead of typing out the "variable value", it is recommended to choose "Browse File", then navigate to the appropriate file based on your above results from the `where` command. Finally, press "OK".
5. **Check to confirm the program is recognized** Close out of the system properties. Close any Git Bash and Command Prompt windows, then re-open them to confirm the program is now recognized. For example:
    ```
    python --version
    ```
    If the program is not recognized, try changing the path to match a different path listed from the `where` command. 

```{note}
If you know the location of a program from the `where` command, you can navigate to it in the Windows file explorer. (You may need to make invisible files visible by selecting "View" then click on the radio box for "Hidden items". 

If you have Git Bash installed, you can right-click inside the folder with the file (e.g. pip.exe) and select "Git Bash Here". That will open Git Bash in that folder. Then you should be able to launch the executable from that location by typing a "./" before the file. For example, `./pip`. 

This may serve as a momentary workaround but it will not resolve your underlying Path issue since you will need to be in the folder. Of course, you could also type out the whole address when referencing the program but this is tedious experience. 

If you are unable to resolve your path issue, contact your local campus IT for help. 
```

   