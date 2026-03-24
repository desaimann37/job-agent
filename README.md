# Job Application Agent

An agentic AI that automates job applications using Claude + Playwright.

## What it does
Paste a job URL → scrapes JD → extracts structured fields → stores in SQLite

## Stack
- Claude API (Haiku for extraction, Sonnet for resume tailoring)
- Playwright (headless scraping)
- SQLite (application tracker)
- Streamlit (UI — coming Week 3)

## Status
- [x] Week 1 — Scraper + Extractor + DB tracker
- [ ] Week 2 — Claude tool use orchestrator
- [ ] Week 3 — Streamlit dashboard
- [ ] Week 4 — Polish + demo

## Setup
```bash
uv sync
uv run playwright install chromium
cp .env.example .env  # add ANTHROPIC_API_KEY
uv run python test_tracker.py
```
