import base64
from openai import OpenAI

client = OpenAI()

async def to_speech(text, background_tasks):
    completion = client.chat.completions.create(
        model="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
    filepath = f"/tmp/{uuid.uuid4()}.wav"
    with open(filepath, "wb") as f:
        f.write(wav_bytes)

    background_tasks.add_task(delete_file, filepath)

    return filepath
