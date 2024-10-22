# POA Grad Seminar GitHub Workshop
Fall 2024 GitHub workshop series in the College of Earth, Ocean, and Atmospheric Sciences at Oregon State University. Designed for Physics of Oceans and Atmospheres graduate students to develop a familiarity with GitHub, collaborative coding, and open source software development.
## Outline of tasks
1. Skim the repository and **identify** a small thing you want to change (don't change anything yet!)
   * Ex: add a line to the README, fix a typo, write a few new lines of code, add a question in the FAQs section below, ... 
2. Open an issue and tell your collaborators what errors you found or describe the feature you think should be added.
3. Fork the repository
4. Clone the fork you made to your local computer
5. Create and switch to a new branch
    * Give the branch a name like `my-new-feature` (or more specifically, `subtract-function`, if you are adding a function that subtracts numbers) 
6. Make your small change to the repository
7. Commit your change
8. Push your change to your fork of the repository on GitHub
9.  Submit a pull request describing the change you have made 
10. Review other pull requests (or issues) and leave some supportive comments!

## Summary of terms
* **Repository**: a place on GitHub where you can store your code, files, and version history
* **Issue**: a forum-style post to plan, discuss, and track work for the repository
* **Fork**: a new repository created from the original repository
* **Clone**: downloading a full copy of a repository. This can be a copy of your new fork or the original repository
* **Branch**: a copy of your main code, but you can edit this without changing the original code
* **Remote**: a repository stored on GitHub, not on your computer
* **Local**: a repository stored on your computer, not on GitHub
* **Commit**: a save/snapshot of your file/repository at a specific time. 
* **Push**: uploads local commits to the remote repository for a specific branch
* **Pull**: download code from a remote repository and update your local repository
* **Merge**: take changes from one branch and apply them to another. If you like the code in your new branch, you can merge them with your original code.
* **Pull request**: you are requesting someone else to merge your branch into their code. To do this, they will "pull" your changes, review them, and then decide to merge them. Sometimes also called a merge request.
* **Review**: comment on proposed changes, make suggestions to improve the changes, and ultimately approve the changes if they are appropriate for the work.

## Some notes/FAQs
* Upstream/origin/local/remote??? 
  * When you **fork** someone else's repository, their repository is **upstream** and your forked repository is **origin**. When you **clone** a repository, **origin** is the copy on GitHub and **local** is the copy on your computer. **Remote** is also the verison on GitHub, but this can be **origin** (by default) or **upstream** or another remote **branch** if you set it up. 
* Commit/push/pull/merge/request???
  * *Simple order of operations*: 
    1. **Pull**: before you start working, download any new changes from remote GitHub repository to your local computer
    2. **Commit**: after you've made some changes, save them locally
    3. **Push**: send your changes to GitHub to be saved remotely
  * *Good practice order of operations*:
    1. **Pull**: before you start working, download any new changes from remote GitHub repository to your local computer
    2. **Branch**: create a new branch of your local repository so you can make new changes without messing up the current version of your code. This will save you sooo much headache if you just do it every time you want to work on a new piece of code/analysis.
    3. **Commit**: after you've made some changes, save them locally (they save to your new branch)
    4. **Push**: send your changes to GitHub to be saved remotely (still on your new branch)
    5. **Merge or pull request**: a pull request is just a request for someone to merge your new branch into the original code, so it's common in collaborative work. It's also good practice, but you can skip the "request" part and just merge a new branch, if you own the GitHub repository.