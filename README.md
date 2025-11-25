# Ansible Python Web App Deployment

This project demonstrates deploying a Python web application from a control machine to a remote target machine using Ansible.

## 📋 Overview

- **Control Machine (Usman)**: 192.168.1.24
- **Target Machine (Moiz)**: 192.168.1.28
- **Application**: Simple Python HTTP server running on port 8000 (target) and 8001 (control)

## 🚀 Features

- Automated deployment using Ansible
- Python web app with a responsive UI
- Systemd service for automatic startup on target machine
- Runs simultaneously on both machines

## 📁 Project Structure

```
ansible-python-deploy/
├── README.md
├── inventory.ini          # Ansible inventory file
├── deploy.yml            # Ansible playbook
└── app.py                # Python web application
```

## 🔧 Prerequisites

### On Control Machine (Usman - 192.168.1.24)
- Ubuntu/Debian-based system
- Python 3
- Ansible
- SSH access to target machine

### On Target Machine (Moiz - 192.168.1.28)
- Ubuntu/Debian-based system
- SSH server running
- Sudo privileges for the user account

## 📦 Installation

### Step 1: Setup SSH Access

Generate SSH keys on the control machine:
```bash
ssh-keygen -t rsa -b 4096
```

Copy SSH key to target machine:
```bash
ssh-copy-id moiz@192.168.1.28
```

Test connection:
```bash
ssh moiz@192.168.1.28
```

### Step 2: Install Ansible

On the control machine:
```bash
sudo apt update
sudo apt install ansible python3 python3-pip -y
```

### Step 3: Create Project Directory

```bash
cd ~/Desktop
mkdir ansible-python-deploy
cd ansible-python-deploy
```

### Step 4: Create Project Files

Create the following files in your project directory:

1. **inventory.ini**
2. **deploy.yml**
3. **app.py**

(Content for these files is provided in the artifacts)

## 🎯 Usage

### Deploy to Target Machine

Test Ansible connection:
```bash
ansible -i inventory.ini webservers -m ping
```

Deploy the application:
```bash
ansible-playbook -i inventory.ini deploy.yml --ask-become-pass
```

Enter the sudo password for the target machine when prompted.

### Run on Control Machine

In a new terminal:
```bash
cd ~/Desktop/ansible-python-deploy
python3 app.py 8001
```

### Access the Applications

**Control Machine (Usman):**
- Browser: http://192.168.1.24:8001
- Command: `curl http://localhost:8001`

**Target Machine (Moiz):**
- Browser: http://192.168.1.28:8000
- Command: `curl http://localhost:8000`

**From Control Machine to Target:**
- Browser: http://192.168.1.28:8000
- Command: `curl http://192.168.1.28:8000`

## 🔍 Verification

### Check Service Status on Target Machine

SSH into target machine:
```bash
ssh moiz@192.168.1.28
```

Check service status:
```bash
sudo systemctl status webapp
```

View logs:
```bash
sudo journalctl -u webapp -f
```

Check if port is listening:
```bash
sudo netstat -tlnp | grep 8000
```

## 🛠️ Troubleshooting

### Port Already in Use

If you get "Address already in use" error:

```bash
# Find process using the port
sudo lsof -i :8000

# Kill the process (replace PID with actual process ID)
sudo kill -9 PID

# Or kill all processes on port
sudo fuser -k 8000/tcp
```

### SSH Connection Issues

On target machine, ensure SSH is running:
```bash
sudo systemctl start ssh
sudo systemctl enable ssh
```

### Firewall Issues

Allow port through firewall:
```bash
sudo ufw allow 8000/tcp
sudo ufw allow 8001/tcp
sudo ufw reload
```

### Service Won't Start

Check for errors:
```bash
sudo systemctl status webapp
sudo journalctl -u webapp -n 50
```

Restart the service:
```bash
sudo systemctl restart webapp
```

## 🔄 Management Commands

### On Target Machine (Moiz)

**Start service:**
```bash
sudo systemctl start webapp
```

**Stop service:**
```bash
sudo systemctl stop webapp
```

**Restart service:**
```bash
sudo systemctl restart webapp
```

**Enable on boot:**
```bash
sudo systemctl enable webapp
```

**Disable on boot:**
```bash
sudo systemctl disable webapp
```

**View logs:**
```bash
sudo journalctl -u webapp -f
```

### On Control Machine (Usman)

**Stop the application:**
- Press `Ctrl+C` in the terminal running the app

**Run on different port:**
```bash
python3 app.py 8002
```

## 📝 Customization

### Change Port on Target Machine

Edit `deploy.yml` and modify the systemd service ExecStart line:
```yaml
ExecStart=/usr/bin/python3 /opt/webapp/app.py 9000
```

Then update the UFW rule accordingly.

### Modify Web App

Edit `app.py` to customize the HTML, add routes, or change functionality. Redeploy using:
```bash
ansible-playbook -i inventory.ini deploy.yml --ask-become-pass
```

## 🎓 What This Project Demonstrates

1. **Ansible Basics**: Inventory management, playbooks, and tasks
2. **Remote Deployment**: Copying files and managing services remotely
3. **Systemd Integration**: Running Python apps as system services
4. **Network Communication**: Inter-machine HTTP communication
5. **DevOps Practices**: Automation and configuration management

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements.

## 📄 License

This project is open source and available for educational purposes.

## 👥 Authors

- **Usman** - Control Machine Setup
- **Moiz** - Target Machine Deployment

## 🙏 Acknowledgments

- Ansible Documentation
- Python HTTP Server Documentation
- Systemd Service Management

---

**Note**: This is a learning project for demonstrating Ansible deployment concepts. For production use, consider adding:
- SSL/TLS encryption
- Authentication
- Error handling
- Logging
- Security hardening
- Load balancing
- Monitoring
