#!/bin/bash
TARGET_IP=$1
echo "checking connection to $TARGET_IP..."
ping -c 1 $TARGET_IP > /dev/null
if [ $? -eq 0 ];then
	echo "Sucess: The server at $TARGET_IP is ONLINE!"
else
	echo "Warning: The server at $TARGET_IP is  OFFLINE or unreachable."
fi
