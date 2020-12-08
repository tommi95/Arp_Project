#!/bin/bash

source devel/setup.bash

echo -n "Type '1' in order to set a goal position from RViz, '2' in order to enable the autonomous navigation or '3' to manually guide the robot."
echo
read MODE
case "$MODE" in
1)
	echo -n "___________________Goal selection mode ___________________"
	echo
	echo
	echo "Do you confirm your choice?"
	read REPLY
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		echo "Please select a goal from the RViz simulation"
		roslaunch coordinator mouse.launch
	else
		exit
	fi
	;;

2)
	echo -n "___________________Autonomous mode___________________"
	echo
	echo
	echo "Do you confirm your choice?"
	read REPLY
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		echo "Digit 0 to stop the simulation"
		roslaunch coordinator coord.launch
	else
		exit
	fi
	;;

	3)
		echo -n "___________________Autonomous mode___________________"
		echo
		echo
		echo "Do you confirm your choice?"
		read REPLY
		echo
		if [[ $REPLY =~ ^[Yy]$ ]]
		then
			echo "Digit 0 to stop the simulation. Look at the new terminal for info abount the keys"
			roslaunch coordinator keyboard.launch &
			gnome-terminal -- rosrun teleop_twist_keyboard teleop_twist_keyboard.py


		else
			exit
		fi
		;;

*)
 	echo -n "Unknown mode."
	echo
	;;


esac
