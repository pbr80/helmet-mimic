# helmet-mimic Project
Python script that pulls a random stat block from Pathfinder 2E bestiary hosted at [Archive of Nethys](https://2e.anonprd.com).  
Can also be used to append your Linux MOTD banner.

## Project consists of two files:
1. **'helmet-mimic.py'** : simple python script that pulls the stat block. Can be run as-is. 
2. **'20-helmet-mimic'** : (optional) bash script to update your MOTD banner. Requires sudo access to use.

### 20-helmet-mimic (optional)
Placing 20-helmet-mimic in /etc/update-motd/ will allow it to be run on ssh login.

#### Installation (Debian/Ubuntu):
1. Edit '20-helmet-mimic'. Set path in the script to point to the python script location  
   `editor 20-helmet-mimic`
2. Copy '20-helmet-mimic' to /etc/update-motd/ (requires sudo permission to do so)  
`sudo cp 20-helmet-mimic /etc/update-motd/`

Wait approx 10 minutes for update-motd to update. Enjoy.
