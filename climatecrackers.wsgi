#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/climatecrackers/")
sys.path.insert(0,"/var/www/climatecrackers/climatecrackers/")

import logging
logging.basicConfig(stream=sys.stderr)

from climatecrackers import app as application
