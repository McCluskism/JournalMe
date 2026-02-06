import random

class PromptProcessor:
    def __init__(self):
        self.prompts = [
            "What is something you learned this week?",
            "Reflect on a challenge you faced. How did you overcome it?",
            "What is a recent accomplishment that you are proud of?",
            "How did you take care of yourself today?",
            "What are you grateful for in this moment?",
            "What was a highlight of your day?",
            "What would you like to improve about yourself?",
            "Describe a situation where you felt empowered."
        ]

    def get_prompt(self):
        return random.choice(self.prompts)

if __name__ == '__main__':
    processor = PromptProcessor()
    print(processor.get_prompt())