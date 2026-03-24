# agent/tools/scraper.py
from playwright.sync_api import sync_playwright

def scrape_job(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=30000)

        # click cookie accept buttons
        for sel in [
            "button:has-text('Accept')",
            "button:has-text('Accept All')",
            "button:has-text('I Accept')",
            "button:has-text('Allow')",
            "[id*='cookie'] button",
            "[class*='cookie'] button",
            "[class*='consent'] button",
        ]:
            try:
                page.click(sel, timeout=2000)
                page.wait_for_timeout(1000)  # wait for banner to dismiss
                break
            except:
                pass

        title    = page.title()
        body     = page.inner_text("body")
        browser.close()

    # strip cookie text from the top — find where real content starts
    skip_phrases = [
        "Essential Cookies", "Use of Cookies", "Privacy Policy",
        "We use cookies"
    ]
    lines = body.split("\n")
    start_idx = 0
    for i, line in enumerate(lines):
        if any(phrase in line for phrase in skip_phrases):
            # skip ahead ~30 lines past the cookie section
            start_idx = min(i + 30, len(lines))
            break

    cleaned = "\n".join(lines[start_idx:])

    return {
        "url":      url,
        "title":    title,
        "raw_text": cleaned[:8000]
    }