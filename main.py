from note import Note
import os
import transcribe_free
import note_maker_free
import check_folders
import pdf_output

def main():
    """Main function"""
    check_folders.main() # Check if the folders exist
    SLASH = get_slash() # Get the slash for the operating system
    for audio_file in os.listdir(f"audio_files"):
        note_maker(audio_file) # Create a note for each audio file

def note_maker(audio_file):
    """Create a note for each audio file"""
    SLASH = get_slash() # Get the slash for the operating system
    if check_if_mp3(audio_file):
        my_note = Note(audio_file[:-4]) # Create a note object
        my_note.path = f"audio_files{SLASH}{my_note.name}.mp3" # Set the path to the audio file
        transcribe_free.main(my_note) # Transcribes the audio file
        note_maker_free.main(my_note) # Makes the file into a note
        pdf_output.main(my_note) # Generates the final output

def check_if_mp3(audio_file):
    """Check if the file is an mp3 file"""
    if audio_file[-3:] == 'mp3': # Check if the file is an mp3 file
        return True
    else:
        return False
    
def get_slash():
    """Get the slash for the operating system"""
    op_sys = os.name
    if op_sys == 'Darwin' or op_sys == 'Linux': # Mac or Linux
        SLASH = '/'
    else:
        SLASH = fr'\'' # Windows
    return SLASH

main()