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
- add
  - Adds a specified file or folder to be tracked by git.
- rm
  - Removes file from stage.
    - must be staged and committed
    - deletes local file as well
  - Combined with '--cahced' flag, will remove it from stage but not from local.
    - must be staged but does not need to be committed
    - does not delete the local file
- commit
  - Prepares all changed branches and added files to be pushed to remote. Appends specified message to be pushed as well.
  - Combined with 'a' flag it auto-adds previously tracked files to commit.  
- push
  - Pushes committed files from a the local to the remote.
- fetch
  - Downloads and stashes changes from the remote to be applied later to the local.
- merge
  - In relation different branches, takes in all files from a specified branch and merges them into the current branch.
  - In relation to current branch, take changes from 'fetch' and applies them to the current branch.
- pull
  - Checks the remote and pulls down any changes that the local does not have. A conbination of 'fetch' and 'merge'. 
- branch
  - Copies the current branch to a new branch with specified name.
- checkout
  - Switches to specified branch.
  - Combined with '-b' flag, will create new branch of specified name and swithc to it.
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

