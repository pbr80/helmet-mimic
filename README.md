# helmet-mimic
helmet-mimic consists of two files
1. **helmet-mimic.py**: python script that pulls a random Pathfinder 2E creature from the [Archives of Nethys](https://2e.aonprd.com)  
2. **20-helmet-mimic.sh**: bash script that calls the python version. Placed in /etc/update-motd/ will allow it to be run on ssh login.

## Installation (Debian/Ubuntu):
1. Copy '20-helmet-mimic.sh' to /etc/update-motd/ (requires sudo permission to do so)  
`sudo cp 20-helmet-mimic.sh /etc/update-motd/`

Wait approx 10 minutes for update-motd to update. Enjoy.
