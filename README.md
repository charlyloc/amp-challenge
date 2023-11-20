# amp-challenge

This is a web-server application written in python and using Flask as the web app framework.
The application consists on 4 containers, each one running an independent function:

- Web App in python/flask (2 replicas)
- nginx load balancer
- mysql database

The containers are executed inside a VM using Vagrant and VirtualBox
The VM is provisioned using Ansible.

## Requirements

To execute the app you need to have installed:

- Vagrant (Vagrant 2.4.0 used)
- Virtualbox (6.1.38 used)
- Ansible (ansible [core 2.15.6] used)
- Python (Python 3.10.12 used)

## How-to

Clone the repository and execute "vagrant up", this will create and start the VM, provision it, and execute the docker compose file that spins up the containers
To expose the port 80 of the VM to the port 80 of the host machine, uncomment this line in the Vagrantfile:

"config.vm.network "forwarded_port", guest: 80, host: 80"

Test the app by doing a curl to:

- curl http://localhost/greetings
- curl -X POST http://localhost/messages
