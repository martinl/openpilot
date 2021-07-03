#!/usr/bin/env python3
import os
import requests

from selfdrive.test.process_replay.test_processes import segments
from selfdrive.test.process_replay.process_replay import CONFIGS

BASE_URL = "https://github.com/martinl/openpilot-ci/raw/master/process_replay/"

process_replay_dir = os.path.dirname(os.path.abspath(__file__))
ref_commit = open(os.path.join(process_replay_dir, "ref_commit")).read().strip()

for car_brand, segment in segments:
  for cfg in CONFIGS:
    cmp_log_url = (BASE_URL + "%s/%s_%s_%s.bz2" % (ref_commit, segment.replace("|", "_"), cfg.proc_name, ref_commit))
    cmp_log_fn = os.path.join(process_replay_dir, "%s_%s_%s.bz2" % (segment, cfg.proc_name, ref_commit))
    r = requests.get(cmp_log_url)
    if r.status_code == 200:
      with open(cmp_log_fn, 'wb') as f:
        f.write(r.content)
    else:
      print("Failed to download: " + cmp_log_url)
