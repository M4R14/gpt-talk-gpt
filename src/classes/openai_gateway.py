import openai


class OpenAIGateway:
    engine = "text-davinci-003"
    max_tokens = 1024
    n = 1
    stop = None
    temperature = 0.5

    def __init__(self, engine, api_key):
        self.engine = engine
        openai.api_key = api_key

    def create_completion(self, prompt):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            n=self.n,
            stop=self.stop,
            temperature=self.temperature,
        )

        return response.choices[0].text


class MockGateway:
    def __init__(self):
        pass

    def create_completion(self, prompt):
        return f"Mock response"
