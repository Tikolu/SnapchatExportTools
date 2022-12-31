# SnapchatExportTools
Python scripts for exporting memories and conversations from your Snapchat account

## Installation
### Python
* Download Python version 3.6 or greater from [here](https://python.org/downloads).
* At the end of the installer, be sure to select "Add Python to Path".
### Requests
* The Requests library is only required to export memories.
* Install it by running the following command in your terminal / Command Prompt.
> `python -m pip install requests`

## Downloading the scripts
* Download all the code from [here](https://github.com/Tikolu/SnapchatExportTools/archive/refs/heads/main.zip).
* Extract the ZIP file. The scripts can then be opened directly (they contain a simple command line interface).

## Downloading your Snapchat data
* Navigate to [accounts.snapchat.com/accounts/downloadmydata](https://accounts.snapchat.com/accounts/downloadmydata) and sign in.
* Scroll to the bottom of the page, enter and confirm any email addres. Note that this does not have to match the email on your account, nor does this have to be an email you have access to.
* Make sure to disable "Filter your export by date range" in order to download all of the data.
* Click "Submit Request" and wait for your file to be generated. Waiting times vary greatly depending on how much data exists on your account.
* After your data is ready for download, a `mydata~...zip` link will show up at the top of the page. (refreshing the page is required to see the link)
* Click on the link to download the ZIP file. Extract it and open the "json" folder located within.
* Once in the folder, copy the two files, `memories_history.json` and `chat_history.json` and paste them into the same folder as the Python scripts downloaded earlier.

## Usage
### Memories
* Open `export_memories.py` and the script will start downloading all memories saved in the `memories_history.json` file, saving them to the `memories` folder.
* Images are saved as JPG files, videos are saved as MP4 files.
* The actual date and time of each file is also saved, so memories can be easily imported into a service such as Google Photos without messing up file order. 
* Files are only available for export for 7 days since downloading the data from Snapchat. After this period of time has elapsed, you will need to submit another request and download a new ZIP file of you have still not exported all of your files.
* Please note: Some (especially older) videos file are saved in the `mp4v` codec, which might not play correctly.
  * [VLC Media Player](https://videolan.org/vlc) can open these files.
  * The following `ffmpeg` command can be used to save the first frame of such files as a normal JPG image:
  * > `ffmpeg -i filename.mp4 -vf "select=eq(n\,0)" -q:v 3 filename.jpg`

### Chats
* Open `export_memories.py` and enter your Snapchat username.
* Choose the preferred output format by entering the corresponding number (HTML is recommended).
* The script will load all messages from the `chat_history.json` file, split them into separate conversations, sort by date and save to files in the `chats` folder.
* Only text messages are exported, as Snapchat does not provide sent images, videos or voice messages.

## Feedback, questions, problems
All can be reported to [Tikolu](https://tikolu.net/contact).

## Credits
All code by [Tikolu](https://tikolu.net). Special thanks to Anna Z. for inspiration, testing and mental support.
