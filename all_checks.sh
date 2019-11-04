#!/bin/bash
python bgp_apply_config.py &
wait
python sh_ip_int_br.py &
python sh_ip_route.py &
wait
python sh_ip_bgp_sum.py
python sh_disk.py

