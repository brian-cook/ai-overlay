# WoW AI Combat Analysis Overlay

A real-time computer vision analysis system for World of Warcraft, providing combat information extraction and unit tracking through an optimized overlay interface.

## Project Structure

.
├── src/
│ ├── capture/ # Screen capture components
│ ├── vision/ # Computer vision pipeline
│ ├── ai/ # AI model and training
│ ├── overlay/ # UI and overlay system
│ ├── utils/ # Shared utilities
│ └── tests/ # Test suites
├── data/
│ ├── training/ # Training datasets
│ ├── models/ # Trained models
│ └── configs/ # Configuration files
├── docs/ # Documentation
└── scripts/ # Build and automation scripts
```

## Setup

1. Install Python 3.10+
2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Verify setup:
   ```bash
   python scripts/verify_gpu.py
   ```

## Development

- Follow [best practices](docs/resources/wow_ai_overlay_best_practices.txt)
- See [master plan](docs/resources/wow_ai_overlay_master_plan.txt) for project overview
- Check [setup checklist](docs/resources/phase1_setup_checklist.txt) for environment setup

## Performance Targets

- Frame processing: <16ms
- CPU usage: <5%
- Memory footprint: <2GB
- Detection accuracy: >95%