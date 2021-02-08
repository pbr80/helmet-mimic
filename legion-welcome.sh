#! /bin/bash
# by Patrick Brady
# See:
# https://github.com/pbr80/helmet-mimic
# Changes linux welcome banner to a random 'Monster of the Day' from Pathfinder 2E Bestiary
# Used in conjunction with helmet-mimic.py

script='helmet-mimic.py'
motd='101-helmet-mimic-motd'
touch $motd
python $script > $motd
cp $motd /etc/update-motd.d
