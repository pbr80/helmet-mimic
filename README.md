# helmet-mimic

Random Pathfinder 2E monster stat blocks for your terminal and MOTD. 

`helmet-mimic` fetches a random creature stat block from the [Archive of Nethys](https://2e.aonprd.com) Pathfinder 2E wiki. Run it standalone to get a monster of the day, or integrate it with your Linux MOTD so every SSH login greets you with a new monster.

## Features

- Random monster stat blocks from all PF2E bestiaries
- Optional Linux MOTD integration via `update-motd.d`
- Minimal dependencies (`beautifulsoup4`, `requests`)

## Requirements

- Python 3.6+
- `beautifulsoup4`
- `requests`

## Installation

```bash
git clone https://github.com/pbr80/helmet-mimic.git
cd helmet-mimic
pip install -r requirements.txt
```

## Usage

### Standalone - get a random monster

```bash
python pathfinder_MOTD.py
```

### MOTD Integration (Optional)

1. Copy both scripts to your MOTD directory:
   ```bash
   sudo cp pathfinder_MOTD.py 20-helmet-mimic /etc/update-motd.d/
   ```
2. Make the helper script executable:
   ```bash
   sudo chmod +x /etc/update-motd.d/20-helmet-mimic
   ```
3. SSH into your machine - you'll see a new monster greeting on every login!

## License

[GNU General Public License](LICENSE)
