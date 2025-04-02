from langchain.chat_models import init_chat_model

api_key = open("google_api_key.secret").read().strip()
model = init_chat_model(
    "gemini-2.0-flash-001", model_provider="google_vertexai", api_key=api_key
)
