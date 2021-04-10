# helmet-mimic
helmet-mimic consists of two files
1. **helmet-mimic.py**: python script that pulls a random Pathfinder 2E creature from the 
   [Archives of Nethys](https://2e.aonprd.com)  
2. **20-helmet-mimic**: bash script that calls the python version. Placed in /etc/update-motd/ will allow it to be 
   run on ssh login.

## Installation (Debian/Ubuntu):
1. Edit '20-helmet-mimic', change path to where you saved the python script  
   `nano 20-helmet-mimic`
2. Copy '20-helmet-mimic' to /etc/update-motd/ (requires sudo permission to do so)  
`sudo cp 20-helmet-mimic /etc/update-motd/`

Wait approx 10 minutes for update-motd to update. Enjoy.
