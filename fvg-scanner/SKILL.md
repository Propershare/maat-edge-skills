---
name: fvg-scanner
description: Analyze OHLC price data for Fair Value Gaps (FVGs), 50-yard line, liquidity sweeps, and retests using Easy E's ICT/SMC methodology. Use when the user provides price data or asks about FVG analysis.
---

# FVG Pattern Scanner

## Description
Detects bullish and bearish Fair Value Gaps from OHLC data, calculates the 50-yard line (FVG midpoint), checks for liquidity sweeps below/above the FVG, and confirms retests. All logic runs locally on-device.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"analyze"` — Analyze OHLC data for FVGs. Requires `candles` field.
  - `"help"` — Show usage examples.

- **candles**: Array of candle objects (required when `action` is `"analyze"`). Each candle:
  ```json
  {
    "high": 100.50,
    "low": 99.20,
    "open": 99.80,
    "close": 100.30,
    "time": "2026-07-29T14:00:00Z"
  }
  ```
  Provide at least 6-10 candles for meaningful analysis. 4H timeframe preferred.

The script returns JSON with:
- `fvgs`: Array of detected FVGs (bullish/bearish, price levels, midpoint/50-yard line)
- `sweeps`: Array of detected liquidity sweeps
- `retests`: Array of confirmed retests
- `summary`: Overall market context

## Response guidance
- Present FVGs clearly with price levels and direction
- Highlight the 50-yard line (midpoint) as the battlefield
- Note any sweeps and whether retests confirmed
- Give a clear bias: bullish, bearish, or neutral
- If data is insufficient, ask for more candles
