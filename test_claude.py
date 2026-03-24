import anthropic, os
from dotenv import load_dotenv

load_dotenv()  # make sure this is called before Anthropic client init

client = anthropic.Anthropic()  # auto-reads ANTHROPIC_API_KEY from env

resp = client.messages.create(
    model="claude-haiku-4-5-20251001",  # use Haiku for testing — cheaper
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}]
)
print(resp.content[0].text)