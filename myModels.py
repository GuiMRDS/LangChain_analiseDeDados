from groq import Groq

from myKeys import GROQ_API

client = Groq(api_key=GROQ_API)

models = client.models.list()

for model in models.data:
    print(model.id)
