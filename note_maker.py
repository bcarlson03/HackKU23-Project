from note import Note
import gpt

def main(note):
    
    # This is the initial prompt that the model will use to generate the response
    prompt = "Please take the following transcript and turn it into a note sheet for a person who can't take notes. It should include all of the main points and should include ALL of the important information in the transcript below. Do NOT leave out anything important. Make sure to separate various section with headers to make sure it's not just a list of bullet points."

    # Adds the transcript
    prompt += note.transcription

    # Gets GPT's response
    response = gpt.main(prompt)

    note.summary = response
