#AirBnB Clone (HBNB) Project

## Project Description

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website clone.

##General Use

1. First clone this repository of the project from Github. 
1. This will contain the simple shell program and all of its dependencies.
1. Locate the console.py file and run it.
1. This will appear (hbnb). then use the supported commands.

## Supported commands
These are commands that can be executed by the command interpreter. They have the format command [argument]... but you could also use the format Model.command([argument]...), with the exception of the first 3 commands below.

- create - Creates an instance based on given class

- destroy - Destroys an object based on class and UUID

- show - Shows an object based on class and UUID

- all - Shows all objects the program has access to, or all objects of a given class

- update - Updates existing attributes an object based on class name and UUID

- quit - Exits the program (EOF will as well)

**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again to wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


```
$ echo "help" | ./console.py
(hbnb)
```
##Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command|	|Description|
|-- | --|
| **quit or EOF** | Exits the program|
| **Usage**   | By itself   |
| ***-----*** | ***-----*** |
