"""
Holden Vail
04/14/2023

The purpose of this program is to take an inputted mp3 file and return a transcript of the video in a txt file

"""

from google.cloud import speech
from google.cloud import storage


given_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.mp3"

mp3_filename = "second.mp3"

def main(note):
    transcribe(note.path)

def transcribe(mp3_filename=mp3_filename):
    my_uri = upload_file()
    config = speech.RecognitionConfig(language_code="en")
    audio = speech.RecognitionAudio(uri=my_uri)
    response = speech_to_text(config, audio)
    results = []
    for response in response.results:
        results.append(str(response))
    out_file = open("results.txt", "w")
    for line in results:
        out_file.write(f"{line}\n")
    out_file.close()
    return out_file 

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response

def upload_file():
    my_client = storage.Client()
    my_bucket = my_client.bucket("note_me_bucket")
    my_blob = my_bucket.blob("note_me_blob")
    my_blob.upload_from_filename(mp3_filename)
    return "gs://note_me_bucket/note_me_blob"
