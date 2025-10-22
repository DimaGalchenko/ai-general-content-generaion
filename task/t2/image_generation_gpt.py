import base64
from datetime import datetime

from task.client import OpenAIClient
from task.constants import OPENAI_HOST, OPENAI_API_KEY
import requests

# https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1&api=image&multi-turn=imageid
# ---
# Request:
# curl -X POST "https://api.openai.com/v1/images/generations" \
#     -H "Authorization: Bearer $OPENAI_API_KEY" \
#     -H "Content-type: application/json" \
#     -d '{
#         "model": "gpt-image-1",
#         "prompt": "smiling catdog."
#     }'
# Response:
# {
#   "created": 1699900000,
#   "data": [
#     {
#       "b64_json": Qt0n6ArYAEABGOhEoYgVAJFdt8jM79uW2DO...,
#     }
#   ]
# }

#TODO:
# You need to create some images with `gpt-image-1` model:
#   - Generate an image with 'Smiling catdog'
#   - Decode and save it locally
# ---
# Hints:
#   - Use OpenAIClient to connect to OpenAI API
#   - Use /v1/images/generations endpoint
#   - The image will be returned in base64 format

# client = OpenAIClient(f"{OPENAI_HOST}/v1/images/generations")
#
# result = client.call(
#     model="gpt-image-1",
#     prompt='Smiling catdog'
# )
#
# image_base64 = result['data'][0]['b64_json']
# image_bytes = base64.b64decode(image_base64)
#
# with open("result_image_gpt.png", "wb") as f:
#     f.write(image_bytes)


with open("pavlusha.png", "rb") as image_file:
    files = {
        "image": ("pavlusha.png", image_file, "image/png"),
    }

    data = {
        "model": "gpt-image-1",
        "prompt": "Do not alter the man's facial features or expression. Keep his face identical to the original. Only change his clothing and background to make him appear like a wealthy, confident businessman — wearing a stylish suit and accessories."
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    response = requests.post(url=f"{OPENAI_HOST}/v1/images/edits", headers=headers, files=files, data=data)

    if response.ok:
        result = response.json()
        image_base64 = result["data"][0]["b64_json"]
        image_bytes = base64.b64decode(image_base64)

        with open("good_pavlusha.png", "wb") as f:
            f.write(image_bytes)
    else:
        print(response.text)