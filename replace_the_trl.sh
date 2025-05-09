#!/bin/bash

# Name of the file to replace
TARGET_FILE="dpo_trainer.py"

# Get the installation location of the 'trl' Python package
TRL_LOCATION=$(pip show trl | grep 'Location:' | cut -d' ' -f2-)

# Check if TRL location was found
if [ -z "$TRL_LOCATION" ]; then
  echo "Error: Could not find the installation path for 'trl'. Please make sure it is installed."
  exit 1
fi

# Define source and destination paths
SOURCE_FILE="./$TARGET_FILE"
DEST_FILE="$TRL_LOCATION/trl/trainer/$TARGET_FILE"

# Check if the source file exists
if [ ! -f "$SOURCE_FILE" ]; then
  echo "Error: Source file '$SOURCE_FILE' not found in current directory."
  exit 1
fi

# Check if the destination file exists
if [ ! -f "$DEST_FILE" ]; then
  echo "Error: Destination file '$DEST_FILE' does not exist. Please verify the structure of the 'trl' package."
  exit 1
fi


# Replace the file
cp -f "$SOURCE_FILE" "$DEST_FILE"
echo "Successfully replaced '$SOURCE_FILE' to '$DEST_FILE'"