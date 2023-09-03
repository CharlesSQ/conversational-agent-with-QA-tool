# Custom Chat Agent with Langchain and GPT-3.5

This repository contains code that demonstrates how to build a custom chat agent using Langchain, integrating GPT-3.5 from OpenAI. The agent can handle conversational context, provide various tools, and assist in answering questions, including math-related queries.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The project showcases the implementation of a custom chat agent that leverages Langchain, an open-source framework, to interact with users in a conversational manner. The agent uses a conversational business document search tool. This agent is powered by GPT-3.5 for natural language understanding and generation.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`
3. Obtain an API key from OpenAI and set it in the `OPENAI_API_KEY` field in the `config.py` file.
4. Obtain API keys for Pinecone and set them in the `config.py` file.
5. Get a previously created Pinecone index name, for document retrieval and set it in the `constants.py` file.

## Usage

To use the custom chat agent:

1. Run the provided Python script: `python main.py`
2. Enter your message as a user prompt.
3. The agent will process the input and respond with relevant information or tools.

## Configuration

The configuration of the chat agent can be customized by modifying the parameters in the `main.py` script. Key components include:

- Memory: Adjust the conversation memory buffer settings.
- Tools: Define and configure different tools the agent can use.
- Prompt Template: Modify the structure of the prompt used to interact with GPT-3.5.
- Output Parsing: Configure how the agent interprets and processes the model's responses.

## License

This project is licensed under the [MIT License](LICENSE).
