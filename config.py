import os

# Allow either DEEPSEEK_API_KEY or OPENAI_API_KEY to be used for API key configuration.
# This makes it easier to run the project when an OpenAI-style env var is set.
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
# Allow overriding the model via env var, default to DeepSeek model name used previously.
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")