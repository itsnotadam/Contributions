# 🎲 GitHub Contribution Graph Generator

A simple Python script that generates random commits to create activity on your GitHub contribution graph.

![GitHub](https://img.shields.io/badge/GitHub-Contribution-green) ![Python](https://img.shields.io/badge/Python-3.6+-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

<br>

## ✨ Features

- 🎲 **Random Commit Generation**: Creates commits with random dates over the past year
- ⚡ **Easy to Use**: Simple command-line interface
- 🔧 **Customizable**: Choose number of commits and target file
- 📊 **GitHub Compatible**: Uses proper Git date environment variables
- 🐍 **Python-Based**: Works on Windows, Mac, and Linux

<br>

## 📥 Prerequisites

Before you begin, ensure you have:

- **Git** installed on your system
- **Python 3.6+** installed
- A **GitHub account**
- A **private repository** (recommended)

<br>

## 🛠 Installation

### Step 1: Install Git on Windows

1. Download Git from [git-scm.com](https://git-scm.com/)
2. Run the installer with all default options
3. Open **Command Prompt**
4. Verify installation:
```
git --version
```

### Step 2: Verify Python on Windows

Check if Python is installed:
```
python --version
```

If not installed:
1. Download from [python.org](https://python.org)
2. Run installer **WITH "Add Python to PATH" checked**
3. Restart Command Prompt and verify:
```
python --version
```

<br>

## 🚀 Setup

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **"+"** → **"New repository"**
3. Name it anything (recommended: `Garden` or `Graph`)
4. **Make it private**
5. **Do not** initialize with README
6. Click **"Create repository"**

### Step 2: Clone Repository in Command Prompt

Open Command Prompt and run:
```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 3: Download and Add Python File

1. Download `main.py` from this repository
2. Drag it to your cloned repository folder on your system
3. Verify the file is in the correct location:

You should see `main.py` in the file list.

### Step 4: Configure Git (First Time Only)

Set your Git identity:
```
git config --global user.name "Your Github Username"
git config --global user.email "yourgithub.email@example.com"
```

<br>

## 🎯 Usage

### Step 1: Commit the Script to GitHub

Add and push the Python file to your repository:
```
git add main.py
git commit -m "Add commit generator script"
git push origin main
```

### Step 2: Run the Script

Execute the Python script:
```
python main.py
```

### Step 3: Follow the Prompts

The script will ask for:
1. **Number of commits** (default: 200)
2. **File to modify** (default: data.txt)

Then it will automatically:
- Create random commits over the past year
- Push them to GitHub
- Show progress in real-time

### Step 4: Check Your Results

Wait 2-3 minutes, then visit your GitHub profile page to see your updated contribution graph

<br>


## ❓ FAQ

### ⏰ How long does it take?
- 200 commits ≈ 2-3 minutes
- 500 commits ≈ 5-7 minutes
- Depends on your internet connection

### 🔄 Can I run it multiple times?
Yes! Each run will add more commits to your graph.

### 🗑️ How do I clear my graph?
Easiest way is to delete your repository on Github and restart from scratch.

<br>

## ⚠️ Disclaimer

This tool is intended for:
- Learning Git and GitHub workflows
- Testing contribution graph features
- Personal private repositories

<br>

## 🐛 Troubleshooting

### Common Windows Issues:

**"python not found"**
- Python not in PATH - reinstall with "Add to PATH" checked
- Try:
```
py --version
```

**"Permission denied"**
- Configure Git user properly:
```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Push rejected**
- Pull latest changes first:
```
git pull origin main
```

**Script stops mid-way**
- Check internet connection
- Ensure repository is properly cloned
- Verify GitHub credentials are saved

<br>

## 📝 License

This project is for educational purposes. Use responsibly and in accordance with GitHub's Terms of Service.
