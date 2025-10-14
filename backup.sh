#!/bin/bash
# Backup script for the assignment
# Usage: ./backup.sh
# NOTE: This script uses GNU date/stat. On macOS you may need to adjust date/stat flags.

# [TASK 1]
# Set the source (target) directory and destination directory
targetDirectory="/home/$(whoami)/backup_test_target"
destinationDirectory="/home/$(whoami)/backup_test_destination"

# [TASK 2]
# Display the values to the user
echo "Target directory: $targetDirectory"
echo "Destination directory: $destinationDirectory"

# Ensure destination directory exists
mkdir -p "$destinationDirectory"

# [TASK 3]
# Set currentTS to the current timestamp in seconds
currentTS=$(date +%s)
echo "currentTS = $currentTS"

# [TASK 4]
# Set the backup file name. Use human readable plus timestamp.
backupFileName="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
echo "backupFileName = $backupFileName"

# Prepare array to hold files to back up
toBackup=()

# [TASK 5]
# We will define origAbsPath inside the loop for each file. Example:
# origAbsPath will be set as an absolute path of the file when iterating.
# (This line is an example definition; actual assignment happens per-file below)
origAbsPath=""

# [TASK 6]
# Define destAbsPath (destination absolute path for the backup file)
destAbsPath="$destinationDirectory/$backupFileName"
echo "destAbsPath = $destAbsPath"

# [TASK 7]
# Change directory to targetDirectory
mkdir -p "$targetDirectory"   # create target for testing if it doesn't exist
cd "$targetDirectory" || { echo "Cannot cd to $targetDirectory"; exit 1; }

# [TASK 8]
# Set yesterdayTS = timestamp for 24 hours before currentTS (in seconds)
yesterdayTS=$(date -d "@$currentTS - 24 hours" +%s)
echo "yesterdayTS = $yesterdayTS"

# [TASK 9]
# Command to list all files and directories (use inside $())
allitems=$(ls -A)
echo "All items in target:"
echo "$allitems"

# Iterate through files and decide which to back up
for file in $(ls -A); do
  # Skip directories (optional) - include if you want files only
  if [ -d "$file" ]; then
    continue
  fi

  # [TASK 10]
  # Check if file was updated within the past day:
  # get file modified time in seconds (using stat -c %Y)
  fileTS=$(stat -c %Y "$file")

  # If fileTS is newer than yesterdayTS, it was updated in the past 24 hrs
  if [ "$fileTS" -gt "$yesterdayTS" ]; then
    # [TASK 11]
    # Add the file name to the toBackup array
    toBackup+=("$file")
    echo "Added to backup: $file (modified: $fileTS)"
  fi
done

# If array empty, notify and exit
if [ ${#toBackup[@]} -eq 0 ]; then
  echo "No files modified in the last 24 hours. No backup created."
  exit 0
fi

# [TASK 12]
# Create the backup file (archive & compress) in the current directory
# Use tar with list of files from array
tar -czvf "$backupFileName" "${toBackup[@]}"

# [TASK 13]
# Move the backup file to the destination path
mv "$backupFileName" "$destinationDirectory/"

# Show the final location
echo "Backup moved to: $destinationDirectory/$backupFileName"
