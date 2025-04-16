import subprocess
from google import genai

def vibe(prompt: str, key: str):
    client = genai.Client(api_key = key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="Respond to this only with PYTHON 3.5 code that can be run in the python compiler, do not add anything other than code. The code should run any function necessary and at the end return to the stdout a value. This is the prompt: " + prompt
    )

    lines = response.text.splitlines()
    middle_lines = lines[1:-1]
    result = '\n'.join(middle_lines)
    return subprocess.run(["python", "-c", result ], capture_output=True, text=True).stdout.strip()