"""
创建一个Agent：调用工具回答用户问题
"""
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from my_llm import deepseek_llm

@tool
def get_weather(location: str) -> str:
    """
    获取指定位置的天气信息
    :return:
    """
    return f"天气信息：{location}的天气是晴朗的"

agent = create_agent(
    model=deepseek_llm,
    tools=[get_weather],
    system_prompt="你是一个 helpful的助手，只能使用提供的工具来回答用户问题。"
)

# 调用Agent
# 第一种写法
resp = agent.invoke(HumanMessage(content="北京的天气如何"))
print(resp)
# 第二种写法
resp1 = agent.invoke({"messages": [{"role": "user", "content": "深圳的天气如何"}]})
print(resp1)

