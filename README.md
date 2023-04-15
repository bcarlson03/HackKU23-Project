# HackKU23-Project
The HackKU23 project by Blake Carlson, Michael Stang, Holden Vail, and Logan Smith. 

Our project is ToBeNamed. The program takes an audio clip and outputs a pdf that is a formatted and condensed outline of the information spoken in the audio. Its intended use is to generate notes for people who are unable to take physical notes on their own. It provides a way for these students to have their own study materials in a much more reliable and accessible way.

Our program works by first taking an mp3 file and uses the Google Cloud API to generate a transcription of the audio. The transcription is stored as a .txt file. The text file is then given to the ChatGPT API and is prompted to create a summary of the transcription which will be used as notes. The response will be stored as a string. The transcript and summarization is then used to create a pdf which contains the formatted notes as well as the original transcript of the audio file.   
