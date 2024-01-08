# vpn-server-management

## How to run the program

Before anything, remember to add your server stuff (hostname, user, SSH key, password, etc.) to config.py

If you want to use your v2ray config you can replace it with config.json. **By default, the existing configuration is used, which is on port 8443 and has 2 client IDs by default.**

After running the program your VPN server will be set up.

**Remember before running the program, select which type of SSH you want to use (with a SSH key or with a password) and comment on the other function. There are two functions: 1-init_ssh_client_with_ssh_key 2-init_ssh_client_with_password**

```
pip install -r requirements.txt
python main.py
```
