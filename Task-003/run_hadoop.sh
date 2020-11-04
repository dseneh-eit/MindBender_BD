#! /usr/bin/bash

dataNode="DataNode"
nameNode="NameNode"

echo "Enter 1 to START service"
echo "Enter 2 to STOP service"

read opt

if [[ $opt == 1 ]]; then
	
	out=$(jps)
	echo "${out}"

	#Check if service is running otherwish start service:
	if [[ "$out" == *"$dataNode"* ]]; then
		echo "Service is running"
	else 
		echo "Starting service..."
		eval "start-all.sh"

	fi

else
	out=$(jps)
	echo "${out}"

	#Check if service is running otherwish start service:
	if [[ "$out" == *"$dataNode"* ]]; then
		echo "Stopping service..."
		eval "stop-all.sh"
	else 
		echo "Service is not running"

	fi

fi
