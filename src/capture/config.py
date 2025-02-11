from dataclasses import dataclass

@dataclass
class CaptureConfig:
    """Configuration for screen capture"""
    window_title: str = ""  # Target window title
    capture_rate: int = 60  # FPS target
    resize_factor: float = 1.0  # Resize factor for captured frames 