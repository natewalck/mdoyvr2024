"""Tools for manipulating Munki"""

import subprocess

from langchain_core.tools import tool


# Note: If new tools are not added here, they will not be available for use
def get_munki_tools():
    """Return a list of all tools from dialog tools."""
    return [get_munki_version]


@tool
def get_munki_version() -> str:
    """Get munki version"""
    return subprocess.check_output(["managedsoftwareupdate", "--version"])
