#!/usr/bin/env python
import sys
import traceback

print("Testing imports...")

try:
    print("1. Testing logging...")
    import logging
    print("   ✓ logging OK")
except Exception as e:
    print(f"   ✗ logging FAILED: {e}")
    traceback.print_exc()

try:
    print("2. Testing os...")
    import os
    print("   ✓ os OK")
except Exception as e:
    print(f"   ✗ os FAILED: {e}")

try:
    print("3. Testing subprocess...")
    import subprocess
    print("   ✓ subprocess OK")
except Exception as e:
    print(f"   ✗ subprocess FAILED: {e}")

try:
    print("4. Testing pynput...")
    from pynput import keyboard
    print("   ✓ pynput OK")
except Exception as e:
    print(f"   ✗ pynput FAILED: {e}")
    traceback.print_exc()

try:
    print("5. Testing psutil...")
    import psutil
    print("   ✓ psutil OK")
except Exception as e:
    print(f"   ✗ psutil FAILED: {e}")
    traceback.print_exc()

try:
    print("6. Testing PyQt5...")
    from PyQt5.QtWidgets import QApplication
    print("   ✓ PyQt5 OK")
except Exception as e:
    print(f"   ✗ PyQt5 FAILED: {e}")
    traceback.print_exc()

try:
    print("7. Testing requests...")
    import requests
    print("   ✓ requests OK")
except Exception as e:
    print(f"   ✗ requests FAILED: {e}")
    traceback.print_exc()

print("\nAll import tests completed!")
