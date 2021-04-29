# Push Changes to the Web

Now that you have made changes to your site, the final step is to make those changes live on the web. In the language of *git*, we need to *push* our changes to our GitHub repository. Here, we assume that you are working alone on the site, so we are not going to go into issues that may be significant for working collaboratively with *git*. (For example, these directions discuss *pushing* to GitHub, but do not discuss *pulling*, *merging*, or other more advanced methods. If you would like to learn more about git, a great starting point is [Corey Schafer's YouTube Series on git](https://youtu.be/HVsySz-h9r4).)

## The three essential git commands

When it comes to *pushing* your repository to GitHub, we will use three commands:

|git command|purpose|
|---|---|
|`git add -A`|Add all the files in the repository|
|`git commit -m "A message describing your commit"`|Attach this message to my updates|
|`git push`|Push my changes to GitHub|

1. Open up your command line, either Git Bash or terminal, then navigate to your repository using `cd`. 
2. Use the `git add -A` command to add all the files in the repository. If you would prefer to just add one file, you can specify that file instead of using the `-A` flag.
3. Use the `git commit -m "Put a commit message here"` command to commit a message to your changes. The text in quotation marks should describe the changes you made for this update. Git keeps track of all of your changes, so if you ever need to roll back changes this message will be very useful for finding which version of your repository you want to return to.
4. Use the `git push` command to push to your GitHub repository. When you push for the first time, you will need to validate your identity as the owner of your GitHub account by entering your password. It is important here that the git global user email you set also matches your GitHub account email. If git prompts you to login to GitHub through the website, choose that option, as it may set permissions so that future logins are not necessary. Alternatively, you can [send a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) as your password which should keep you from having to enter your password every time you push.

```{note}
After your push completes successfully, it may take 2-3 minutes before the live version of your site is updated. The change is not immediate.
```

## What if I mess up local installation?

It happens to everyone at some point. If your local install is completely broken, you can simply delete the local repository folder from your computer. Simply use the `git clone` command again to download a new copy from GitHub. The downloaded copy will contain any changes from your last push.

## What if I need to go back a version?

We don't recommend doing this if you're collaborating with others. If you're the only person pushing to the repository though, you can use the `git revert` command to undo your last push. You will need the seven-digit "hash" of your last commit which can be found on the GitHub website. 

![the most recent commit hash](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/commit-hash.png)

If you click on the clock which shows the number of commits, it will show the hashes for all recent commits.

![all recent commit hashes in github](https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/recent-commits.png)

Grab the hash for the commit  you would like to revert and run:
```
git revert 1234567
```


