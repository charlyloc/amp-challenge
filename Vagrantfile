Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  # VM network settings
  config.vm.network "private_network", ip: "192.168.56.10"
  #config.vm.network "forwarded_port", guest: 80, host: 80  UNCOMMENT To expose port 80 of the vm to the port 80 of the host machine

  # VM Hostname
  config.vm.hostname = "ubuntu-vm"

  # VirtualBox Configuration
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  # Ansible Provisioning
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/main.yml"
    ansible.compatibility_mode = "2.0"
  end

end

