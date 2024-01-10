import openai

openai.api_key = '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'

brukerinput = "Hei, hvordan har du det?"
svar = openai.Completion.create(
    model="gpt-3.5-turbo",  # Velg riktig modellnavn
    prompt=brukerinput,
    max_tokens=10  # Juster etter behov
)

gpt_svar = svar['choices'][0]['text']
print(gpt_svar)

