from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_OPENAI
from autogen_core.models import ModelInfo
import os 
from dotenv import load_dotenv
load_dotenv() 


def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model = MODEL_OPENAI,
        api_key= os.getenv('GROQ_API_KEY'),
        base_url="https://api.groq.com/openai/v1",
        model_info=ModelInfo(
            # These capabilities are what AutoGen needs to know
            vision=False,
            function_calling=True,   # Groq supports tool/function calling via OpenAI-compatible API
            json_output=True,        # model can output JSON (best-effort)
            family="groq"
        ),

    )
    return openai_model_client