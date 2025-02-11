import torch
import cv2
import numpy as np

def verify_system():
    print("=== System Verification ===")
    
    # Check CUDA availability
    print("\nCUDA Support:")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU device: {torch.cuda.get_device_name(0)}")
    
    # Check OpenCV
    print("\nOpenCV Support:")
    print(f"OpenCV version: {cv2.__version__}")
    
    # Check NumPy
    print("\nNumPy Support:")
    print(f"NumPy version: {np.__version__}")

if __name__ == "__main__":
    verify_system() 