# HackKU23 Project

[INSERT NAME HERE] is an AI-Powered Note taking tool that can automate the note-taking process. Simply let it listen in on lectures, meetings, seminars, and more, and it will automatically create refined notes and full transcriptions to help those who prefer not to take notes (but still would want them), and more importantly, help those who can't take notes on their own.

The process is very simple, simply install the files above using:

'''
git clone git@github.com:bcarlson03/HackKU23-Project.git
'''

Navigate to the repo and run

'''
python -m pip install -r requirements.txt
'''

Upon first running main.py two folders will be created, one named "audio_files" and one named "notes."

Once those folders have been created (or if you create them) place your audio files in the "audio_files" folder and run main.py again.

Give it time to process and it should output one .pdf in the "notes" folder for each .mp3 in the "audio_files" folder.

This is a project created for HackKU23 created by Blake Carlson, Michael Stang, Holden Vail, and Logan Smith. 

Our program works by first taking an mp3 file and uses the Google Cloud API to generate a transcription of the audio. The transcription is stored as a .txt file. The text file is then given to the ChatGPT API and is prompted to create a summary of the transcription which will be used as notes. The response will be stored as a string. The transcript and summarization is then used to create a pdf which contains the formatted notes as well as the original transcript of the audio file.   
