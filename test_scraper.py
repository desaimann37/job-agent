# test_scraper.py
"""
from agent.tools.scraper import scrape_job

result = scrape_job("https://careers.google.com/jobs/results/")
print(result["title"])
print(result["raw_text"][:500])
"""

# test_scraper.py - update to a specific job URL
from agent.tools.scraper import scrape_job

# paste any specific job listing URL here
result = scrape_job("https://ciena.wd5.myworkdayjobs.com/Careers/job/London/Data-Science-Analyst-Intern--Summer-2026-_R030463?utm_source=Simplify&ref=Simplify")

print("Title:", result["title"])
print("---")
print(result["raw_text"][:1000])