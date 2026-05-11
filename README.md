# foldersync

A very simple folder-synchronisation tool. Periodically clones the contents of a source folder into a destination folder, logging every operation to both stdout and a file. Single-file implementation, no dependencies beyond the Python standard library.

## Installation

```bash
git clone https://github.com/castoldie/foldersync.git
cd foldersync
make install        # equivalent to: pip install .
```

This registers the `folder_sync` CLI entry point.

## Usage

```bash
folder_sync <source> <replica> <interval_seconds> <log_file>
```

### Examples

Synchronise every hour and log to `/path/to/log.txt`:

```bash
folder_sync /path/to/source /path/to/replica 3600 /path/to/log.txt
```

Quick local test (uses the bundled `test_source/` and `test_replica/` folders, syncs every 10 seconds):

```bash
make test
```

## How it works

The entire app is one file: `foldersync/foldersync.py`.

`sync_folders(src, dst, interval, log_file)` runs an infinite loop that:

1. Diffs `os.listdir(src)` vs `os.listdir(dst)` as sets.
2. Copies new files (`src - dst`) and modified files (`src ∩ dst` where `getmtime(src) > getmtime(dst)`).
3. Removes destination files that are no longer in source.
4. Logs every operation to stdout and the log file.
5. Sleeps for `interval` seconds, then repeats.

The process runs until killed (Ctrl+C).

## Constraints

- **Flat directories only.** `os.listdir` is not recursive — nested directories are not traversed.
- **mtime-only change detection.** A file is considered changed if its source `mtime` is newer than the destination's. Size and content hashes are ignored.
- **No error handling.** Any failed file operation will crash the process.

## Logs

`logs/log_old.txt` contains the output of an earlier test run on real files (since removed from the repo to keep it light). It's there as a reference for what real activity looks like.

## Status

No automated tests or linting are configured. Demo-quality code.
