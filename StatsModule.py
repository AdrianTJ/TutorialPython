#! usr/bin/python3.7
# Basic things to do with Stats Module in Python. 

import statistics

example = [2,3,4,7,9,12,34,112,64,2,2]

mean = statistics.mean(example)
stdev = statistics.stdev(example)
variance = statistics.variance(example)

print(mean,'    ',stdev,'     ',variance)