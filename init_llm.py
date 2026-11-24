"""
init_chat_model 初始化聊天模型
"""
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel


from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, OPENAI_API_KEY, OPENAI_BASE_URL, ANTHROPIC_API_KEY, \
    ANTHROPIC_BASE_URL, HUNYUAN_APP_ID, HUNYUAN_SECRET_ID, HUNYUAN_SECRET_KEY, DASHSCOPE_API_KEY, ZHIPUAI_API_KEY, \
    ZHIPUAI_BASE_URL, DASHSCOPE_BASE_URL

deepseek_llm: BaseChatModel = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)


openai_llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai",
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)

anthropic_llm = init_chat_model(
    # model="claude-3-5-haiku-latest",
    model="claude-haiku-4-5-20251001",
    model_provider="openai",
    api_key=ANTHROPIC_API_KEY,
    base_url=ANTHROPIC_BASE_URL,
)


ollama_llm = init_chat_model(
    model="deepseek-r1:7b",
    model_provider="ollama",
    base_url="http://127.0.0.1:11434",
)


tongyi_llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,

)

zhipu_llm = init_chat_model(
    model="glm-4",
    model_provider="openai",
    api_key=ZHIPUAI_API_KEY,
    base_url=ZHIPUAI_BASE_URL,

)
