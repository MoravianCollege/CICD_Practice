sudo systemctl stop cicd
cd /home/ubuntu/CICD_Practice/ && git pull origin master
sudo systemctl start cicd
