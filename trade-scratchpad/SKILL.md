---
name: trade-scratchpad
description: Save and organize trade ideas, chart observations, and market notes on your phone. Review them later at your desk. All data stored locally.
---

# Trade Scratchpad

## Description
A quick-capture scratchpad for trade ideas. Record setups you spot on your phone, save chart observations, and review everything later when you're at the desk. All data stays on-device.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"save"` — Save a new note. Requires: `content`. Optional: `symbol`, `tags`, `confidence`.
  - `"list"` — Show saved notes. Optional: `limit` (default 10), `symbol` (filter).
  - `"search"` — Search notes. Requires: `query`.
  - `"delete"` — Delete a note. Requires: `id`.
  - `"help"` — Show usage guide.

- **content**: String. The note text (required for "save").
- **symbol**: String. Optional ticker symbol to tag the note with.
- **tags**: String. Optional comma-separated tags (e.g., "FVG, sweep, bullish").
- **confidence**: Number. Optional confidence level 1-10.
- **query**: String. Search term (required for "search").
- **id**: String. Note ID (required for "delete").
- **limit**: Number. Max notes to return (default 10).

The script returns JSON with the saved note or list of notes.

## Response guidance
- When saving: confirm with a preview of the note
- When listing: show notes with timestamps, symbols, and tags
- When searching: highlight matching notes
- Notes persist locally on the device
