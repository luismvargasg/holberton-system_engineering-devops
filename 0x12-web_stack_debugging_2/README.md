# Web stack debugging #2

> This directory contains all the tasks of the project "0x12. Web stack debugging #2" at [Holberton School](https://www.holbertonschool.com "Holberton School.")

[![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1)

## Table of Contents

- [Web stack debugging #2](#web-stack-debugging-2)
  - [Table of Contents](#table-of-contents)
  - [Basic Info](#basic-info)
    - [w](#w)
    - [history](#history)
    - [top](#top)
    - [df](#df)
    - [netstat](#netstat)
    - [Machine](#machine)
  - [Directory Files Description](#directory-files-description)
  - [Built With](#built-with)
  - [AUTHOR](#author)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Basic Info

### w

* shows server uptime which is the time during which the server has been continuously running
* shows which users are connected to the server
* load average will give you a good sense of the server health - (read more about load here and here)

### history

* shows which commands were previously run by the user you are currently connected to
* you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
* where you might want to start your debugging work

### top

* shows what is currently running on this server
* order results by CPU, memory utilization and catch the ones that are resource intensive

### df

* shows disk utilization

### netstat

* what port and IP your server is listening on
* what processes are using sockets
* try netstat -lpn on a Ubuntu machine

### Machine

Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

Does the server have free disk space? - df
Is the server able to keep up with CPU load? - w, top, ps
Does the server have available memory? free
Are the server disk(s) able to keep up with read/write IO? - htop
If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

free up resources (stop process(es) or reduce their resource consumption)
increase the machine resources (adding memory, CPU, disk space…)
distributing the resource usage to other machines

## Directory Files Description

| **File** | **Description** |
|----------|-----------------|
| [0. Run software as another user](./0-iamsomeonelese) | Bash script that accepts one argument and should run the whoami command under the user passed as an argument. |
| [1. Run Nginx as Nginx](./1-run_nginx_as_nginx) | Bash script that configures the container to fit some requirements. |
  
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
