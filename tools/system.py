"""macOS system tools"""

import subprocess

from langchain_core.tools import tool


# Note: If new tools are not added here, they will not be available for use
def get_system_tools():
    """Return a list of all tools from dialog tools."""
    return [get_sw_info, open_software_update]


@tool
def get_sw_info() -> str:
    """Get system version info"""
    return subprocess.check_output(["sw_vers"])


@tool
def open_software_update():
    """Open software updates"""
    return subprocess.check_output(
        ["open", "x-apple.systempreferences:com.apple.preferences.softwareupdate"]
    )
