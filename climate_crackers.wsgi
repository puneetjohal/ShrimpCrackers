#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/climate_crackers/")
sys.path.insert(0,"/var/www/climate_crackers/climate_crackers/")

import logging
logging.basicConfig(stream=sys.stderr)

from climate_crackers import app as application
