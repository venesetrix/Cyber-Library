# Git Basics

## Git as Version Control System

Centralized - Saving and changing code on the Server. Example: Apache SubVersion (SVN)
Dezentralized - Saves the Code on the local machine (cloning) and pushes/pulls when finished.

Ist ein Versionskontrollsystem
Commits = Check Points
Branches = Multiverse
Merging = Synchronisierung von Branches

## How Git works

HEAD is pointing to the Branch we're working in.
The first Branch has been called MASTER in the past, but is called MAIN today.

There are 3 environments:
* Working
* Staging
* Commit

## Using Git

### Start Git
**Option #1:** Start Git Bash in the Git folder by right-clicking in the folder > "Show more options" > Open Git Bash here.

**Option #2:** Open Visual Studio Code

### Maintain files in the Git folder that should not be synchronized
Maintain the files or folders in a file with the name *.gitignore*
For example:
* ./DS_Store
* .vscode/
* authentication.js
* node_modules
* notes/
* **/*-todo.md

This can also be maintained in a global ignore file:

```
git config --global core.excludesfile [file]
```

If the ignore file does not work so well, it may be due to the local cache, which can be deleted as follows:
```
git rm -r --cached .
```

## Essential files of a repository

GitHub can provide templates for many of the following files.

| Filename | Description
| ----- | :----- |
| README.md | Purpose, Homepage. Kann in root, docs or .github liegen. |
| LICENSE | Lizenz-File. Auch im Format .md, .txt, rst. Muss im root-Folder sein. |
| CODE_OF_CONDUCT.md | Templates verfügbar. |
| SECURITY.md | Security-Policy und wo Schwachstellen gemeldet werden können. |
| CONTRIBUTING.md | Wie man beitragen kann. Kann in root, docs oder .github-Folder sein. |
| SUPPORT.md | Wie man Support bekommen kann. Im root, docs oder .github. |
| CODEOWNERS | Wer Schreibberechtigungen hat und Notifications bekommt. Format ist: **/*.js @USERNAME OR /docs EMAIL @USERNAME @USERNAME |

## Git Flow
Typical development process:
* Create a feature/fix branch
* Make changes
* Merge to the master
* Delete the feature branch

# Git Commands

## Git Config
Set global config settings
```
git config --global user.name "Venesetrix"
git config --global user.email "Your Email"
```

Creating a repository
```
git init
```

## Working with Branches

Show the branches
```
git branch
```

Change to another branch
```
git switch BRANCH
```

Copy of a branch
```
git switch -c NAME
git checkout -b NAME
```

Merge the given branch into the current
```
git merge BRANCH
```

Delete a branch
```
git branch --delete BRANCH
```

Show status
```
git status
```

Show what has been done
```
git log
```


## Commiting Files

To commit a file later, we have to bring it into the Staging area.

Add a single file to the staging environment
```
git add FILENAME
```

Add all files of a project
```
git add --all/-A
```

Add all files of a folder
```
git add .
```

Create a checkpoint with a description
```
git commit -m "First Commit"
```

Change last commit and it's title
```
git commit --amend
```

Rebase a commit into the pasts or merge it there
```
git rebase -i --root
```

Reset to an old commit
```
git reset COMMIT-ID
```

Reset to an old commit, delete changes and change the files, too
```
git reset --hard COMMIT-ID
```

## File handling

### Diffing files

Compare changes. You can quit with a q after the colon. Visual Studio Code also has a Source Control Editor.
```
git diff
```

Compare Changes in a specific commit via commit-ID
```
git diff [commit-ID]
```

See only the changes
```
git log --oneline
```

### File recovery
Recover a file via name
```
git restore FILENAME
```

Restore all files	
```
git restore .
```

Old recovery command
```
git checkout .
```

Pull a file out of Staging
```
git restore -S
```

### Delete or rename files
**Option #1: Delete via VSC** 
Simply delete via Visual Studio Code (VSC) or from the operating system. However, the deletion must be passed on to the system via git add/commit.

**Option #2: Delete via CLI** 
```
git rm <filename>
```

**Option #1: Rename via file system**
Rename in the file system. However, this deletes the old file and creates a new file with the old name. If you now restore from the staging (before the commit), the same file is created again with a different name.

**Option #2: Rename via CLI**
```
git mv [oldname] [newname]
```

### Delete files which are not under version control
Show which files will be deleted
```
git clean -n
```
Show which files and folders will be deleted
```
git clean -dn
```
Delete all files
```
git clean -df
```
# Working with GitHub
## Setup a repository
First, create a repository in GitHub by using the browser. Then connect it with the local repository:
```
echo "# <title>" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/venesetrix/<title>.git
git push -u origin main
```
## Push a given repository via CLI
```
git remote add origin https://github.com/venesetrix/<title>.git
git branch -M main
git push -u origin main
```
## Working with remote sources
Add a remote source
```
git remote add NAME URL
```
Remove a remote source
```
git remote remove NAME
```
Rename
```
git rename OLDNAME NEWNAME
```
## Push a branch
```
git push REMOTE BRANCH
```
Needs to be done as setup:
```
git push --set-upstream-to/up origin main
```
```
git push -u origin main
```
Push all local branches
```
git push --all
```
## Typical procedure of Changes in GitHub
1. Changes of the files via the browser
2. Button Commit changes…
3. Create a new branch
4. Create pull request
5. (add reviewers)
6. Merge pull request
7. Delete branch

## Syncing of Git
Clone/Download a respository onto the local computer
```
git clone URL
```
Pull changes from other users
```
git pull
```
Load commits, objects and references from a repository
```
git fetch
```