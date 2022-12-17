import re

TARGET_FILE = "actualInput.txt"
OFFSET = 1649857

sensors = []
beacons = []
minVal = 0
with open(TARGET_FILE, 'r') as file:
	for i, line in enumerate(file):
		re_output = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
		
		sensor = list(map(int, re_output[0]))
		beacon = list(map(int, re_output[1]))

		sensor = [x + OFFSET for x in sensor]
		beacon = [x + OFFSET for x in beacon]

		print(f"Set {i+1}: Sensor @ {sensor}, Beacon @ {beacon}")

		localMin = min(sensor) if min(sensor) < min(beacon) else min(beacon)
		minVal = localMin if localMin < minVal else minVal
	
		sensors.append(sensor)
		beacons.append(beacons)

adjFactor = abs(minVal)

