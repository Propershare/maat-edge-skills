---
name: maat-road
description: OTR trucking copilot — HOS clock, loads, fuel, parking, expenses, notes, day summary. Works fully offline.
---

# MAAT Road — OTR Copilot

Everything a driver needs on the road, voice-first and **offline**. No cloud, no bridge, no signal required. Data lives on the phone in `localStorage`.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with:

### ⏱️ Hours of Service (`action: "hos"`)
Property-carrying rules. Every call returns the live clock.
- `subaction: "start"` — go on duty (starts the 14-hour window).
- `subaction: "drive"` — start driving.
- `subaction: "stop"` — on-duty not driving (fuel, scale, dock, 30-min break). Optional: `note`.
- `subaction: "sleeper"` — sleeper berth.
- `subaction: "off"` — off duty (10+ hours resets the clock).
- `subaction: "status"` — what's my clock? Drive left, window left, break due, cycle left.
- `subaction: "log"` — recent duty entries (optional `limit`, default 12).
- `subaction: "undo"` — remove the last entry. Requires `confirm: true`.

### 🚛 Loads (`action: "load"`)
- `subaction: "add"` — `load_no` (required), `broker`, `pickup`, `delivery`, `miles`, `deadhead`, `rate`, `notes`.
- `subaction: "list"` — active loads.
- `subaction: "close"` — `load_no` (required), optional `miles` actually run, `rate`.
- `subaction: "stats"` — all-time loads, miles, revenue, revenue per mile.

### ⛽ Fuel (`action: "fuel"`)
- `subaction: "add"` — `gallons`, `price` (per gallon), optional `location`, `odometer`, `total`, `state`.
- `subaction: "stats"` — gallons, spend, average price per gallon, last 30 days.

### 🅿️ Parking (`action: "parking"`)
- `subaction: "add"` — `location` (required), optional `spaces_free`, `safe` (yes/no), `showers`, `note`.
- `subaction: "list"` — recent stops.
- `subaction: "search"` — `query`.

### 💵 Expenses (`action: "expense"`)
- `subaction: "add"` — `amount` (required), `category` (lumper/scale/toll/repair/food/other), `note`.
- `subaction: "list"` — recent (optional `limit`).
- `subaction: "stats"` — totals by category, today and all-time.

### 📝 Notes (`action: "note"`)
- `subaction: "add"` — `content` (required), optional `title`, `tags`.
- `subaction: "list"`, `subaction: "search"` with `query`.

### 📅 Day summary (`action: "day"`)
One spoken rollup: today's drive/on-duty hours, miles and money, active loads, last parking, open issues.

### 📊 Trading (`action: "trading"`)
Best-effort pull of the lab shortlist + journal. Degrades to "offline" when there is no signal — never blocks.

### ❓ `action: "help"`

## Response guidance
Speak the numbers. HOS answers must lead with what matters: drive time left, window left, break due. No tables, no walls of text — the driver is holding a wheel. Convert raw timestamps to clock times.
