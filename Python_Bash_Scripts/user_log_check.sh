#!/bin/bash
# file: user_log_check.sh

echo "Listing all system users:"
cut -d: -f1 /etc/passwd

echo -e "\nChecking for users with empty passwords (may require sudo):"
if [ -f /etc/shadow ]; then
    sudo awk -F: '($2==""){print $1}' /etc/shadow 2>/dev/null || echo "Cannot check empty passwords without sudo"
else
    echo "/etc/shadow not found. Skipping empty password check."
fi

echo -e "\nChecking last login for all users (using 'last' command):"
if command -v last >/dev/null 2>&1; then
    last -n 5
else
    echo "'last' command not found. Skipping last login info."
fi




