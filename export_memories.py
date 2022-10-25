# Code by Tikolu.net

def cancel():
	print("\n\nPress enter to exit...")
	input()
	exit()

try:
	import requests
except ImportError:
	print("Requests library not installed")
	print("Please intall it by running 'python -m pip install requests'")
	cancel()

import json, re, os
from datetime import datetime

try:
	with open("memories_history.json", encoding="utf8") as f:
		memories = json.load(f)
		memories = memories["Saved Media"]
except:
	print("Error opening 'chat_history.json'")
	cancel()

length = len(memories)
print(f"{length} memories found in file\n")
start = 0

try:
	os.mkdir("memories")
except FileExistsError:
	print("'memories' directory already exists")
	print("Delete it, or enter starting number below")
	while True:
		start = int(input("Enter number [default 0]: ") or 0)
		if start > length:
			print("Number cannot exceed memories count")
		else:
			break

print("\nStarting export. Preszz Ctrl+C to cancel.")

counter = 0

for memory in memories:
	counter += 1
	if counter < start:
		continue

	print(f"Downloading {memory['Media Type']}\t{counter} of {length}\t{(counter-start)/(length-start):.2%} done")

	while True:
		try:
			link = requests.post(memory['Download Link'])
			link = link.text
			if not link.startswith("http"):
				print("Error connecting to Snapchat")
				cancel()
			file_name = re.findall("(?<=\/)[0-9a-f\-]*\.[a-z0-9]{3,4}(?=\?)", link)[0]
		except KeyboardInterrupt:
			print("Export cancelled by user")
			cancel()
		except:
			print("Connection error. Retrying...")
			continue
		break
	
	
	while True:
		try:
			file = requests.get(link).content
		except KeyboardInterrupt:
			print("Export cancelled by user")
			cancel()
		except:
			print("Download error. Retrying...")
			continue
		break

	date = datetime.strptime(memory["Date"], "%Y-%m-%d %H:%M:%S %Z")
	date = int(datetime.timestamp(date))

	path = f"memories/{file_name}"

	with open(path, "wb") as f:
		f.write(file)
	os.utime(path, times = (date, date))

print("Memories export complete")
cancel()