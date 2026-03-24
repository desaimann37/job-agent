# test_tracker.py
from agent.tools.scraper import scrape_job
from agent.tools.extractor import extract_job_fields
from db.tracker import init_db, save_job

url    = "https://ciena.wd5.myworkdayjobs.com/en-US/Careers/job/London/Data-Science-Analyst-Intern--Summer-2026-_R030463"
result = scrape_job(url)
fields = extract_job_fields(result["raw_text"])
save_job(fields, url)

# verify it saved
db = init_db()
for row in db["applications"].rows:
    print(row)