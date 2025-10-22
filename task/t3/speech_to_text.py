import json

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/speech-to-text?lang=curl

#TODO:
# You need to transcribe 'codeus_audio.mp3':
#   - Create Client that will go to transcriptions OpenAI API
#   - Call API and provide file (pay attention that you work with 'multipart/form-data')
#   - Get response with transcription
# ---
# Hints:
#   - Use /v1/audio/transcriptions endpoint
#   - Use whisper-1 or gpt-4o-transcribe model
with open('codeus_audio.mp3', "rb") as file:
    print(requests.post(
        'https://api.openai.com/v1/audio/transcriptions',
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",

        },
        data={
            "model": "gpt-4o-transcribe",
            "response_format": "text"
        },
        files={
            "file": file
        }
    ).text)