# Common Apple OS X Installation Issues

## Fixing Symbolic Links to an old version of Python

1. Open terminal using either Spotlight (the magnifying glass in the upper righthand corner) or navigating to
       **Macintosh HD > Applications > Terminal**
2. Try the following command to verify the old version of Python is being recognized:
    ```
    python --version
    ```
    If an old version of Python, such as Python 2.7, is returned, you'll need to update your symbolic links.
3. Verify where your new installation is installed. The following command will search your computer for where there are existing Python installations:
    ```
    ls -l /usr/local/bin/python*
    ```
    The terminal should return a list of places where Python is installed.
    ![Terminal output of locations](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/sym-link-check.png)
   Find the location for the version of Python you would like to use, such as:
    ```
    /usr/local/bin/python3.9
    ```
4. Finally, we will create the symbolic link. Assuming the link is at `/usr/local/bin/python3.9`, enter:
    ```
    ln -s -f /usr/local/bin/python3.9 /usr/local/bin/python
    ```
5. Close your terminal session and open a new one. Enter:
    ```
    python --version
    ```
   You should receive the correct version in response. 