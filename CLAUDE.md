# Project: COVID-19 News Metadata Extraction

## How I want help on this project

**I am writing the code myself.** My goal is to learn by doing, not to have a
working script handed to me. Please default to:

- Explaining concepts (e.g. how structured output / tool calling works, what a
  Pydantic model is doing, how a given library's API is shaped)
- Giving **similar-but-not-identical** examples to what I'm building, so I can
  adapt the pattern myself rather than copy-paste a solution
- Pointing me to relevant docs, course chapters, articles, or library
  documentation I should read
- Reviewing/debugging code I've already written, and explaining *why* something
  is wrong, not just fixing it
- Search-related help (finding articles, checking facts) - that part's fine to do
  directly, it's not the "code I'm learning" part of the assignment

**Please do not write the actual project code for me** (the extraction script,
the schemas, the fear-score logic, etc.) unless I specifically ask you to write
something directly. Default to teaching/pointing/reviewing, not producing.


## Background

This is a part-time job assignment. The task (from handwritten notes, originally in
Slovenian) is:

- Find 10-20 news articles about COVID-19, roughly spanning the beginning of the
  pandemic (China, Dec 2019) through around summer 2020 (China -> Italy/Bergamo ->
  Slovenia timeline).
- Write a program that extracts metadata from each article: number of infected,
  deaths, recovered, hospitalized, etc.
- For each article, also produce a "fear score" (1-10) estimating how much fear/alarm
  the article's language and framing would cause a reader.

## Current status

- 11 articles selected and saved (3 Slovenian, rest international - China, Italy,
  UK, USA, Europe-wide coverage), spanning Feb-July 2020.
- Articles live in the `articles/` subfolder as `.txt` files, named
  `{ID}_{country}_{short-slug}.txt` (e.g. `01_china_wuhan_lockdown.txt`), each with a
  header block (`SOURCE`, `DATE`, `URL`, then `---`, then the article body).
- A spreadsheet tracker (`covid_article_tracker.xlsx`) logs each article's ID,
  milestone, country, source, language, date, URL, and collection status.
- Not yet built: the extraction script itself.

## Planned approach

1. **Data extraction first, fear score second, as separate steps.** Build and test
   a structured-output extraction (case counts, deaths, etc.) using a Pydantic
   schema, independent from the fear-score logic. Get this working reliably before
   touching fear scoring. This keeps debugging simpler (precise fact-extraction vs.
   fuzzy judgment task don't get tangled together) and lets each piece be iterated
   on independently.
2. Only once both pieces work individually would they possibly be merged into a
   combined schema/single call - not before.
3. Structured output will be done via a free-tier LLM API (provider TBD - Groq,
   Gemini, or OpenRouter) using Pydantic schemas, likely with the `instructor`
   library or the provider's native structured-output/function-calling support.

## IMPORTANT: how the fear score will work is NOT decided yet

Do not design, scaffold, or make architectural decisions about the fear-score
system ahead of time. No schema, no scoring rubric, no prompt structure for it
should be assumed or pre-built. This will be figured out deliberately, later, once
data extraction is solid. If asked about it, discuss options/tradeoffs when asked,
but don't pre-emptively build toward one design.

