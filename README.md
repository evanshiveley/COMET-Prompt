# README - Comet AI Assistant

## Overview
`comet.py` is a Python script designed to act as an AI assistant for astronauts during a space mission. It monitors astronaut conversations with mission control and detects potential issues based on predefined rules.

## Features
- Uses OpenAI's GPT model to analyze astronaut communications.
- Detects stress, uncertainty, or explicit mission-related issues.
- Responds concisely with a structured 3-step problem-solving approach.
- Reads conversation scripts from text files and simulates real-time interaction.

## Requirements
- Python 3.x
- OpenAI API Key (stored in environment variables)
- Required dependencies: `openai`, `dotenv`

## Installation
1. Clone or download the repository.
2. Install dependencies using:
   pip install openai python-dotenv
4. Set up the `.env` file with your OpenAI API key


## Usage
Run the script with:
python comet.py
