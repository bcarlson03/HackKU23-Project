from note import Note

def main(note):
    # This is the initial prompt that the model will use to generate the response
    prompt = "Please take the following transcript and turn it into a note sheet for a person who can't take notes. It should include all of the main points and should include ALL of the important information in the transcript below. Do NOT leave out anything important. Make sure to separate various section with headers to make sure it's not just a list of bullet points."

    # Adds the transcript
    prompt += note.transcription

    # Gets GPT's response
    response = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae turpis massa sed elementum tempus egestas sed. Facilisi nullam vehicula ipsum a arcu cursus vitae congue. Urna cursus eget nunc scelerisque viverra. Tortor at risus viverra adipiscing at. Viverra maecenas accumsan lacus vel facilisis volutpat est velit egestas. Interdum posuere lorem ipsum dolor sit amet. Amet dictum sit amet justo donec enim. Mi proin sed libero enim sed faucibus. Cras ornare arcu dui vivamus arcu felis. Netus et malesuada fames ac turpis egestas sed tempus urna. Ultrices neque ornare aenean euismod elementum nisi quis. Amet consectetur adipiscing elit pellentesque habitant."

    note.summary = response
