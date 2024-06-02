#!/usr/bin/env python3

# import subprocess
import sys

# from langchain_core.tools import tool

from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent

from langchain_openai import ChatOpenAI

from tools.system import get_system_tools
from tools.munki import get_munki_tools
from tools.dialog import get_dialog_tools


def main() -> None:
    """Main function"""
    user_input = sys.argv[1:]
    print(user_input)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.1)
    prompt = hub.pull("hwchase17/openai-functions-agent")
    # tools = get_function_tools(
    tools = []
    tools = tools + get_dialog_tools()
    tools = tools + get_system_tools()
    tools = tools + get_munki_tools()
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({"input": user_input})


main()
