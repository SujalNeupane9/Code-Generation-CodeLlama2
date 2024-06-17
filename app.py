
from fastapi import FastAPI
from ctransformers import AutoModelForCausalLM

##create a new FastAPI app instance
app = FastAPI()

def get_llm():
  model_path = "TheBloke/CodeLlama-7B-GGUF"
  llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-7B-GGUF", model_type="llama")
  return llm

@app.get("/generate")
def generate(text:str) ->dict:
  llm = get_llm()
  res = llm(text)
  return {"text":res}
