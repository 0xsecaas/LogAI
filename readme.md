
# Local LLM System Log Analyzer - Lightweight SRS

## 1. Purpose
Local tool to monitor Linux system logs to make a succinct report of the system status.
Privacy-preserving; no data leaves the device.

## Current Scope (MVP)
- Parse and index system logs locally (`/var/log/*`, `journalctl`).
- CLI interface to ask natural language questions.
- Use small LLM via `llama.cpp` (e.g., LLaMA2-7B Q4 or smaller).
- Return plain-text answers; no dashboard yet.
- Privacy-preserving: No external API calls.

## Ideal Final Vision
- Cross-platform app (Linux, Windows, macOS).
- Extend with plugins
 - generate actionable advisories
 - support wider range of logs
- Full dashboard (Tauri + React) with:
  - Real-time system monitoring.
  - Summaries (daily/weekly reports).
  - Security recommendations (LLM + rule-based).
- Lightweight, <2 GB RAM usage, near-instant responses.
- Community-driven open-source project.

## Tech
- **Input:** `/var/log/*`, `journalctl`, dmesg.  
- **Output:** Summaries, status insights, security suggestions.  
- **Platform:** Linux (initial), Windows & macOS (later).  
- **Tech:** `llama.cpp` or Ollama for LLM inference, Tauri/React for UI.

