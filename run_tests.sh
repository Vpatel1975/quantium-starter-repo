#!/bin/bash
set -e

# Activate virtual environment
source "$(dirname "$0")/venv/Scripts/activate"

# Run test suite
python -m pytest test_app.py -v

# Exit 0 on success (set -e handles non-zero exits automatically)
exit 0
