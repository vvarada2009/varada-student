---
layout: post
title: Tools Set-up Blog  
permalink: /tools/setupblog
comments: true
---

Switching from a MacBook to a Windows computer for my CSP class required setting up VS Code, and learning how to use terminal and VS Code on a different computer. Here is my journey of how I set up VS code and successfully, after many tries,  got everything working and running!

## 🖥️ 1. Installing VS Code and Dependencies on Windows

Downloaded VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/) and installed it. During installation, ensured:
- **Add VS Code to PATH**
- **Enable context menu entries** to open folders directly

**Installed VS Code Extensions**:
- `Python (Microsoft)` – Python support and debugging
- `Jupyter (Microsoft)` – Notebook integration
- `GitLens` – Advanced Git history and insights


**Verified installations:**

```bash
# Check Python version
python --version

# Check Git version and configuration
git --version
git config --global user.name "Varada Chirag Vichare"
git config --global user.email "varada.vichare@gmail.com"
```

## 📂 2. Managing Repositories

- Copied the `pages` repository into a personal folder under the `opencs` directory
- Experimented with **theme changes** in the `pages` repo to personalize the site
-Created a student personal repository 

## 🐍 3. Setting Up a Virtual Environment

Run setup script for virtual environment:

```bash
# Setup virtual environment
./scripts/venv.sh
```

Activate virtual environment:

```bash
# Activate venv before running code
source/venv/bin/activate
```


## 🤝 4. Repository Collaboration

- Created a shared repository for my team 
- Created a fork of the team repository 

## 📓 5. Working with Jupyter Notebooks

- Locate the notebook file (e.g., `Jokes.ipynb`) in the personal repo
- Open **Developer Tools → Console → Clear**
- Run cells with the play button
- Adjust code so outputs display correctly on `pages` as well as chaning the jokes to some of my own!
- Commit changes with outputs:

```bash
# Commit notebook with outputs
git add <notebook_filename>.ipynb
git commit -m "Updated notebook with outputs"
git push
```


## ✅ 6. Other Tasks Completed

- Verified all outputs in notebooks appeared correctly on pages
- Confirmed Python code ran properly in the virtual environment
- Managed multiple repositories and forks
- Customized project settings and themes for personal workflow
- Ensured VS Code functionality on Windows 

## 🌟 Final Thoughts

After many efforts and tries, I was able to finally get everything set up properly on my new Windows computer. This experience of switching and re-doing everything on a different computer allowed me to grow as a student and learn many new things. Furthermore, I am also highly grateful for my peers who helped me out during this process and teaching me new things! 

## Progress during weeks 1-4 

## 👤 About Me Page
- Created an **About Me page** in the `about.md` file

## 📂 Cloning Repositories 
-Cloned the pages repository of Open Coding 

-Established Personal repository

-Cloned team repository

# General format to clone a repository

git clone <repository-url>

## 📑 Copying Files Between Repositories

- Learned how to move files from one repo to another
-For example, moved the 2025-09-03-background-lesson.ipy file from pages to personal repo

## 📓 Jupyter Notebooks & Jokes

-Opened and ran Jupyter Notebooks in VS Code

-Practiced with the Jokes.ipynb notebook and converted results into HTML format

-Added my own lawyer jokes

 ## Changing Background

-Made changes to the background.md file

-By editing the front matter, we were able to change the background image for our website

