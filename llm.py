from litellm import completion
from deepeval.models.base_model import DeepEvalBaseLLM

class LLM(DeepEvalBaseLLM):
    def __init__(
        self,
        model
        ):
        self.model = model

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        model = self.load_model()
        # print('model: ', model)

        response = completion(
            model=model,
            messages=[{ "content": prompt, "role": "user"}], 
            temperature=0.1
            # api_base="http://localhost:11434"
        )
        return response['choices'][0]['message']['content']
    
    async def a_generate(self, prompt: str) -> str:
        # print(prompt)
        return self.generate(prompt)
    
    def get_model_name(self):
        return self.model