#!/bin/bash
# Generate all book formats from the translation files
# Requires: pandoc, weasyprint, python3

set -e
cd "$(dirname "$0")"

echo "=== Building English manuscript ==="
python3 build-manuscript.py

echo "=== Building bilingual manuscript ==="
python3 build-bilingual.py

echo "=== Generating EPUB ==="
pandoc manuscript.md \
  -o "The Recitation - A Root-Recovery Translation.epub" \
  --toc --toc-depth=1 \
  --metadata title="The Recitation" \
  --metadata subtitle="A Root-Recovery Translation of the Qur'an" \
  --metadata author="Joop Kiefte"

echo "=== Generating English PDF ==="
pandoc manuscript.md \
  -o /tmp/recitation-en.html \
  --toc --toc-depth=1 \
  --standalone
weasyprint /tmp/recitation-en.html \
  "The Recitation - A Root-Recovery Translation.pdf" 2>/dev/null

echo "=== Generating Bilingual PDF ==="
weasyprint manuscript-bilingual.html \
  "The Recitation - Bilingual Edition.pdf" 2>/dev/null

echo "=== Done ==="
ls -lh "The Recitation"*.epub "The Recitation"*.pdf
