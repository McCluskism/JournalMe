# LLM Integration Service

from langchain.llms import HuggingFaceLLM

class LLMIntegrationService:
    def __init__(self, model_name="gpt-2"):
        self.model = HuggingFaceLLM.from_pretrained(model_name)

    def generate_text(self, prompt: str) -> str:
        return self.model(prompt)

    def get_available_models(self):
        # This is a placeholder for future implementation
        return ["gpt-2", "gpt-neo", "gpt-j" ]

# Example usage:
# service = LLMIntegrationService()
# response = service.generate_text("What is the capital of France?")
# print(response)