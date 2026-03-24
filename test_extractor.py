from agent.tools.scraper import scrape_job
from agent.tools.extractor import extract_job_fields

# job description URL, not the /apply URL
url = "https://ciena.wd5.myworkdayjobs.com/en-US/Careers/job/London/Data-Science-Analyst-Intern--Summer-2026-_R030463"

result = scrape_job(url)
print(f"Scraped {len(result['raw_text'])} chars")
print(result['raw_text'][:300])  # preview what was scraped
print("---")

fields = extract_job_fields(result["raw_text"])
print(fields)