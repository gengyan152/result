# AutoDL complete project backup

Private backup of `AutoDL_all_projects_20261030.zip` dated 2026-10-30.

The complete original ZIP is stored in [20 split release assets](https://github.com/gengyan152/result/releases/tag/backup-20261030).
The archive includes source code, experiment results, Python environments, and model weights.

- Original ZIP size: 21,082,554,276 bytes
- Part size: 1 GiB, except the final part
- Original ZIP SHA-256: `4aeb1fd66153bc2a517a6a0440fb8bd3e1b6b4a52a4ef61d25422c59595efa50`

## Restore

1. Download all `.partNNN` assets from the release into one directory.
2. Save `restore.py` and `archive-manifest.json` in that directory.
3. Run `python restore.py`.

The script verifies every part, merges the original ZIP, and verifies its SHA-256.
Allow enough disk space for both the downloaded parts and the restored ZIP.
The parts are raw byte segments; concatenate them before opening the ZIP.
