---
name: position-calculator
description: Calculate position size, risk amount, and R:R targets based on account size, risk percentage, stop loss, and entry price. Includes Easy E's 1% risk rule.
---

# Position Size Calculator

## Description
Calculate optimal position sizes for trades. Input your account size, risk percentage, entry price, and stop loss to get position size, dollar risk, and R:R targets.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

- **action**: String. One of:
  - `"calculate"` — Calculate position size. Requires: `account`, `risk_pct`, `entry`, `stop`, `direction`.
  - `"targets"` — Calculate R:R targets. Requires: `entry`, `stop`, `direction`, `target_r` (optional, default 3).
  - `"help"` — Show usage guide.

- **account**: Number. Account size in dollars.
- **risk_pct**: Number. Risk percentage (e.g., 1 for 1%).
- **entry**: Number. Entry price.
- **stop**: Number. Stop loss price.
- **direction**: String. "long" or "short".
- **target_r**: Number. R multiple for targets (default 3).

The script returns JSON with calculated values.

## Response guidance
- Show the position size clearly
- Break down the dollar risk amount
- Show R:R targets at 1R, 2R, 3R
- If using Easy E's 1% rule, note it
