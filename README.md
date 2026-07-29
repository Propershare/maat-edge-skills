# MAAT Edge Skills

Agent Skills for **Google AI Edge Gallery** — run on your iPhone with Gemma 4, fully offline.

## Skills

| Skill | Description | Offline |
|-------|-------------|---------|
| [maat-lab-bridge](maat-lab-bridge/) | Query your MAAT lab: trading status, memories, search | ✅ (LAN) |
| [fvg-scanner](fvg-scanner/) | Analyze OHLC data for FVGs, 50-yard line, sweeps, retests | ✅ |
| [trade-journal](trade-journal/) | Log trades, track win rate, P&L, performance stats | ✅ |
| [position-calculator](position-calculator/) | Position size, risk amount, R:R targets (Easy E 1% rule) | ✅ |
| [session-timer](session-timer/) | Track London, NY, Asia, Sydney sessions + overlaps | ✅ |
| [trade-scratchpad](trade-scratchpad/) | Save trade ideas, chart observations, market notes | ✅ |

## Quick Start

### 1. Start the bridge on your Mac

```bash
python3 /Users/ps/clawd/edge-bridge/bridge_server.py
```

### 2. Load skills on iPhone

Open **AI Edge Gallery** → Agent Skills → **+** → **Load skill from URL**

| Skill | URL |
|-------|-----|
| Lab Bridge | `https://2bbf4613325340.lhr.life/skill/maat-lab-bridge/` |
| FVG Scanner | `https://2bbf4613325340.lhr.life/skill/fvg-scanner/` |
| Trade Journal | `https://2bbf4613325340.lhr.life/skill/trade-journal/` |
| Position Calc | `https://2bbf4613325340.lhr.life/skill/position-calculator/` |
| Session Timer | `https://2bbf4613325340.lhr.life/skill/session-timer/` |
| Scratchpad | `https://2bbf4613325340.lhr.life/skill/trade-scratchpad/` |

### 3. Try them

- *"What's the trading system status?"* (lab-bridge)
- *"Analyze these candles for FVGs: [high: 100.5, low: 99.2, ...]"* (fvg-scanner)
- *"Log a trade: ES=F long, entry 7448, exit 7500, qty 2, FVG sweep"* (trade-journal)
- *"Calculate position: $80k account, 1% risk, long at 7448, stop at 7420"* (position-calculator)
- *"What sessions are active now?"* (session-timer)
- *"Save idea: ES=F bearish FVG sweep at 7450, confidence 7"* (scratchpad)

## Architecture

```
iPhone (AI Edge Gallery)          Mac (192.168.4.36)           Lab
┌─────────────────────┐    HTTP    ┌──────────────────┐    ┌──────────────┐
│ Gemma 4 + Skills    │ ────────→ │ bridge_server.py │───→│ maat-memory  │
│ (6 trading skills)  │ ←──────── │ :9876 / tunnel    │    │ (git files)  │
└─────────────────────┘    JSON    └──────────────────┘    └──────────────┘
```

## Structure

```
edge-bridge/
├── bridge_server.py          # HTTP API + static file server
├── .nojekyll                 # For GitHub Pages
├── README.md
├── maat-lab-bridge/          # Lab query skill
│   ├── SKILL.md
│   └── scripts/index.html
├── fvg-scanner/              # FVG pattern detection
│   ├── SKILL.md
│   └── scripts/index.html
├── trade-journal/            # Trade logging + stats
│   ├── SKILL.md
│   └── scripts/index.html
├── position-calculator/      # Position sizing + R:R
│   ├── SKILL.md
│   └── scripts/index.html
├── session-timer/            # Trading session tracker
│   ├── SKILL.md
│   └── scripts/index.html
└── trade-scratchpad/         # Trade idea scratchpad
    ├── SKILL.md
    └── scripts/index.html
```
