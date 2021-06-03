# helmet-mimic.py
'Monster of the Day' inspired script. Pulls a random stat block from Pathfinder 2E bestiary hosted at [Archive of Nethys](https://2e.anonprd.com).

The format was perfect for MOTD for personal use systems.

Project consists of two files:
1. **helmet-mimic.py**: python script that's doing the work 
2. **20-helmet-mimic**: (optional) bash script to set up the MOTD. Requires sudo access to modify MOTD.
   
## 20-helmet-mimic
This is optional as it is not necessary to run helmet-mimic.py.  

Placing 20-helmet-mimic in /etc/update-motd/ will allow it to be run on ssh login.

Installation (Debian/Ubuntu):
1. Edit '20-helmet-mimic', edit path in the script to where you saved the python script  
   `nano 20-helmet-mimic`
2. Copy '20-helmet-mimic' to /etc/update-motd/ (requires sudo permission to do so)  
`sudo cp 20-helmet-mimic /etc/update-motd/`

Wait approx 10 minutes for update-motd to update. Enjoy.
