from src.utils.profiling import timing_decorator, profile_memory
import numpy as np

@timing_decorator
def test_cpu_operation():
    """Test basic CPU operation with timing"""
    # Create large arrays
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)

@timing_decorator
@profile_memory
def test_memory_usage():
    """Test memory profiling"""
    # Allocate and operate on memory
    data = []
    for _ in range(100):
        data.append(np.random.rand(100, 100))
    return len(data)

def main():
    print("Testing CPU timing...")
    test_cpu_operation()
    
    print("\nTesting memory profiling...")
    test_memory_usage()

if __name__ == "__main__":
    main() 