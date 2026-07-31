---
name: maat-trader
description: All-in-one trading toolkit — FVG scanner, trade journal, position calculator, session timer, trade scratchpad, and chart vision for Meta glasses. Use for any trading analysis or record-keeping.
---

# MAAT Trader — All-in-One Toolkit

## Description
Six trading tools in one skill. All logic runs locally on-device. No internet needed. Works with Meta glasses camera for chart analysis.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

### Tool 1: FVG Scanner
- **action**: `"fvg"`
- **candles**: Array of `{high, low, open, close, time}` objects (at least 4)

### Tool 2: Trade Journal
- **action**: `"journal"`
- **subaction**: `"log"`, `"list"`, `"stats"`, or `"clear"`
- **symbol**, **direction**, **entry**, **exit**, **quantity**, **setup**, **notes**: For logging trades

### Tool 3: Position Calculator
- **action**: `"position"`
- **account**, **risk_pct**, **entry**, **stop**, **direction**: Required

### Tool 4: Session Timer
- **action**: `"sessions"`
- **subaction**: `"now"` or `"schedule"`

### Tool 5: Trade Scratchpad
- **action**: `"scratchpad"`
- **subaction**: `"save"`, `"list"`, `"search"`, or `"delete"`
- **content**, **symbol**, **tags**, **confidence**: For saving notes

### Tool 6: Chart Vision (Meta Glasses)
When the user shares a chart image (from Meta glasses camera or photo gallery), analyze it visually for ICT/SMC patterns. No JS needed — use your vision capabilities.

**Steps:**
1. Identify the timeframe from the chart
2. Detect bullish/bearish FVGs and mark the 50-yard line
3. Check for liquidity sweeps below/above FVGs
4. Confirm retests at the 50-yard line
5. Determine bias (bullish/bearish/neutral)
6. Identify targets (opposing FVG, swing highs/lows)
7. Note market structure (MSS, CHoCH, order blocks)

**Voice responses (Meta glasses):**
- Keep responses concise — user hears through glasses speakers
- Read key levels clearly: "Bullish FVG from 7440 to 7450, 50-yard line at 7445"
- Describe the chart verbally when asked "what do you see?"

## Response guidance
Present results clearly. For FVG scans, show the 50-yard line. For journal stats, highlight win rate. For position calc, show R:R targets. For chart vision, describe what you see conversationally.
