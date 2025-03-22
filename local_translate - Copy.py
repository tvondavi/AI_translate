import pandas as pd
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Name of local LLM
local_llm = "deepseek-r1:8b"

# Load the CSV data
df = pd.read_csv("w_inscription.csv")

# Identify the column to translate
column_to_translate = "inscription text"

# Create a translation chain
llm = ChatOllama(model=local_llm, temperature=0)  # Ensure GPU usage
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Translate the following text to English: {text}"
)
translation_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=False)

# Convert text column into a list for batch processing
texts = df[column_to_translate].tolist()

# **Batch Processing** - Translate multiple texts at once
batch_size = 10  # Adjust based on your system's capability
translated_texts = []

for i in range(0, len(texts), batch_size):
    batch = texts[i:i+batch_size]
    batch_results = [translation_chain.predict(text=text) for text in batch]
    translated_texts.extend(batch_results)

# Add translations to DataFrame
df["translated_text"] = translated_texts

# Save the translated data
df.to_csv("translated_file.csv", index=False)

# Output the translations as a list
print(translated_texts)