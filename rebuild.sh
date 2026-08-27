#!/usr/bin/env bash
set -euo pipefail
SOURCE="${1:-../dxspider}"
python3 tools/generate_reference.py --source "$SOURCE"
python3 tools/check_docs.py
mkdocs build --strict
echo
echo "Documentation built successfully in site/"
