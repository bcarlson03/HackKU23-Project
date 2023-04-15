import os

def main():
    dirs = os.listdir(".")
    if 'notes' not in dirs:
        os.mkdir('notes')
        print('"notes" folder not found, making one now...')
    if 'audio_files' not in dirs:
        os.mkdir('audio_files')
        print('"audio_files" folder not found, making one now...')