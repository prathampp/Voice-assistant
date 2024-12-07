from openai import OpenAI
from config import apikey

def chat(query, chatStr):
    try:
        client = OpenAI(api_key=apikey)
        chatStr += f"Aashif: {query}\n Pythia: "

        if "who created you" in query.lower() or "who made you" in query.lower():
            return "I was created by MD Aashif using OpenAI's GPT-3 model."

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=chatStr,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # //gg

        text = response.choices[0].text.strip()
        chatStr += f"{text}\n"

        with open(f"Openai/{''.join(query.split('intelligence')[1:])}.txt", "w") as f:
            f.write(text)

        return text

    except Exception as e:
        print("An error occurred:", e)
        return "Some Error Occurred. Sorry, from Pythia"

def ai(prompt):
    try:
        client = OpenAI(api_key=apikey)

        if "who created you" in prompt.lower() or "who made you" in prompt.lower():
            return "I was created by MD Aashif using OpenAI's GPT-3 model."

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        text = response.choices[0].text.strip()

        with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
            f.write(text)

        return text

    except Exception as e:
        print("An error occurred:", e)
        return "Some Error Occurred. Sorry, from Pythia"
