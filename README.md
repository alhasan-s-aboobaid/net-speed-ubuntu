# Netspeed ubuntu :earth_asia:
A python code to read and show transmitted and received bytes for every network interface

#The key features of the script include:
- Reading and parsing network statistics from the /proc/net/dev file.
- Differentiating data columns into received and transmitted categories.
- Storing and displaying the data in a structured dictionary format, mapping each network interface to its respective statistics.
- Periodic execution of the data retrieval function, leveraging the schedule library to ensure the task runs continuously at the specified interval.

This script is useful for system administrators and network engineers who need to monitor network interface performance and diagnose potential issues in real time.



# Usage :loudspeaker:
```
pip3 install schedule
```

```
python3 speed_info.py
```
Result example :computer:
```
{'enp2s0': {},
 'lo': {'recv_bytes': '109199',
        'recv_compressed': '0',
        'recv_drop': '0',
        'recv_errs': '0',
        'recv_fifo': '0',
        'recv_frame': '0',
        'recv_multicast': '0',
        'recv_packets': '1032',
        'trans_bytes': '109199',
        'trans_carrier': '0',
        'trans_colls': '0',
        'trans_compressed': '0',
        'trans_drop': '0',
        'trans_errs': '0',
        'trans_fifo': '0',
        'trans_packets': '1032'},
 'wlp4s0': {}}

```
