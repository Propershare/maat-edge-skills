---
name: maat-bridge
description: All-in-one MAAT lab bridge — save voice notes, write your book, save pictures, query trading system, search memories, FVG scan, trade journal, position calculator, session timer, scratchpad, and chart vision. One skill to rule them all.
---

# MAAT Bridge — All-in-One Lab & Trading Toolkit

## Description
Everything in one skill. Voice notes, book writing, picture saving, trading tools, lab queries, and constitutional safety. All data goes to your local Mac. No cloud.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

### 📝 Notes & Book
- **action**: `"note"` — Save a voice note. Fields: `content` (required), `title`, `tags`.
- **action**: `"book"` — Write a book chapter. Fields: `content` (required), `chapter`, `section`.
- **action**: `"picture"` — Save a photo. Fields: `image` (base64, required), `filename`.
- **action**: `"notes"` — List saved notes.
- **action**: `"book-list"` — Show book structure.

### 📊 Trading
- **action**: `"fvg"` — FVG scan. Fields: `candles` (array of {high, low, open, close, time}).
- **action**: `"journal"` — Trade journal. Fields: `subaction` ("log"/"list"/"stats"), `symbol`, `direction`, `entry`, `exit`, `quantity`, `setup`.
- **action**: `"position"` — Position calculator. Fields: `account`, `risk_pct`, `entry`, `stop`, `direction`.
- **action**: `"sessions"` — Session timer. Fields: `subaction` ("now"/"schedule").
- **action**: `"scratchpad"` — Trade ideas. Fields: `subaction` ("save"/"list"/"search"), `content`, `symbol`, `tags`.

### 🔬 Lab
- **action**: `"status"` — Lab bridge status.
- **action**: `"episodic"` — Recent episodic memories.
- **action**: `"semantic"` — Semantic knowledge. Optional: `domain`.
- **action**: `"search"` — Search lab memory. Fields: `query` (required).
- **action**: `"trading"` — Trading system status.

### 🛡️ Guardian
- **action**: `"rights"` — Know your rights.
- **action**: `"record"` — Start encrypted recording.

### ❓ Help
- **action**: `"help"` — Show this guide.

## Response guidance
Present results clearly. For notes, confirm the save. For trading, show levels and bias. For lab queries, show the data. Keep responses concise for voice output through glasses.
