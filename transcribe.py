"""
Holden Vail
04/14/2023
The purpose of this program is to take an inputted mp3 file and return a transcript of the video in a .txt file
"""

from google.cloud import speech
from google.cloud import storage
import clean_output

given_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.mp3"


def main(note):
    transcript = transcribe(note.path)
    note.transcription = transcript[0]
    note.results = transcript[1]

def transcribe(wav_filename):
    my_uri = upload_file(wav_filename)
    audio = speech.RecognitionAudio(uri=my_uri)
    client = speech.SpeechClient()

    try:
        config = speech.RecognitionConfig(language_code="en", audio_channel_count=2)

    except:
        config = speech.RecognitionConfig(language_code="en", audio_channel_count=1)

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()
    results = []

    for response in response.results:
        results.append(str(response))
    cleaned_output = clean_output.main(results)
    return (cleaned_output, results)

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    response = client.recognize(config=config, audio=audio)

    return response

def upload_file(wav_filename):
    my_client = storage.Client()
    my_bucket = my_client.bucket("note_me_bucket")
    my_blob = my_bucket.blob("note_me_blob")
    my_blob.upload_from_filename(wav_filename)
    return "gs://note_me_bucket/note_me_blob"