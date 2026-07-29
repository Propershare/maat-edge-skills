---
name: session-timer
description: Track forex/crypto trading sessions — London, New York, Asia, and Sydney. Shows which sessions are active, time remaining, and upcoming economic events.
---

# Session Timer

## Description
Track the four major trading sessions (Sydney, Asia/Tokyo, London, New York). Shows which sessions are currently active, time remaining, and upcoming session opens. All runs locally on-device.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"now"` — Show current session status
  - `"schedule"` — Show full session schedule for today
  - `"help"` — Show usage guide

The script returns JSON with session information.

## Response guidance
- Highlight active sessions with remaining time
- Show upcoming sessions with open time
- Note session overlaps (e.g., London + NY overlap)
- Use local time for readability
