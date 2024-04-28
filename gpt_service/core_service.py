from openai import OpenAI

client = OpenAI(
    organization="",
    project="",
)


class GPTRecipeService:
    def fetch_recipe(self):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Give me a recipe that I can cook today"},
            ],
        )
        print(completion)
        return "recipe fetched"
