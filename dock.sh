#!/bin/bash
echo "-----------------------------------------------------------------------"
echo "Listing Docker containers "
echo " "
docker ps -a

i='y'

while [ $i == 'y' ]
do
	echo "_________________________________________________________"
	echo "enter name of docker containers you want to start"
	
	read s

	echo "starting $s"
	
	echo "__________________________________________________________"
	
	docker start $s

	echo "__________________________________________________________"

	echo "docker container started successfully"

	docker exec $s service nginx start
	echo "__________________________________________________________"
	
	echo "SERVER STARTED SUCCESSFULLY"

	echo "__________________________________________________________"
	
	echo "Do you want to continue [y/n]"
	
	read i
	
done


