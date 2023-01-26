import boto3
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys
import os
import subprocess

polly = boto3.client('polly')

try:
    # Try requesting
    response = polly.synthesize_speech(Text="this is sample text",
                                       OutputFormat="mp3",
                                       VoiceId="Joanna")
    print(response)
except (BotoCoreError, ClientError) as error:
    # Service returned an error - exit application
    print(error)
    sys.exit(-1)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        try:
            # Saving the output to the file as binary stream
            with open("temp/audio.mp3", "wb") as file:
                file.write(stream.read())
        except IOError as error:
            print(error)
            sys.exit(-1)
else:
    print("Could not stream audio")
    sys.exit(-1)

# Play the audio using the platform's default player
audio_file_path = "E:/Users/kubam/OneDrive/Pulpit/python_exercises/pdf_to_speach_aws_polly/temp/audio.mp3"
if sys.platform == "win32":
    os.startfile(audio_file_path)
else:
    # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, audio_file_path])
