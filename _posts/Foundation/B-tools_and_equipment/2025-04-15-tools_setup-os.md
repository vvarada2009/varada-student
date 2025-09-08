---
layout: post
title: Setting Up VS Code on Windows for CSP Projects
permalink: /tools/setupblog
comments: true
---


Switching from a MacBook to a Windows computer for CSP projects required setting up VS Code once again. Here is my journey documenting all the commands and tasks I completed and finally got everything to work on my Windows computer!


Installing VS Code and Dependencies on Windows


Downloaded VS Code from https://code.visualstudio.com/ and installed it. During installation, made sure to:
- Add VS Code to PATH
- Enable context menu entries to open folders directly


Installed necessary VS Code extensions:
- Python (Microsoft) for running Python code
Jupyter (Microsoft) for notebooks
- GitLens (optional) for Git integration


-


Installed Python and verified installation:
python --version


Installed Git for Windows and configured my identity:
git config --global user.name "Your Name"
git config --global user.email "you@example.com"


Transitioning Projects from Mac to Windows


Cloned the `pages` repository into my personal folder under the `opencs` directory to work without affecting the main repo.


Experimented with theme changes on the `pages` repo to personalize it.


Setting Up a Virtual Environment


Ran the virtual environment setup script:
./scripts/venv.sh


Activated the virtual environment before running code:
source/venv/bin/activate


Verified that the virtual environment was active by checking the Python interpreter in VS Code.


Repository Collaboration


Created a shared repository with my group.


Working with Jupyter Notebooks:


Located the Jupyter Notebook file in my personal repo.


Opened Developer Tools in VS Code, selected Console, and cleared previous outputs.


Ran notebook cells using the play button, for example in the `2025-08-21-github_pages.ipynb` file.


Changed the joked into html format and added some jokes of my own.


Committed the notebook with outputs to Git:
git add <notebook_filename>.ipynb
git commit -m "Updated notebook with outputs"
git push


Other Tasks Completed


- Verified all outputs in Jupyter notebooks appeared correctly on pages.
- Confirmed Python code ran properly in the virtual environment.
- Ensured VS Code was fully functional on Windows, replicating my MacBook setup.


Final Thoughts


Switching from Mac to Windows was a learning experience for me. It required me to carefully follow instructions and set up VS Code, Python, virtual environments, Jupyter Notebooks, and repository management.