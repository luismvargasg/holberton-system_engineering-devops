# Processes and signals

> This directory contains all the tasks of the project "0x05. Processes and signals" at [Holberton School](https://www.holbertonschool.com "Holberton School.")

[![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1)

## Table of Contents

- [Processes and signals](#processes-and-signals)
  - [Table of Contents](#table-of-contents)
  - [Basic info](#basic-info)
    - [PID and Processes](#pid-and-processes)
    - [Signals](#signals)
  - [General Objectives](#general-objectives)
  - [Directory Files Description](#directory-files-description)
  - [Prerequisites](#prerequisites)
  - [Built With](#built-with)
  - [AUTHOR](#author)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Basic info

### PID and Processes

A PID or "Process Identification" is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system. A process is an executing instance of a program and each process has a unique PID, a positive integer. There is a reserved PID, the number 1 and it is always assigned to the process init because is always the first process on the system or session.

The default maximum value of PIDs is 32,767. Usually in small computers this default value is enough but in larger computers or servers that may require more processes this maximum value could be greater.

### Signals

Signals are software interrupts, when the signal occurs, the process has to tell the kernel what to do with it. In Linux, every signal has a name that begins with characters SIG. For example:

* A SIGINT signal that is generated when a user presses ctrl+c. This is the way to terminate programs from terminal.
* A SIGALRM  is generated when the timer set by alarm function goes off.
* A SIGABRT signal is generated when a process calls the abort function.

Please visit:
* [Linux PID](http://www.linfo.org/pid.html)
* [Linux Process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux Signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)

## General Objectives

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Directory Files Description

| **File** | **Description** |
|----------|-----------------|
| [0. What is my PID](./0-what-is-my-pid) | Write a Bash script that displays its own PID. |
| [1. List your processes](./1-list_your_processes) | Write a Bash script that displays a list of currently running processes. |
| [2. Show your Bash PID](./2-show_your_bash_pid) | Write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. |
| [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy) | Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash. |
| [4. To infinity and beyond](./4-to_infinity_and_beyond) | Write a Bash script that displays To infinity and beyond indefinitely. |
| [5. Kill me now](./5-kill_me_now) | Write a Bash script that kills 4-to_infinity_and_beyond process. |
| [6. Kill me now made easy](./6-kill_me_now_made_easy) | Write a Bash script that kills 4-to_infinity_and_beyond process wihout using kill or killall |
| [7. Highlander](./7-highlander) | Write a Bash script that displays: To infinity and beyond indefinitely With a sleep 2 in between each iteration and I am invincible!!! when receiving a SIGTERM signal. |
| [8. Beheaded process](./8-beheaded_process) | Write a Bash script that kills the process 7-highlander. |

## Prerequisites

This bash scripts were made and tested using Ubuntu 14.04.3 LTS We recommend you to test this files under this conditions.

## Built With

* Ubuntu 14.04.3 LTS Running on a Virtual Machine "Vagrant"
* GNU Emacs 24.3.1

## AUTHOR

**Luis Miguel Vargas**

* [Github @luismvargasg](https://github.com/luismvargasg)
* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)

## License

Opensource project.

## Acknowledgments

* Project made at Holberton School - Colombia.