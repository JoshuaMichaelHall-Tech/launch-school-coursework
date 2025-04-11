# Getting Started - Preparations

## Installation Challenges

- Installing and configuring software is often challenging for developers
- Different hardware, software versions, and configurations can cause issues
- Consider it a learning opportunity when troubleshooting problems
- Recommendation: Use a Macintosh or AWS Cloud9
- Python command may be `python` or `python3` depending on system

## The Command Line

- Command examples are shown with `$` to represent the command prompt
- Don't type the `$` when entering commands
- Use `echo $SHELL` to determine which shell you're using
- Bash uses `$` prompt, Zsh uses `%` prompt
- Essential shell commands to know:
  - `cd`: navigate between directories
  - `mkdir`: create a new directory
  - `rmdir`: delete an empty directory
  - `touch`: create an empty file
  - `rm`: delete a file
  - `git`: for version control

## Installing Python

### Mac Installation

- Use Homebrew for easiest installation
- For Apple silicon Macs, ensure Terminal.app is not set to use Rosetta
- After Homebrew installation, update PATH environment variable
- Install Python using `brew install python@3.12` (or latest version)
- Create alias with `echo "alias python=python3" >> ~/.bash_profile` or for Zsh
- Check installation with `python --version`
- Verify PATH with `echo $PATH`

### GitHub Codespaces

- Cloud-based alternative for development
- Free environments available with limitations:
  - Use smallest codespaces (2-core)
  - Don't leave codespaces running
  - Don't create multiple codespaces
  - Don't add additional disk space
- Uses browser interface, relatively trouble-free
- Comes with Python pre-installed

### AWS Cloud9

- Another cloud-based alternative
- Free tier available with limitations similar to GitHub Codespaces
- Only needs browser and internet connection
- May have older Python version pre-installed

### Other Linux Systems

- Most Linux systems come with Python pre-installed
- Check version with `python --version`
- Follow official Python installation instructions if needed

### Windows

- Not recommended, but Windows Subsystem for Linux Version 2 (WSL2) works well
- Essentially provides Linux environment on Windows

## Using a Code Editor

- Use a plain text code editor, not a word processor
- Visual Studio Code (VSCode) highly recommended
- Other options: Vim, Emacs
- Word processors add unwanted formatting that breaks code

## Python Documentation

- Available at python.org/doc/
- Key sections to focus on:
  - Language Reference (especially Expressions, Simple Statements, Compound Statements)
  - Library Reference (Built-in Types, Functions, Constants)
  - Glossary for terminology
  - Complete Table of Contents
- Documentation may not always be helpful; additional research may be necessary
