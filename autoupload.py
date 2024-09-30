import subprocess
import os
import sys

if len(sys.argv) > 1:
    message = sys.argv[1]
    print(f"Message received: {message}")

# Define the path to your Git repository
repo_path = 'C:/Users/shind/OneDrive/Desktop/desktop things/python DA'

# Change to the repository directory
os.chdir(repo_path)

# Function to run a command and print its output
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    print("Command:", ' '.join(command))
    print("Return code:", result.returncode)
    if result.stdout:
        print("Output:", result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())
    return result

# Refresh requirements
with open('requirements.txt', 'w') as req_file:
    result_new_req = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    req_file.write(result_new_req.stdout)

if result_new_req.returncode != 0:
    print("Failed to refresh requirements. Exiting.")
    exit(1)

# Run `git add .`
result_add = run_command(['git', 'add', '.'])

# Check if `git add .` was successful
if result_add.returncode != 0:
    print("Failed to add changes. Exiting.")
    exit(1)

# Run `git rm -r --cached myenv/`
result_remove_myenv = run_command(['git', 'rm', '-r', '--cached', 'myenv/'])

# Check if `git rm` was successful
if result_remove_myenv.returncode != 0:
    print("Failed to remove myenv. Exiting.")
    exit(1)

# Run `git commit -m "new code"`
commit_message = message if message else "new code"
result_commit = run_command(['git', 'commit', '-m', commit_message])

# Check if `git commit` was successful
if result_commit.returncode != 0:
    print("Failed to commit changes. Exiting.")
    exit(1)

# Run `git push origin master`
result_push = run_command(['git', 'push', 'origin', 'data_science_project'])

# Check if `git push` was successful
if result_push.returncode != 0:
    print("Failed to push changes. Exiting.")
    exit(1)

print("Git repository updated successfully.")
