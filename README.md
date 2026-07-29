# MAAT Edge Skills

Agent Skills for **Google AI Edge Gallery** — query your MAAT lab from your iPhone.

## Skills

| Skill | Description | Type |
|-------|-------------|------|
| [maat-lab-bridge](maat-lab-bridge/) | Query lab status, trading system, episodic/semantic memories, search | JS |

## Setup

### 1. Start the bridge on your Mac

```bash
python3 /Users/ps/clawd/edge-bridge/bridge_server.py
```

The bridge runs on `http://192.168.4.36:9876` and exposes:
- `/status` — Bridge health
- `/episodic` — Recent episodic memories
- `/semantic` — Semantic knowledge
- `/trading` — Trading system status
- `/search?q=...` — Search across all lab memory
- `/artifacts` — Lab brain artifacts

### 2. Load the skill on iPhone

1. Open **AI Edge Gallery** on iPhone
2. Go to **Agent Skills** tile
3. Tap **+** → **Load skill from URL**
4. Enter: `https://ps.github.io/maat-edge-skills/maat-lab-bridge/`
5. The skill will query your Mac's bridge server over LAN

### 3. Auto-start the bridge (optional)

Add to your crontab or launchd to start on boot:

```bash
@reboot python3 /Users/ps/clawd/edge-bridge/bridge_server.py &
```

## Architecture

```
iPhone (AI Edge Gallery)          Mac (192.168.4.36)           Lab
┌─────────────────────┐    HTTP    ┌──────────────────┐    ┌──────────────┐
│ Gemma 4 + Skill     │ ────────→ │ bridge_server.py │───→│ maat-memory  │
│ maat-lab-bridge     │ ←──────── │ :9876            │    │ (git files)  │
└─────────────────────┘    JSON    └──────────────────┘    └──────────────┘
                                          │
                                          └──→ Lab Brain Postgres (192.168.4.21)
```

## Development

Each skill follows the standard AI Edge Gallery structure:

```
skill-name/
├── SKILL.md          # Metadata + LLM instructions
└── scripts/
    └── index.html    # JS entry point (ai_edge_gallery_get_result)
```
