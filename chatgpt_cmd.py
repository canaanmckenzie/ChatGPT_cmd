import openai
import argparse

#set up openAI api Key
openai.api_key = "API_KEY"

#generate ai response
def generate_response(prompt,model,temperature=0.5):
    response = openai.Completion.create(
        engine = model,
        prompt=prompt,
        max_tokens=1024,
        temperature = temperature,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

#define command line args
parser = argparse.ArgumentParser(description='Generate AI response from OpenAI API')
parser.add_argument('--model', metavar='MODEL', type=str, default='davinci', help='The Name of the OpenAI model to use (default: davinci)')
parser.add_argument('--temperature', metavar='TEMP',type=float,default=0.5, help='The sampling temperature to use (default: 0.5)')
parser.add_argument('prompt',metavar='PROMPT',type=str,help='The prompt to use fro generating AI response')

#parse cmd-line args
args = parser.parse_args()

#gen response and print it
response = generate_response(args.prompt, args.model, args.temperature)
print(response)