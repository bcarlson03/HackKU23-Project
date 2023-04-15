from note import Note

def main(note):

    # This is the initial prompt that the model will use to generate the response
    prompt = "Please take the following transcript and turn it into a note sheet for a person who can't take notes. It should include all of the main points and should include ALL of the important information in the transcript below. Do NOT leave out anything important. Make sure to separate various section with headers to make sure it's not just a list of bullet points."

    # Adds the transcript
    prompt += note.transcript

    # Gets GPT's response
    response = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    note.summary = response
