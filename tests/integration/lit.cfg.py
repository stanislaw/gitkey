import os
import sys

import lit.formats


THIS_DIR = os.path.dirname(__file__)
REPO_ROOT = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
TOOLS_DIR = os.path.join(THIS_DIR, "tools")

config.name = "gitkey-integration"
config.test_format = lit.formats.ShTest(execute_external=True)
config.suffixes = [".test"]
config.test_source_root = THIS_DIR
config.test_exec_root = os.path.join(REPO_ROOT, "build", "lit")

gitkey_path = os.path.join(REPO_ROOT, "gitkey")
config.environment["GITKEY_BIN"] = (
    "env HOME=%t/home "
    "GIT_CONFIG_GLOBAL=/dev/null "
    "GIT_CONFIG_SYSTEM=/dev/null "
    "GITKEY_TEST_INPUT=1 "
    f"{gitkey_path}"
)

expect_exit = os.path.join(TOOLS_DIR, "expect_exit.py")
config.substitutions.append(("%expect_exit", f"{sys.executable} {expect_exit}"))
