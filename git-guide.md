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
  - Adds a specified file or folder to be tracked by git
- rm
  - 
- commit
  - Prepares all changed branches and added files to be pushed to remote. Appends specified message to be pushed as well.  
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
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~

