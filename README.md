# Arp_Project

This didactic project consists of an architecture implemented with ROS aimed to develop a mobile robot capable of being controlled by the user or to navigate autonompusly in the simulated scenario.

## Installation and prerequisites

For the configuration a script has been implemented, consequently all the packages and dependecies can be installed by typing the following:
```
$ install_dep.sh
```

## Execute the code

In order to run the code implemented the following command can be digited once the workspace has been accessed:
```
$ bash launch.sh
```

Once the code has been executed 3 modalities can be chosen:

 1. from RViz select the option 2D Nav in the toolbar and select a point that the robot will reach. It is possible to interact through RViz by selecting other points once the one chosen has been reached or at any time during the achievement of the position;

 2. the robot will autonomously navigate in the scenario;

 3. the robot can be controlled exploiting the keyboard, the possible commands are shown in a dedicated terminal.

Once the navigation is performed it is possible to store the map by typing the following command:
```
$ rosrun map_server map_server -f <filename>
```
by replacing filename with a desired name.


## Team:

Giovanni Battista Borre':  giovaborr@gmail.com

Tommaso Gruppi:  tommygruppi@gmail.com
