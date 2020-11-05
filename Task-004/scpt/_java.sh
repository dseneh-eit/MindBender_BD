#!/bin/bash

echo "JAVA INSTALLATION"

cd

# Create opt folder if it doesn't exists
mkdir -p opt
cd opt

# Remove this particular file if already exists to avoid confusion
rm -f jdk-8u221-linux-x64.tar.gz

# Download Java
echo "Downloading from URL.."
wget -O jdk-8u221-linux-x64.tar.gz -c --content-disposition "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"
echo "Download done!"

# Unzip downloaded file
echo "Unzipping file..."
tar -zxf jdk-8u221-linux-x64.tar.gz

# Delete download file
rm jdk-8u221-linux-x64.tar.gz

cd

# Set the path in the .bash_profile file
echo "Adding settings to bash file..."
echo '## JAVA_HOME' >> .bash_profile
echo 'JAVA_HOME=/opt/jdk1.8.0_221' >> .bash_profile
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> .bash_profile

source .bash_profile

echo 'Java Installation Done!!'


