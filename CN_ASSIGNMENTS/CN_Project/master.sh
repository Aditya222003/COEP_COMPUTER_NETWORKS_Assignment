#!/bin/bash
################################################################################

# Sometimes the port number causes problem and it doesn't restart
while true
do
echo "s to start, q to exit, r to start/ restart."
read key

if [[ "$key" == 'r' ]]
then
    echo "Server Running On port 5565"
    echo
    kill $(lsof -t -i:5565)
    gnome-terminal -e "bash -c \"python3 httpServer.py 5565; exec bash\""       
elif [[ "$key" == 'q' ]]
then
    echo "Shutting Down... zzzz..."
	# program to quit
    # fuser -k 5565/tcp
    kill $(lsof -t -i:5565)
    # killall terminal
    exit;
elif [[ $key == 's' ]]
then
    echo "Starting :D"
    # killall zsh
    kill $(lsof -t -i:5565)
    gnome-terminal -e "bash -c \"python3 httpServer.py 5565; exec bash\""       
    
else
    echo
fi

done
