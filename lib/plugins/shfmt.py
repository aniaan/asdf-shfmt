import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="shfmt",
    cmd="shfmt",
    repo_name="mvdan/sh",
    filename_template="shfmt_{version}_{platform}_{arch}",
    arch_map={
        "x86_64": "amd64",
        "aarch64": "arm64",
    },
    checksum_filename_template="sha256sums.txt",
    bin_path="shfmt",
    recover_raw_version=lambda x: f"v{x}",
    is_compressed=False,
)
