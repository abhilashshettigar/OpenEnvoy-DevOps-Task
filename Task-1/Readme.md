# Task-1: Log Archiving Script

## Overview
This task implements an automated log archiving solution that finds all `.log` files in a directory and its subdirectories, compresses them into a date-stamped archive, and stores them in a backup directory.

## Project Structure
```
Task-1/s
├── archive.sh          # Main archiving script
├── README.md           # This documentation file
├── backup/             # Directory containing archived logs
│   └── logs-20250903.tar.gz  # Example archived file
└── sample/             # Sample directory with test log files
    ├── access.log      # Sample access log file (410 lines)
    └── errors/         # Sample error logs directory
        └── error.log   # Sample error log file (74 lines)
```

## Script Overview

### `archive.sh`
A simplified bash script that automatically archives log files with the following features:

## Usage
### Basic Usage
```bash
# Archive logs from current directory to ./backup
./archive.sh

# Archive logs from specific directory
./archive.sh /path/to/logs

# Archive logs from specific directory to custom backup location
./archive.sh /path/to/logs /path/to/backup
```

### Parameters
1. **SEARCH_DIR** (optional): Directory to search for `.log` files (defaults to current directory)
2. **BACKUP_DIR** (optional): Directory to store archives (defaults to `./backup`)

### Examples
```bash
# Archive all logs in current directory
./archive.sh

# Archive logs from /var/log to /backups/logs
./archive.sh /var/log /backups/logs

# Archive logs from sample directory
./archive.sh ./sample
```

## Exit Codes

The script returns specific exit codes to indicate success or failure:

- **Exit Code 0**: Success - Log files were successfully archived
- **Exit Code 1**: Error - Various error conditions:
  - Search directory does not exist
  - Cannot create backup directory (permission denied)
  - Archive creation failed
  - Any other command failure

### Example Usage with Exit Codes
```bash
# Success case
./archive.sh sample
echo $?  # Output: 0

# Error case - non-existent directory
./archive.sh /non/existent/directory
echo $?  # Output: 1

# Error case - no log files
./archive.sh /tmp
echo $?  # Output: 1
```
## Archive Contents
The current archive (`logs-20250903.tar.gz`) contains **2 files**:
- `sample/access.log` - Sample access log file
- `sample/errors/error.log` - Sample error log file

## Requirements
- **Operating System**: Unix-like systems (Linux, macOS, BSD)
- **Shell**: Bash
- **Dependencies**: `find`, `tar`, `date`, `mkdir`, `mv` (standard Unix tools)

## Installation
1. Ensure the script has execute permissions:
   ```bash
   chmod +x archive.sh
   ```

2. Run the script:
   ```bash
   ./archive.sh
   ```

## Troubleshooting

### Common Issues
1. **Permission Denied**: Make sure the script is executable (`chmod +x archive.sh`)
2. **No Log Files Found**: The script will exit with code 0 and display a message if no .log files are found
3. **Backup Directory Creation Failed**: Check write permissions for the backup location
4. **Search Directory Not Found**: Ensure the specified search directory exists

### Error Messages
The script provides clear error messages:
- `Error: Directory '/path' not found` - When search directory doesn't exist
- `No log files found in '/path'` - When no .log files exist (exits with code 0)
- `Error: Cannot create backup directory '/path'` - When backup directory creation fails
- Script will exit with code 1 on any command failure due to `set -e`

### Debug Mode
To see what the script is doing, you can run it with bash debugging:
```bash
bash -x archive.sh
```