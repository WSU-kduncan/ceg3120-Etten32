J+M+J
## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Makes a clone of specified remote repository onto local device.
  - `git clone git@github.com:WSU-kduncan/ceg3120-Etten32.git`
- add
  - Adds a specified file or folder to be tracked by git.
  - `git add caloy.txt`
- rm
  - Removes file from stage.
    - must be staged and committed
    - deletes local file as well
  - Combined with '--cahced' flag, will remove it from stage but not from local.
    - must be staged but does not need to be committed
    - does not delete the local file
  - `git rm --cahce caloy.txt`
- commit
  - Prepares all changed branches and added files to be pushed to remote. Appends specified message (typed in editor) to be pushed as well.
  - Combined with 'a' flag it auto-adds previously tracked files to commit.
  - Combined with 'm' flag a message may be appended right in the console.
  - `git commit -am "Commit example"`  
- push
  - Pushes committed files from a the local to the remote.
  - `git push`
- fetch
  - Downloads and stashes changes from the remote to be applied later to the local.
  - `git fetch`
- merge
  - In relation different branches, takes in all files from a specified branch and merges them into the current branch.
  - In relation to current branch, take changes from 'fetch' and applies them to the current branch.
  - `git merge exampleBranch` or `git merge`
- pull
  - Checks the remote and pulls down any changes that the local does not have. A conbination of 'fetch' and 'merge'.
  - `git pull` 
- branch
  - Copies the current branch to a new branch with specified name.
  - `git branch exampleBranch`
- checkout
  - Switches to specified branch.
  - Combined with '-b' flag, will create new branch of specified name and swithc to it.
  - `git checkout exampleBranch` or `git checkout -b "exampleBranch"
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - Contains information retaining to git such as commit messages, logs, and the git config file. 
- .gitignore file
    - File that holds list of files for git to ignore.
    - files should use relative paths
    - prevents file from being added unless forced
- ~~.git/hooks~~

## GitHub

- Pull requests
  - Form to request a branch merge wich can be checked over and commented, and either merged or rejected by repository authorities.
- SSH authentication to repositories
  - A key system between local and remote that gives authority for the local to securely connect and deal with GitHub repositories.
    - requires a private key on the machine
    - requires a public key on GitHub that corresponds to a copy on the local 
- ~~Actions~~

