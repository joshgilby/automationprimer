sudo apt -y update && sudo apt -y upgrade
sudo apt -y install git docker.io docker-compose-v2 python3.12-venv
sudo usermod -a -G docker `whoami`
sudo reboot