import base64
import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/audio?example=audio-in#add-audio-to-your-existing-application

# TODO:
# You need to generate answer in audio format based on the audio message:
#   - Create Client that is similar with OpenAIClients but extracts from message audio (instead of content)
#   - Call API
#   - Get response as base64 content, decode and save as .mp3 file
# ---
# Hints:
#   - Use /v1/chat/completions endpoint
#   - Use gpt-4o-audio-preview model
#   - Use modalities=["text", "audio"]
#   - Use audio={"voice": "ballad", "format": "mp3"}
#   - Similar method to encode audio https://platform.openai.com/docs/guides/images-vision?api-mode=chat&lang=python

with open('question.mp3', 'rb') as f:
    audio = f.read()
    audio = base64.b64encode(audio).decode('utf-8')
    with open('answer.mp3', 'wb') as output_file:
        output_file.write(base64.b64decode(requests.post(
            url=f'{OPENAI_HOST}/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {OPENAI_API_KEY}',
            },
            json={
                "model": "gpt-4o-audio-preview",
                "modalities": ["text", "audio"],
                "audio": {"voice": "alloy", "format": "mp3"},
                "messages": [
                    {
                        "role": 'user',
                        "content": [{"type": 'input_audio', "input_audio": {"data": audio, "format": "mp3"}}]
                    }
                ]
            }
        ).json()['choices'][0]['message']["audio"]['data']))
