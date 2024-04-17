#!/bin/bash

# Update and upgrade Termux packages
echo "Updating and upgrading Termux packages..."
pkg update -y && pkg upgrade -y

# Install necessary packages for Python and Selenium
echo "Installing Python and Selenium packages..."
pkg install python -y
pip install selenium colorama

# Install Firefox in Termux
echo "Installing Firefox in Termux..."
pkg install firefox -y

# Install geckodriver for Firefox
echo "Installing geckodriver for Firefox..."
pkg install geckodriver -y

# All required packages installed
echo "All required packages installed successfully!"
