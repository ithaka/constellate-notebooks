# Make local changes
Now that you have a local copy of your site, you can make changes and improve it. You can use two different kinds of editors to make improvements. For improvements to the website configuration, you can use a simple text editor. For improvements to the lessons, we will use *The Jupyter Notebook*.

## Making improvements to the website configuration

The [full documentation for Jupyter Book](https://jupyterbook.org/intro.html) contains many more details, but we will focus on two main files:
* `config.yml`- The general site configuration file which gives us lots of options for how the site will look and function.
* `toc.yml`- The file that configures the Table of Contents for our website.

Both of these files are simple text files, so you do not need the command line to change them. You can simply open them with a plain text editor like *TextEdit* (Apple OS X) or *Notepad* (Microsoft Windows 10). 
```{note}
If you would like to try a more advanced editor, you might check out [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio](https://visualstudio.microsoft.com/). Both have free versions that work on Apple OS X and Microsoft Windows 10.
```

## Editing `config.yml`

Each setting in the `config.yml` file has description in form of a comment, but we also recommend taking a look at [the Jupyter Book Documentation page](https://jupyterbook.org/customize/config.html). The basic settings are fairly easy to change, but there's also a tremendous amount of flexibility for more powerful transformations. Here are a few basic items you're likely to want to change:

|Setting|Use|
|---|---|
|title|The title of the book. Will be placed in the left navbar.\
|author|The author of the book|
|logo|The path to a logo for your book|
|repository: url| The github URL to your book's repository|

```{warning}
If you don't change the repository URL, your notebook lessons will not launch correctly. Your repository URL will look like:
`https://github.com/yourGitHubUserName/yourRepositoryName`
```
## Editing `toc.yml`

This file edits the table of contents found in the lefthand navigation of the site. We recommend taking a look at the [Jupyter Book documentation for the table of contents](https://jupyterbook.org/customize/toc.html). You have an option for organizing your table of contents:

* Chapters
* Chapters broken up into parts

The original site table of contents is composed of chapters broken up into parts. Here are a few things to note when making changes:

* The Jupyter Book builder is exacting about spacing for the table of contents file. It is essential to have the correct number of tabs for your file names and chapters.
* When you specify the location of a chapter file, you do not need to add the file extension, such as .md or .ipynb
* We recommend making only one significant change to your table of contents at a time. If the build fails, it will be easy to change back to a working version.

## Making Changes to the Website Content

The main content of your site is composed of two kinds of files:
* Jupyter Notebook Files (.ipynb)- These are notebook files that we can view and change with Jupyter Notebook. 
* Markdown Files (.md)- These are simple text files with a little markdown for styling and adding things like links, images, and other explanatory content. They can be edited in *The Jupyter Notebook*, a simple text editor, or a more advanced editor. The advantage of *The Jupyter Notebook* or a more advanced editor is that either will give you a preview of your Markdown.

## Editing with The Jupyter Notebook

*The Jupyter Notebook* is launched from the command line. Open your command line, either Git Bash or Terminal, and navigate to the repository using the `cd` command. When you are in your repository, run:
```
jupyter notebook
```
This will launch *The Jupyter Notebook* in your browser. You will then be able to open any notebook (.ipynb) or markdown (.md) files to edit. Your command line, either Git Bash or Terminal, will be running a local server for Jupyter Notebook, so do not quit the command line or *The Jupyter Notebook* will also stop. Simply minimize the window out of the way.

As you modify each notebook or markdown file, you will need to save changes. On OS X, use (⌘ + s). On Windows 10, use (Ctrl + s). When you're finished making changes, save, close *The Jupyter Notebook* tab, then close the command line. 

```{note}
If you are working on a Jupyter Notebook, we recommend clearing all code outputs before saving. That will essentially reset the notebook for the next user. If you do not clear the outputs, any existing outputs will be visible for the next user. This can be confusing!
```
![clearing all outputs](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/clear_output.gif)

## Previewing your website changes

If you would like to preview what your website will look like, you need to use *Jupyter Book* to build the site first. Essentially, this takes all the information from your configuration file, your table of contents file, your markdown files, and your notebook files to create a website. We are converting all of content files into HTML files.

Open your command line, navigate to your repository, then run the *Jupyter Book* build command:

```
jupyter-book build .
```
The period here specifies to build the book in the present working directory. If you were in a different directly, you could specify the location of the repository instead of using a period.

Assuming there are no errors and your book builds successfully, the HTML files will be deposited in `_build/html`. To preview your website you can open the file main index through your file explorer by navigating to `_build/html/index.html`. Alternatively, you could copy the file location link that posts at the end of the successful build and paste it into a web browser.

![preview of successful output](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/jupyter-book-output.png)

```{note}
As you make changes, you may need to build your website many times to see previews. Rather than retyping the `jupyter-book build .` command, you can simply press the ↑ (up) key. Git Bash or Terminal will cycle back through the most recent commands you entered. (This is also very helpful if you typed a very long command that was just off by one letter.) It may even make sense to have a sense to one terminal window open just for building. Possibly another may be open running The Jupyter Notebook. Terminal, on OS X, has support for tabbed windows.
```

When you are happy with your website changes, you can push them to GitHub to make them live on your site.



