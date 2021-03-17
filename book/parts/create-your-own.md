# Creating your own Jupyter Book for Teaching
The [official Jupyter Book documentation](https://jupyterbook.org/intro.html) has more details about the platform. This tutorial is intended to help teachers get a course website up and running quickly for teaching a course. This tutorial will help you create a class website using free hosting from [GitHub Pages](https://pages.github.com/). See the GitHub Pages documentation for details about using a custom domain and other possibilities.

## Create a GitHub Account

Click "Sign up" and supply a username, email address, and password for your account.

![github sign up page](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/join_github.png)

Verify your email address with GitHub by clicking the "Verify Email Address" button sent to your email.

## Fork the Constellate Notebooks repository

Visit the [Constellate notebooks repository](https://github.com/ithaka/tdm-notebooks). In the upper right-hand corner click on "Fork". 

![fork button in github](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/fork.png)

## Rename your repository

In the repository, click on "Settings" and rename the repository to your course name. Then click "Rename".

![Settings menu and repository rename form](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/rename-repo.png)

## GitHub Pages Settings

Navigate back into "Settings" then scroll down the page to "GitHub Pages". Check that the source is the branch "gh-pages" and the folder is "/(root)". If necessary, click the "Save" button. (This is also where you can find settings for a custom domain if you own one you would like to use.)

![The GitHub Pages settings form](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/pages-settings.png)

## View your Site

It may take 1-2 minutes for GitHub to load your settings. When your site is ready, it will be available at the site: https://**your-github-username**.github.io/**your-repository-name**/ 

If you navigate back to "Settings > GitHub Pages", a link to your site will be supplied.

## Site Configuration (_config.yml)

The Jupypter Book site settings are in a file called `config.yml`. It is located in the root directory of your repository. To preview the file, click on it. To make changes, click on the pencil icon. 

![The pencil icon to edit a file](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/edit-config.png)

Here are some key items you will probably want to change.

| Setting | Effect |
|---|---|
|title| Changes the displayed title of your book/site|
|author| Changes the name of the author for your book/site! |
|logo| A path to a logo for your class|
|favicon| A path to a favicon for your site |
|repository url | Change this to the github page for your repository |

There are many more settings in this configuration file. For more details see the [official Jupyter Book documentation](https://jupyterbook.org/intro.html).

When you are finished making changes, scroll to the bottom of the page. Write a description of the changes you made for reference and click "Commit Changes".

![The commit changes form in GitHub](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/commit-changes.png)

These changes may take 1-2 minutes to be reflected on your site.

## Editing Table of Contents (_toc.yml)

The information for your Jupyter Book's table of contents is in a file called `_toc.yml`. It is located in the root directory of your repository. To preview the file, click on it. To make changes, click on the pencil icon.

![The pencil icon to edit a file](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/edit-config.png)

