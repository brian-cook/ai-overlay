# AI Combat Analysis Overlay

A real-time computer vision analysis system providing combat information extraction and unit tracking through an optimized overlay interface.

## Features (Planned)

- Real-time screen capture and analysis
- Unit identification and tracking
- Health/resource monitoring
- Combat state analysis
- Performance metrics display
- Low-impact overlay interface

## Performance Targets

- Frame processing: <16ms
- CPU usage: <5%
- Memory footprint: <2GB
- Detection accuracy: >95%

## Requirements

- Windows 10/11
- Python 3.11+
- NVIDIA GPU with CUDA support
- Target application client

## Project Structure

.
├── src/
│   ├── capture/     # Screen capture components
│   ├── vision/      # Computer vision pipeline
│   ├── ai/          # AI model and training
│   ├── overlay/     # UI and overlay system
│   ├── utils/       # Shared utilities
│   └── tests/       # Test suites
├── data/
│   ├── training/    # Training datasets
│   ├── models/      # Trained models
│   └── configs/     # Configuration files
├── docs/            # Documentation
└── scripts/         # Build and automation scripts

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/brian-cook/ai-overlay.git
   cd ai-overlay
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r docs/resources/requirements.txt
   ```

4. Verify setup:
   ```bash
   python scripts/verify_gpu.py
   ```

## Development

- Follow [best practices](docs/resources/best_practices.txt)
- See [master plan](docs/resources/master_plan.txt) for project overview
- Check [setup checklist](docs/resources/phase1_setup_checklist.txt) for environment setup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)

## Disclaimer
