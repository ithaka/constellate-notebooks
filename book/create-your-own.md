# Creating your own Jupyter Book Website for Teaching
The [official Jupyter Book documentation](https://jupyterbook.org/intro.html) has more details about the platform. This tutorial is intended to help teachers get a course website up and running quickly for teaching. This tutorial will help you create a class website using free hosting from [GitHub Pages](https://pages.github.com/). See the GitHub Pages documentation for details about using a custom domain and other possibilities.

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

Navigate back into "Settings" then choose "Pages" in the lefthand navigation. Check that the source is the branch "gh-pages" and the folder is "/(root)". If necessary, click the "Save" button. (This is also where you can find settings for a custom domain if you own one you would like to use.)

![The GitHub Pages settings form](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/pages-settings.png)

If a link is listed, you should be able to click it to view your site immediately.

## Approving GitHub Actions

Our last step is to approve automatic workflows called GitHub actions. These will automatically create a new version of your website every time you make a change. Click on the "Actions" tab, then click "I understand my workflows, go ahead and enable them."

![the enable workflows button](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/approve-workflows.png)

There are two workflows created by default: 
* Ensure Clean Notebook Metadata- Reminds users if they forget to clear all notebook cells. This workflow can be safely deleted if it is not useful to you.
* deploy-book- This workflow automatically generates your website after you make a change. We recommend keeping it in place to make updating your website easy. This method is [documented in the official Jupyter Book documentation](https://jupyterbook.org/publish/gh-pages.html).

When you first open this page, it will say "There are no workflow runs yet" since the workflows are triggered by making a change to your repository. After each subsequent change, you will be able to inspect a log of the workflows to see if they completed successfully. 

![the box showing no workflows have run](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/no-workflows.png)

