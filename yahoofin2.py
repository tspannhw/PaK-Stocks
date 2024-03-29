import random
import time
from yahoo_fin import stock_info as si
from yahoo_fin import news  as sn
from yahoo_fin import options as so
from datetime import datetime, timezone
import time
import logging
import sys
import subprocess
import os
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import time
import psutil
import uuid
import requests
from time import sleep
from math import isnan
from subprocess import PIPE, Popen
import socket
import argparse
import os.path
import re
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from time import sleep
from math import isnan
import datetime
import subprocess
import sys
import os
from subprocess import PIPE, Popen
import traceback
import math
import base64
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import json

StockNames = ["ORCL", "SAP", "CSCO","GOOG","ETH-USD", "NVDA", "AMZN",  "IBM", "NFLX"]

n = 1

producer = KafkaProducer(key_serializer=str.encode, value_serializer=lambda v: json.dumps(v).encode('ascii'),bootstrap_servers='kafka:9092',retries=3)

while n > 0:
	stockname = random.choice(StockNames)
	ts = time.time()
	uuid_key = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
	try:
		producer.send("yahoofinstocks", key=uuid_key, value={'uuid': uuid_key, 'stockname': stockname, 'ts': float(int(ts * 1000)), 'currentts': float(strftime("%Y%m%d%H%M%S",gmtime())), 'stockvalue': float(si.get_live_price(stockname)) })
		producer.flush()
	except:
		print("Bad stockname " + stockname)

	print(stockname)
	time.sleep(1)
