# SSH

> This directory contains all the tasks of the project "0x0B. SSH" at [Holberton School](https://www.holbertonschool.com "Holberton School.")

[![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1)

## Table of Contents

- [SSH](#ssh)
  - [Table of Contents](#table-of-contents)
  - [Learning Objectives](#learning-objectives)
  - [Basic info](#basic-info)
  - [Directory Files Description](#directory-files-description)
  - [Built With](#built-with)
  - [AUTHOR](#author)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Learning Objectives

* What is a server.
* Where servers usually live.
* What is SSH.
* How to create an SSH RSA key pair.
* How to connect to a remote host using an SSH RSA key pair.
* The advantage of using #!/usr/bin/env bash instead of /bin/bash.

## Basic info

Please visit:
* [Server](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config file](https://www.ssh.com/ssh/config/)

## Directory Files Description

| **File** | **Description** |
|----------|-----------------|
| [0. Use a private key](./0-use_a_private_key) | Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu. |
| [1. Create an SSH key pair](./1-create_ssh_key_pair) | Write a Bash script that creates an RSA key pair. |
| [2. Client configuration file](./2-ssh_config) | Configure the file for the local machine so that you can connect to a server without typing a password. |
| [3. Let me in!](/0x0B-ssh) | Add the SSH public key below to your server so that we can connect using the ubuntu user. |
| [4. Client configuration file \(w/ Puppet\)](./4-puppet_ssh_config.pp) | Set up your client SSH configuration file so that you can connect to a server without typing a password. |

## Built With

* Ubuntu 14.04.3 LTS Running on a Virtual Machine "Vagrant"
* GNU Emacs 24.3.1
* Puppet 3.4.3

## AUTHOR

**Luis Miguel Vargas**

* [Github @luismvargasg](https://github.com/luismvargasg)
* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)

## License

Opensource project.

## Acknowledgments

* Project made at Holberton School - Colombia.
