## Buzz Bar - Project Plan

## Purpose
Create a minimal, always-on-top floating visualizer window for real-time audio amplitude or spectrum display, designed for use with Ableton or system audio as visual studio feedback.

## Active Project Name
**Buzz Bar**

## Description
*Buzz Bar* is a lightweight desktop utility designed to display real-time audio amplitude or frequency spectrum as thin bars over any application, intended for studio use with PowerToys or external window control software.

## Core Libraries
- sounddevice (audio input)
- pygame (visualization)
- numpy (FFT and data smoothing)

## Target Platform
- Primary: Windows 10/11
- Secondary (future testing): macOS

## Project Folder Structure
buzz_bar/
├── src/
│ ├── init.py
│ ├── audio_input.py
│ ├── visualizer.py
│ └── main.py
├── tests/
├── requirements.txt
├── README.md
├── buzz_bar_project_plan.md
├── buzz_bar_goals_ideas.md
├── .gitignore
└── .vscode/

## Development Phases

### Phase 1 - Core Audio + Amplitude Visual
**Status: Complete**
- Captured system audio amplitude using sounddevice
- Created small always-on-top floating window with pygame
- Displayed a single horizontal orange bar on black background to represent amplitude

### Phase 1.5 - Minimal Multi-Bar Mode
**Status: Complete**
- Replaced single bar with 16 thin vertical bars across window
- All bars reacted equally to overall amplitude
- Matched intended minimalist aesthetic

### Phase 2 - Spectrum Mode
**Status: Complete**
- Replaced amplitude display with real-time spectrum visualization
- Implemented FFT using numpy
- Split spectrum into 16 frequency bands (bars) for independent movement
- Achieved live visual feedback with minimal latency

## Current Status
- Prototype complete
- Fully functioning real-time spectrum visualizer
- Low-latency, low-resource window usable over DAWs like Ableton

## Next Phase Ideas (Future Work)
See `buzz_bar_goals_ideas.md` for more details.
- Peak hold mode
- User-selectable color schemes
- User-configurable bar count (ex: 8, 16, 32)
- Toggle between amplitude and spectrum modes
- Frameless window mode for true overlay appearance
- Save window position between launches
- Refactor into class-based architecture for easier feature expansion

## Workflow Notes
1. Develop in `feature/*` branches
2. Use regular snapshots and descriptive commits
3. After each dev session:
   - Update project plan
   - Push branch to remote
   - Save ChatGPT collaboration notes if helpful
   - Reload into GPT project folder for next session

## ✅ Milestone: BuzzBarBridge v1 Stable Prototype (May 15, 2025)

### Overview
This marks the successful creation and test of the first full data bridge between Ableton Live and Python for the Buzz Bar project. Real-time audio amplitude data is now sent directly from Ableton into a Python listener, forming the foundation for future visualizer development.

### Completed
- Built `BuzzBarBridge.amxd` Max for Live device:
  - `[plugin~] → [snapshot~ 50] → [pack f] → [prepend /buzzbar/amplitude] → [udpsend 127.0.0.1 7400]`
  - Patched `[plugin~ L]` output into `[snapshot~]` to enable correct audio signal capture
- Built `test_bridge_capture.py` Python OSC listener to receive `/buzzbar/amplitude` data
- Verified full pipeline:
  - Audio input in Ableton → BuzzBarBridge → OSC → Python
  - Continuous, stable float stream representing waveform amplitude
- Confirmed this prototype works in current Ableton + Max for Live environment

### Notes
- Raw amplitude values are in range `-1.0 to +1.0`, matching audio waveform samples
- Absolute value filtering to remove negatives pending next phase
- Data bridge officially stable and expandable

### Next Steps
- Begin Phase 2 development:
  - Silence threshold filter
  - Optional smoothing or peak hold
  - Integration with visualizer bars in `buzz_bar`
