---
name: maat-lab-bridge
description: Query the MAAT lab — check trading system status, browse episodic/semantic memories, search across lab knowledge, and view artifacts. Use when the user asks about lab status, trading system, or lab knowledge.
metadata:
  homepage: https://github.com/ps/maat-edge-skills
---

# MAAT Lab Bridge

## Description
Connects to the MAAT lab server on the local network to query trading system status, browse episodic and semantic memories, search across lab knowledge, and view artifacts.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"status"` — Get lab bridge status (host, version, uptime)
  - `"episodic"` — Get recent episodic memories (what happened recently)
  - `"semantic"` — Get semantic knowledge (system knowledge). Optional: pass `domain` to filter.
  - `"trading"` — Get trading system status (last scan, open positions, equity)
  - `"search"` — Search across all lab memory. Requires `query` field.
  - `"artifacts"` — Get artifacts from the lab brain

- **query**: String. Required when `action` is `"search"`. The search term.
- **domain**: String. Optional filter for `"semantic"` action (e.g., `"fvg-edge"`, `"methodology"`).

The script returns JSON with the results from the lab server.

## Response guidance
- Present the results clearly, formatted for mobile reading.
- For trading status: highlight the last scan date, any open positions, and account equity.
- For search results: show the filename, source (episodic/semantic), and a snippet.
- If the lab server is unreachable, tell the user and suggest checking that the bridge is running on the Mac.
