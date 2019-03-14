# -*- coding: utf-8 -*-

import subprocess
import time

cmd = "python /opt/full_link/utils/get_es_history.py"


while True:

    subprocess.getstatusoutput(cmd)
    time.sleep(10)
