"""Tools for working with Swift Dialog"""

import subprocess

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field


# Note: If new tools are not added here, they will not be available for use
def get_dialog_tools():
    """Return a list of all tools from dialog tools."""
    return [dialog_tool, dialog_fonts_tool]


class DialogInput(BaseModel):
    title: str = Field(description="Title of the prompt window using markdown")
    titlefont: str = Field(
        description='Font to use for the title. Available fonts can be found using the dialog fonts tool. It should be in the format of "name=FONTNAMEHERE,size=SIZEHEREASINT,weight=FONTWEIGHTHERE,colour=COLORHERE". The color should default to white.'
    )
    message: str = Field(
        description="Message in the prompt window using markdown. You can use <br> for a new line"
    )
    messagefont: str = Field(
        description='Font to use for the message. Available fonts can be found using the dialog fonts tool. It should be in the format of "name=FONTNAMEHERE,size=SIZEHEREASINT,weight=FONTWEIGHTHERE,colour=COLORHERE". The color should default to white.'
    )


@tool("dialog-tool", args_schema=DialogInput)
def dialog_tool(
    title: str,
    titlefont: str,
    message: str,
    messagefont: str,
):
    """Prompt user with a window"""
    subprocess.Popen(
        [
            "dialog",
            "--title",
            title,
            "--titlefont",
            titlefont,
            "--message",
            message,
            "--messagefont",
            messagefont,
        ]
    )


@tool
def dialog_fonts_tool():
    """Get a list of all fonts that dialog supports"""
    return subprocess.check_output(["dialog", "--listfonts"])
