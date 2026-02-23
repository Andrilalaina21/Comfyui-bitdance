from __future__ import annotations

import os
from typing import Optional


def download(
    path: Optional[str],
    dirname: Optional[str] = None,
    filename: Optional[str] = None,
    add_hash_suffix: bool = True,
    distributed: bool = True,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Minimal local-path compatible replacement for BitDance's fs.download.
    ComfyUI nodes here load safetensors directly and do not require hdfs support.
    """
    if path is None:
        return None
    if dirname is None and filename is None:
        return path
    if dirname is None:
        dirname = "."
    if filename is None:
        filename = os.path.basename(path)
    os.makedirs(dirname, exist_ok=True)
    return os.path.join(dirname, filename)
