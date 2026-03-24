# agent/tools/extractor.py
import anthropic, json, re, os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

def extract_job_fields(raw_text: str) -> dict:
    if len(raw_text.strip()) < 100:
        raise ValueError("Page text too short — likely scraped wrong page")

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system="Return only valid JSON. No markdown, no backticks, no prose.",
        messages=[{"role": "user", "content": f"""
Extract these fields from the job posting below.
Return JSON:
{{
  "company": "company name",
  "role": "job title",
  "location": "location or remote",
  "requirements": ["req1", "req2"],
  "tech_stack": ["python", "aws"]
}}

Job posting:
{raw_text[:4000]}
"""}]
    )

    text = resp.content[0].text.strip()

    # strip markdown backticks if present
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    # extract just the JSON object even if Claude added extra text
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found in response: {text[:200]}")

    return json.loads(match.group())