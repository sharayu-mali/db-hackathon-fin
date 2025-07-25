
# from google.colab import auth
# init(project="flowing-design-466913-e5", location="us-central1")
from google import genai
from google.genai import types
import logging
from embedder import get_context
llm = genai.Client(
vertexai=True, project="flowing-design-466913-e5", location="global",
)
# If your image is stored in Google Cloud Storage, you can use the from_uri class method to create a Part object.
model = "gemini-2.5-flash-lite"
google_api_key = "AIzaSyBh-emCSHKlWdhyzbfoS12MkQa0ShjF8_Y"


# Init Gemini model
# chat_model = ChatModel.from_pretrained("chat-bison@001")  # or "gemini-1.5-pro-preview"
# chat = chat_model.start_chat()
client = genai.Client(api_key=google_api_key)


def generate_response(business,query, profile):
    logging.info("Business",business)
    context = get_context(business)

    prompt = f"""
You are a business advisor specialized in Indian Retail.

User Profile:
{profile}

Business Context
{context}

User Query:
{query}

Provide a short, actionable recommendation in simple terms.
"""
    # response = llm.models.generate_content(
    # model=model,
    # contents=[
    # prompt
    # ],
    # )
    
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt 
    )
    logging.info(response.text, end="")
    return {"text":response.text.strip()}
