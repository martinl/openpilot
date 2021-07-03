#!/usr/bin/env python3
import os
import requests
from selfdrive.test.process_replay.regen import regen_and_save

BASE_URL = "https://github.com/martinl/openpilot-ci/raw/master/"

custom_segments = [
  ("SUBARU", "05bca04dfbdca165|2021-07-01--21-54-54--1"),      # SUBARU.IMPREZA
  ("SUBARU", "8bf7e79a3ce64055|2021-05-24--09-36-27--1"),      # SUBARU.IMPREZA_2020
  ("SUBARU", "7393c1b180278950|2021-06-29--13-00-40--1"),      # SUBARU.OUTBACK
]

new_segments = []

def download_route(url, path, filename):

  r = requests.get(url)
  print("Downloading: " + url)
  if r.status_code == 200:
    if not os.path.exists(path):
      os.makedirs(path)
    with open(filename, 'wb') as f:
      f.write(r.content)
  else:
    print("Failed to download: " + rlog_url)

for car_brand, segment in custom_segments:

  route_name, segment_num = segment.rsplit("--", 1)
  segment_idx = int(segment_num)
  log_path = "%s/%s" % (route_name.replace("|", "/"), segment_num)
  rlog_fn = log_path + "/rlog.bz2"
  fcam_fn = log_path + "/fcamera.hevc"
  rlog_url = BASE_URL + rlog_fn
  fcam_url = BASE_URL + fcam_fn

  download_route(fcam_url, log_path, fcam_fn)
  download_route(rlog_url, log_path, rlog_fn)

  relr = regen_and_save(route_name, segment_idx, upload=False, use_route_meta=False)
  print("\n\n", "*"*30, "\n\n")
  print("New route:", relr, "\n")
  relr = relr.replace('/', '|')
  new_segments.append(f'("{segment[0]}", "{relr}"), ')

print('COPY THIS INTO test_processes.py')
for seg in new_segments:
  print(seg)

