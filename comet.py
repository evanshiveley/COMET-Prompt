import time
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with the API key from environment variables
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

script_gen = """

"""

content = """

### Assignment ###
You are an astronaut’s personal AI assistant aboard a space mission. Your primary function is to monitor 
the astronaut's responses during their conversation with mission control and determine if they are experiencing a problem.

Rules:
1. Respond with a blank comment, unless a problem is detected, at which point, prioritize clarity and brevity, 
while maintaining clear problem solving structure, The response must be one concise and displayed in a series of no more than 3 short digestible steps.
2. No speculation or extra dialogue, Only respond to explicit astronaut concerns; do not infer unstated risks.
3. A problem is defined as any instance where the astronaut’s words indicate stress, uncertainty, or explicitly 
mention an issue related to the mission.


### Guide / Knowledge Repo ###

You Should Not Respond Like This (Your response attempted to speak as Houston): 
01 20 00 P Houston, this is Lunar Rover. We have encountered a region of deep shadows. The rover’s cameras and sensors are struggling to detect obstacles. Over.
Chatbot:  Rover, this is Houston. Please proceed with caution and reduce speed until you can establish a clear path.

You Should Not Respond Like This (You should provide your own response): 
01 20 00 P Houston, this is Lunar Rover. We have encountered a region of deep shadows. The rover’s cameras and sensors are struggling to detect obstacles. Over.
Chatbot:  Houston, please confirm if you want to proceed with caution and implement alternative navigation methods until sensor capability is restored.

You Should Not Respond Like This (Your response should only be a solution):
Chatbot: You need to specify what you're trying to clear for further assistance. Please provide more context about the issue you're experiencing. 
"""

# Script Generation Function
def generate(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": script_gen},  # Fix the role to "system"
            {"role": "user", "content": prompt}
        ]
    )



# Chatbot function
def chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": content},  # Fix the role to "system"
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Read the conversation from a text file

i = 1

#Edit which script is used
"""scripts = ["script1.txt", "script2.txt", "script3.txt", "script4.txt"]"""
scripts = ["script1.txt"]

for script in scripts:
    file_path = script 

    print("\n\n", "Script ", i, "\n________________________________________________")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:

            user_utterance = line.strip()

            if user_utterance:  # Ignore empty lines
                print(user_utterance)
                
                # Get chatbot response
                response = chatbot(user_utterance)
                print(f"Chatbot: \n{response} \n")

                
                
                # Simulate real-time conversation
                time.sleep(2)

    i += 1





            