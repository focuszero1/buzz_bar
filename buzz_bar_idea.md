# Buzz Bar - Ideas and Future Goals

## Core Concept
Buzz Bar is intentionally minimal and lightweight. Any added features should enhance studio usability without cluttering the interface.

## Possible Enhancements

### Frequency Range Focus
- Implement optional **low-pass / high-pass filtering** to reduce response to extreme frequencies
- Focus bars only on usable studio audio range (ex: 60 Hz to 16 kHz)
- Could be set as hard-coded or user-adjustable range limits
- Improve visual relevance by removing sub-bass rumble and high-end noise

### Color Customization
- Allow user to toggle between preset color themes
- Example themes:
  - Default: black background, orange bars
  - Dark mode: dark gray background, cyan bars
  - Studio mode: deep blue background, soft white bars
- Possibly allow RGB values to be entered manually in a settings file

### Visual Modes (Stretch Ideas)
- Peak hold mode (small marker shows recent peak value per bar)
- Option to choose number of bars (ex: 8, 16, 32)
- Toggle between amplitude and spectrum modes
- Frameless window mode for floating visualizer with no title bar
- Save window position and size between launches

## Notes
- Spectrum mode (Phase 2) works and looks good
- Next development should focus on small quality-of-life improvements
- Continue to prioritize minimal CPU + GPU use
