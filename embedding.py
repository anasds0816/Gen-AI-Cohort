from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client= OpenAI()

text="The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in Agra, Uttar Pradesh, India. It was commissioned in 1631 by the fifth Mughal emperor, Shah Jahan, to house the tomb of his beloved wife, Mumtaz Mahal; it also houses the tomb of Shah Jahan himself."

response=client.embeddings.create(
    input=text,
    model='text-embedding-3-small'
)

print("Vector Embeddings", response.data[0].embedding)
