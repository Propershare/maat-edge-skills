---
name: trade-journal
description: Log, track, and review your trades. Record entries, exits, setup type, R:R, screenshots, and track win rate over time. All data stored locally on-device.
---

# Trade Journal

## Description
A private trade journal that stores all data locally on your device. Log trades with entry/exit prices, direction, setup type, R:R ratio, notes, and screenshots. Track win rate, P&L, and performance over time.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"log"` — Record a new trade. Requires: `symbol`, `direction`, `entry`, `exit`, `quantity`, `setup`, `notes`.
  - `"list"` — Show recent trades. Optional: `limit` (default 10).
  - `"stats"` — Show performance stats (win rate, P&L, best/worst trades).
  - `"clear"` — Clear all journal data (requires confirmation).
  - `"help"` — Show usage guide.

- **symbol**: String. Ticker symbol (e.g., "ES=F", "SPY").
- **direction**: String. "long" or "short".
- **entry**: Number. Entry price.
- **exit**: Number. Exit price.
- **quantity**: Number. Number of shares/contracts.
- **setup**: String. Setup type (e.g., "FVG sweep", "MSS", "liquidity grab", "50-yard line").
- **notes**: String. Optional trade notes.
- **limit**: Number. Max trades to return (for "list" action).

The script returns JSON with the trade record or summary.

## Response guidance
- When logging: confirm the trade was saved with key details
- When listing: show trades in a readable format with dates
- When showing stats: highlight win rate, total P&L, average R:R
- All data persists locally on the device
