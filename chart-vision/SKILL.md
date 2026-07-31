---
name: chart-vision
description: Analyze chart images from your Meta glasses camera for Fair Value Gaps, liquidity sweeps, 50-yard line, order blocks, and market structure shifts using Easy E's ICT/SMC methodology.
---

# Chart Vision — FVG Analysis from Images

## Description
When you share a chart image (from your Meta glasses camera or photo gallery), this skill guides Gemma 4 to analyze it for ICT/SMC trading patterns. All analysis is done by the model's vision capabilities — no external API calls.

## Instructions

When the user shares a chart image or asks you to look at a chart, follow these steps:

### Step 1: Identify the Timeframe
Look at the chart image and identify the timeframe if visible (4H, 1H, 15m, etc.). If unclear, ask the user.

### Step 2: Detect Fair Value Gaps (FVGs)
Scan the chart for:
- **Bullish FVGs**: Three consecutive candles where the middle candle's high is lower than the previous candle's low (gap up). Mark the FVG zone (previous low → middle high).
- **Bearish FVGs**: Three consecutive candles where the middle candle's low is higher than the previous candle's high (gap down). Mark the FVG zone (previous high → middle low).

### Step 3: Calculate the 50-Yard Line
For each FVG detected:
- **50-yard line** = midpoint of the FVG zone
- This is the battlefield — watch for price reaction here

### Step 4: Check for Liquidity Sweeps
Look for:
- Price moving **below** a bullish FVG's low (sweeping buy-side liquidity)
- Price moving **above** a bearish FVG's high (sweeping sell-side liquidity)
- Note the wick/candle that did the sweep

### Step 5: Confirm Retests
After a sweep, check if price returned to the **50-yard line** and showed:
- A rejection candle (long wick, small body)
- A close back inside the FVG zone
- Multiple touches of the 50-yard line

### Step 6: Determine Bias
- **Bullish bias**: Bullish FVG with sweep below + retest holding + higher highs
- **Bearish bias**: Bearish FVG with sweep above + retest holding + lower lows
- **Neutral**: No clear structure or conflicting signals

### Step 7: Identify Targets
- **First target**: The opposing FVG (if bullish, target the nearest bearish FVG above)
- **Second target**: Previous swing high/low
- **Third target**: Equal highs/lows

### Step 8: Note Market Structure
- **MSS (Market Structure Shift)**: A break of structure — price breaks the previous swing high/low
- **CHoCH (Change of Character)**: A sudden shift in momentum
- **Order Blocks**: Large single candles where price reversed sharply

## Response Format

Present your analysis clearly:

```
📊 **Chart Analysis** — [Timeframe]

🔲 **FVGs Found: [N]**
• [Direction] FVG: [Price Range] → 50-Yard: [Midpoint]
• [Direction] FVG: [Price Range] → 50-Yard: [Midpoint]

🧹 **Sweeps: [N]**
• [Type] sweep to [Price]

🔄 **Retests: [N]**
• [Confirmed/Unconfirmed] at [Price]

📈 **Bias: [Bullish/Bearish/Neutral]**
• [Key reason for bias]

🎯 **Targets**
• 1st: [Price]
• 2nd: [Price]
• 3rd: [Price]

💡 **Notes**
• [Any additional observations about structure, order blocks, etc.]
```

## Voice Interaction (Meta Glasses)

When the user speaks through their Meta glasses:
- Respond conversationally — they're hearing you through the glasses speakers
- Keep responses concise (they're listening, not reading)
- Read out key levels clearly: "Bullish FVG from 7440 to 7450, 50-yard line at 7445"
- If they ask "what do you see?", describe the chart verbally
- If they ask "should I take this trade?", give your analysis but remind them it's not financial advice
