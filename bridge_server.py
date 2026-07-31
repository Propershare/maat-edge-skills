#!/usr/bin/env python3
"""
MAAT Lab Bridge — HTTP API for AI Edge Gallery skills to query lab data.
Runs on the Mac, accessible from iPhone on LAN at 192.168.4.36:9876
"""
import http.server
import json
import os
import subprocess
import sys
from datetime import datetime
from urllib.parse import urlparse, parse_qs

PORT = 9876
HERMES_ENV = os.path.expanduser("~/.hermes/.env")
MAAT_ECOSYSTEM = os.path.expanduser("~/maat-ecosystem")
MEMORY_DIR = os.path.join(MAAT_ECOSYSTEM, "maat-memory")
EPISODIC_DIR = os.path.join(MEMORY_DIR, "episodic")
SEMANTIC_DIR = os.path.join(MEMORY_DIR, "semantic")

# ── Helpers ────────────────────────────────────────────────────────────────

def json_response(data, status=200):
    body = json.dumps(data, indent=2).encode()
    return (status, {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}, body)

def error_response(msg, status=400):
    return json_response({"error": msg}, status)

def read_memory_dir(directory, limit=10):
    """Read recent files from a memory directory."""
    if not os.path.isdir(directory):
        return []
    files = []
    for f in sorted(os.listdir(directory), reverse=True):
        path = os.path.join(directory, f)
        if os.path.isfile(path) and f.endswith((".md", ".json", ".txt")):
            try:
                with open(path) as fh:
                    content = fh.read(2000)  # first 2000 chars
                files.append({"filename": f, "preview": content[:500]})
            except:
                pass
        if len(files) >= limit:
            break
    return files

def run_mcp_tool(tool_name, args_json):
    """Call the MCP server via its stdio interface."""
    mcp_script = os.path.join(MAAT_ECOSYSTEM, "maat-memory", "maat_memory_mcp.py")
    if not os.path.exists(mcp_script):
        return {"error": f"MCP script not found at {mcp_script}"}
    
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": args_json
        }
    }
    
    try:
        result = subprocess.run(
            [sys.executable, mcp_script],
            input=json.dumps(request).encode(),
            capture_output=True,
            timeout=15
        )
        output = json.loads(result.stdout)
        if "result" in output:
            content = output["result"].get("content", [])
            for item in content:
                if item.get("type") == "text":
                    return json.loads(item["text"])
        return output
    except Exception as e:
        return {"error": str(e)}

# ── Route handlers ────────────────────────────────────────────────────────

def handle_status():
    return json_response({
        "status": "ok",
        "service": "maat-lab-bridge",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "host": "192.168.4.36",
        "port": PORT
    })

def handle_episodic(limit=5):
    memories = read_memory_dir(EPISODIC_DIR, limit)
    return json_response({"memories": memories, "count": len(memories)})

def handle_semantic(domain=None):
    files = read_memory_dir(SEMANTIC_DIR, 20)
    if domain:
        files = [f for f in files if domain.lower() in f["filename"].lower()]
    return json_response({"memories": files, "count": len(files)})

def handle_artifacts():
    result = run_mcp_tool("maat_memory_read_artifacts", {"limit": 20})
    return json_response(result)

def handle_trading_status():
    """Check trading system status."""
    trading_dir = os.path.expanduser("~/.hermes/hermes-agent/trading-system")
    status = {
        "system": "maat-fvg-edge",
        "account_type": "paper",
        "last_scan": None,
        "open_positions": 0,
        "equity": None,
        "cron_jobs": []
    }
    
    # Check for recent episodic files with scan data
    scans = read_memory_dir(EPISODIC_DIR, 3)
    for s in scans:
        if "scan" in s["filename"].lower() or "fvg" in s["filename"].lower():
            status["last_scan"] = s["filename"]
            status["last_scan_preview"] = s["preview"]
            break
    
    return json_response(status)

def handle_search(query):
    """Search across all lab memory."""
    results = []
    for directory, label in [(EPISODIC_DIR, "episodic"), (SEMANTIC_DIR, "semantic")]:
        if not os.path.isdir(directory):
            continue
        for f in sorted(os.listdir(directory), reverse=True):
            path = os.path.join(directory, f)
            if not os.path.isfile(path):
                continue
            try:
                with open(path) as fh:
                    content = fh.read()
                if query.lower() in content.lower():
                    results.append({
                        "source": label,
                        "filename": f,
                        "snippet": content[:300]
                    })
            except:
                pass
            if len(results) >= 10:
                break
    return json_response({"results": results, "count": len(results), "query": query})

# ── Static file server for skills ────────────────────────────────────────

SKILLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

