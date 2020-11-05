#!/bin/bash




echo "Java + Hadoop Automated Installation"
#sudo apt update

# Check for update
echo "Running update..."
sudo apt update


jv=$(java --version)
hd=$(hadoop version)

if [[ $jv == *"openjdk"* ]]; then
	echo "Java is already installed. Skipping..."
else
	echo "Installing Java..."
	bash ./scpt/_java.sh
fi


if [[ $hd == *"Hadoop 2.7.3"* ]]; then
	echo "Hadoop 2.73 is already installed. Skipping..."
else
	echo "Installing Hadoop..."
	bash ./scpt/_hadoop.sh
	
	cd

	# Source .bach_profile in .bachrc
	echo 'source .bash_profile' >> .bashrc
fi

