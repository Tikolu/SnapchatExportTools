# Code by Tikolu.net

def cancel():
	print("\n\nPress enter to exit...")
	input()
	exit()
	
import json, os
from datetime import datetime

try:
	with open("chat_history.json", encoding="utf8") as f:
		sections = json.load(f)
except:
	print("Error opening 'chat_history.json'")
	cancel()

try:
	os.rmdir("chats")
except:
	pass

try:
	os.mkdir("chats")
except:
	print("'chat' directory already exists")
	print("Delete or move it before continuing")
	cancel()

username = input("Enter username: ") or exit()
print("\nChoose export format:")
print("1 - HTML (Viewable in a web browser)")
print("2 - Plain Text (one message per line)")
print("3 - JSON (split into separate files)")
format = int(input("Enter number [1 - 3]: ") or 1);
if format < 1 or format > 3:
	exit()
print()

chats = {}
counter = 0

for section in sections:
	amount = len(sections[section])
	counter += amount
	print(f"{section} contains {amount} messages")
	for message in sections[section]:
		if "To" in message:
			chat = message.pop("To")
			message["From"] = username
		elif "From" in message:
			chat = message["From"]
		else:
			chat = "Unknown"
		if not chat in chats:
			chats[chat] = []
		message["Type"] = message.pop("Media Type")
		if message["Type"] != "TEXT":
			message.pop("Text", None)
		message["Date"] = int(datetime.timestamp(datetime.strptime(message.pop("Created", message.pop("Date", None)), "%Y-%m-%d %H:%M:%S %Z")))
		chats[chat].append(message)

print(f"\nLoaded {counter} messages in total")

for chat in chats:
	chats[chat] = sorted(chats[chat], key=lambda d: d["Date"])

illegal_chars = "\"\/:*?<>|";

for chat in chats:
	with open(f"chats/{''.join(i for i in chat if i not in illegal_chars)}.{['html','txt','json'][format-1]}", "w", encoding="utf8") as f:
		if format == 1:
			f.write(f"<html><head><title>{chat}</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><style>")
			f.write("""
				body {font-family:sans-serif}
				section[right] {text-align:right}
				section[right] div {margin-left:auto;background-color:unset;border:1px solid #cde}
				div {background-color:#cde;border-radius:0.5em;width:max-content;max-width:80vw;padding:0.5em}
			""")
			f.write("</style></head><body>")
			f.write(f"<h1>{chat}</h1>\n")
			last_date = ""
			for message in chats[chat]:
				timestamp = datetime.utcfromtimestamp(message["Date"])
				date = timestamp.strftime("%A %e %B %Y")
				time = timestamp.strftime("%H:%M:%S")
				if last_date != date:
					f.write(f"<center>{date}</center>\n")
					last_date = date
				f.write(f"<section{' right' if message['From'] == username else ''}>")
				if message["Type"] == "TEXT":
					f.write(f"<div>{message['Text']}</div>")
				else:
					f.write(f"<b>({message['Type']})</b><br>")
				f.write(f"<small>{time}</small>")
				f.write("</section>\n")

		elif format == 2:
			for message in chats[chat]:
				date = datetime.utcfromtimestamp(message["Date"]).strftime("%Y-%m-%d %H:%M:%S")
				f.write(f"{date} - {message['From']}: {message.get('Text', '') if message['Type'] == 'TEXT' else message['Type']}\n")
		elif format == 3:
			f.write(json.dumps(chats[chat], indent=4))

print("Chat export complete")
print(f"\n{len(chats)} chats saved in {['HTML','plain text','JSON'][format-1]} format")
cancel()
