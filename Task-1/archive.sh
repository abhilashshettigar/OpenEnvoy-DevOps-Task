#!/bin/bash

# Simple log archiver
# Usage: ./archive.sh [search_dir] [backup_dir]

set -e

SEARCH_DIR="${1:-.}"
BACKUP_DIR="${2:-./backup}"
ARCHIVE_NAME="logs-$(date +%Y%m%d).tar.gz"

# Validate input
[ -d "$SEARCH_DIR" ] || { echo "Error: Directory '$SEARCH_DIR' not found"; exit 1; }

# Check if log files exist
LOG_COUNT=$(find "$SEARCH_DIR" -name "*.log" -type f | wc -l)
[ "$LOG_COUNT" -eq 0 ] && { echo "No log files found in '$SEARCH_DIR'"; exit 0; }

# Check if we can create backup directory
mkdir -p "$BACKUP_DIR" 2>/dev/null || { echo "Error: Cannot create backup directory '$BACKUP_DIR'"; exit 1; }

# Create archive
find "$SEARCH_DIR" -name "*.log" -type f | tar -czf "$ARCHIVE_NAME" -T -
mv "$ARCHIVE_NAME" "$BACKUP_DIR/"

echo "Archived to $BACKUP_DIR/$ARCHIVE_NAME"
exit 0