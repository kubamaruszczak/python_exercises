import PyPDF2
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys
import os
import subprocess
from tempfile import gettempdir


def get_speach_file(text: str):
    polly = boto3.client('polly')
    try:
        # Try requesting
        response = polly.synthesize_speech(Text=text,
                                           OutputFormat="mp3",
                                           VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        # Service returned an error - exit application
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            audio_file_path = os.path.join(gettempdir(), "audio.mp3")

            try:
                # Saving the output to the file as binary stream
                with open(audio_file_path, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(audio_file_path)
    else:
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, audio_file_path])


def get_pdf_file_contents(filepath: str) -> str:
    file_contents = ""

    try:
        with open(filepath, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                file_contents += f"{page.extract_text()}\n"
    except (FileNotFoundError, FileExistsError) as error:
        print(error)
        sys.exit(-1)

    return file_contents

pdf_contents = get_pdf_file_contents("pdfs/sample.pdf")
print(pdf_contents)
get_speach_file("this is sample text")
