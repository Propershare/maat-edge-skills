---
name: maat-scribe
description: Voice-powered note-taking, book writing, and picture saving. Dictate notes, write book chapters by voice, and save photos — all saved to your local Mac, not the cloud. Also connects to MAAT memory.
---

# MAAT Scribe — Voice Notes, Book Writing, Picture Saving

## Description
Speak your thoughts and have them saved as notes on your Mac. Dictate book chapters organized by chapter/section. Save pictures from your camera. All data stays on your local machine — no cloud.

## Instructions

Call the `run_js` tool using `index.html` and pass a JSON string in `data` with the following fields:

### Save a Note
- **action**: `"note"`
- **content**: String. The note text (required).
- **title**: String. Optional title (auto-generated if omitted).
- **tags**: String. Optional comma-separated tags.

### Write a Book Chapter
- **action**: `"book"`
- **content**: String. The chapter/section text (required).
- **chapter**: String. Chapter name (e.g., "Chapter 1: Origins").
- **section**: String. Optional section name.

### Save a Picture
- **action**: `"picture"`
- **image**: String. Base64-encoded image data (required).
- **filename**: String. Optional filename (auto-generated if omitted).

### List Notes
- **action**: `"notes"` — List all saved notes.

### List Book
- **action**: `"book-list"` — Show book structure (chapters and sections).

### Help
- **action**: `"help"` — Show usage guide.

## Response guidance
- When saving a note: confirm the title and file path
- When writing a book: show the chapter/section and updated book index
- When saving a picture: confirm the filename and size
- All data is saved to `~/maat-ecosystem/maat-scribe/` on your Mac
