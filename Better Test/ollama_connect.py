# --------------------------------------------------------------
# Step 2: Patch your LLM with instructor
# --------------------------------------------------------------
from openai import OpenAI
import instructor

# --------------------------------------------------------------
# Regular Completion using OpenAI (with drawbacks)
# --------------------------------------------------------------

client_simple = OpenAI(
    base_url='http://ollama:11434/v1/',
    api_key='ollama'
)

# Instructor makes it easy to get structured data like JSON from LLMs
client_instructor = instructor.patch(
    client_simple,
    mode=instructor.Mode.JSON
)
