# Create a GitHub Repository:
# streamlit run C:\Users\truto\PycharmProjects\PersonalProject\main.py
# If you haven('t already created a GitHub repository for your project, '
#              'go to GitHub and create a new repository. Note down the repository URL '
#              '(e.g., https://github.com/yourusername/your-repo.git).)
# Initialize Git in Your Local Project:
#
# Open your project in PyCharm.
# Open the terminal in PyCharm (usually at the bottom of the window).
# Navigate to your project directory using the cd command, e.g., cd /path/to/your/project.
# Initialize Git:
#
# Run the following commands to initialize Git in your project folder:
# bash
# Copy code
git init
git add .
git commit -m "Initial commit"
# Link Your Local Repository to GitHub:
#
# Run the following command, replacing the URL with your GitHub repository URL:
# Copy code
git remote add origin https://github.com/MrOvien/your-repo.git
# Push Your Code to GitHub:
#
# To push your code to GitHub, use the following command:
# bash
# Copy code
git push -u origin master
# If you're working on a different branch, replace master with the name of your branch.
# Provide GitHub Credentials:
#
# When you run the git push command, you'll be prompted to enter your GitHub username
# and password or a personal access token. Enter the required credentials.
# Verify on GitHub:
#
# Go to your GitHub repository in a web browser and verify that your code has been pushed successfully.

git add .
git commit -m "Changed to ilford instead of loondon"
git push origin master