MIME_TYPES = {
    ".html": "text/html",
    ".js": "application/javascript",
    ".md": "text/markdown",
    ".json": "application/json",
    ".css": "text/css",
    ".png": "image/png",
    ".svg": "image/svg+xml",
}

def serve_skill_file(path):
    """Serve static skill files for AI Edge Gallery to load."""
    # path is like /skill/maat-lab-bridge/ or /skill/maat-lab-bridge/SKILL.md
    prefix = "/skill/"
    if path.startswith(prefix):
        rel_path = path[len(prefix):]
    else:
        rel_path = path
    if not rel_path or rel_path.endswith("/"):
        rel_path += "SKILL.md"
    
    full_path = os.path.normpath(os.path.join(SKILLS_DIR, rel_path))
    
    # Security: ensure we stay within the skills directory
    if not full_path.startswith(SKILLS_DIR):
        return error_response("Invalid path", 403)
    
    if not os.path.isfile(full_path):
        return error_response(f"File not found: {rel_path}", 404)
    
    ext = os.path.splitext(full_path)[1].lower()
    content_type = MIME_TYPES.get(ext, "application/octet-stream")
    
    try:
        with open(full_path, "rb") as f:
            body = f.read()
        return (200, {
            "Content-Type": content_type,
            "Access-Control-Allow-Origin": "*",
            "Content-Length": str(len(body)),
        }, body)
    except Exception as e:
        return error_response(f"Error reading file: {e}", 500)

# ── Membership API ───────────────────────────────────────────────────────

# Invite codes (you generate these in the lab)
INVITE_CODES = {
    "MAAT001": {"member": "ps", "status": "active"},
    "MAAT002": {"member": "alpha", "status": "active"},
    "MAAT003": {"member": "beta", "status": "pending"},
}

def handle_verify(data):
    """Verify an invite code."""
    code = data.get("code", "").upper().strip()
    if code in INVITE_CODES:
        entry = INVITE_CODES[code]
        if entry["status"] == "active":
            return json_response({"valid": True, "member": entry["member"]})
        else:
            return json_response({"valid": False, "reason": "code_pending"})
    return json_response({"valid": False, "reason": "invalid_code"})

def handle_register(data):
    """Register a device to a member."""
    code = data.get("code", "").upper().strip()
    device_id = data.get("device_id", "")
    if code in INVITE_CODES and INVITE_CODES[code]["status"] == "active":
        # In production, store in Postgres
        return json_response({"registered": True, "member": INVITE_CODES[code]["member"]})
    return json_response({"registered": False, "reason": "invalid_code"})

def handle_generate(data):
    """Generate a new invite code (admin only)."""
    # In production, require admin auth
    member = data.get("member", "unknown")
    import uuid
    code = f"MAAT{uuid.uuid4().hex[:4].upper()}"
    INVITE_CODES[code] = {"member": member, "status": "active"}
    return json_response({"code": code, "member": member})

# ── Router ────────────────────────────────────────────────────────────────

ROUTES = {
    "/": handle_status,
    "/status": handle_status,
    "/episodic": lambda: handle_episodic(5),
    "/semantic": lambda: handle_semantic(),
    "/artifacts": handle_artifacts,
    "/trading": handle_trading_status,
}

class BridgeHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        params = parse_qs(parsed.query)
        
        if path in ROUTES:
            status, headers, body = ROUTES[path]()
        elif path == "/search" and "q" in params:
            status, headers, body = handle_search(params["q"][0])
        elif path.startswith("/semantic/") and len(path) > 10:
            domain = path.split("/")[-1]
            status, headers, body = handle_semantic(domain)
        elif path.startswith("/skill/"):
            status, headers, body = serve_skill_file(path)
        else:
            status, headers, body = error_response(f"Not found: {path}", 404)
        
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)
    
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length else b"{}"
        
        try:
            data = json.loads(body)
        except:
            data = {}
        
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        
        if path == "/search":
            query = data.get("q", data.get("query", ""))
            if not query:
                status, headers, body = error_response("Missing 'q' or 'query' field")
            else:
                status, headers, body = handle_search(query)
        elif path == "/verify":
            status, headers, body = handle_verify(data)
        elif path == "/register":
            status, headers, body = handle_register(data)
        elif path == "/generate":
            status, headers, body = handle_generate(data)
        else:
            status, headers, body = error_response(f"Not found: {path}", 404)
        
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)
    
    def log_message(self, format, *args):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {args[0]} {args[1]} {args[2]}")

# ── Main ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"🚀 MAAT Lab Bridge starting on http://0.0.0.0:{PORT}")
    print(f"   iPhone can reach it at http://192.168.4.36:{PORT}")
    print(f"   Endpoints: /status /episodic /semantic /artifacts /trading /search?q=...")
    server = http.server.HTTPServer(("0.0.0.0", PORT), BridgeHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()
