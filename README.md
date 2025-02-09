# What is this application?

This [Espanso](https://espanso.org/) extension allows you to use a text expander to make requests to Large Language Models routed by OpenRouter. With it, you can perform the following tasks in most user interfaces that accept text intput:

- Have a chat with an LLM
- Ask a single question to an LLM
- Ask an LLM to check, correct or translate text in Chinese, English, French, Brazilian Portuguese or Spanish

If you are willing to edit YAML and Python files, you can also define your own Espanso shortcuts and associate them with custom prompts, or change the LLM client to connect to any OpenAI compatible LLM API.

# Who wrote this?

I didn't. The files in this repository were extracted from Play by the Writing, a larger application meant to assist users who play TTRPGs:

- https://github.com/saif-ellafi/play-by-the-writing
- https://jeansenvaars.itch.io/play-by-the-writing

I merely extracted the functionality that I thought would be useful to a broader user base. I also renamed a bunch of variables, so that Play by the Writing users can use it along with the present expansion.

If you like this expansion, you can support JeansenVaars by purchasing Play by the Writing from [itch.io](https://jeansenvaars.itch.io/play-by-the-writing)
w

# Installation guide

1. Install Espanso and check that it's working on your machine
2. Install Python and pip
3. Install the [Python openai library](https://pypi.org/project/openai/)
4. Locate your [espanso directory](https://espanso.org/docs/configuration/basics/)
5. Drop the file `espanso_llm.yml` in the `match` folder of your `espanso` directory
6. If there isn't a `scripts` folder in your `espanso` directory, create one
7. Drop the files `espanso_llm.py`, `espanso_llm_common.py` and `espanso_llm_core.py` in the `scripts` folder

# Setup

Once the extension is installed, you need to set up LLM access. First, you need to get an [OpenRouter key](https://openrouter.ai/docs/api-reference/authentication). Then, with Espanso running, type `:llmsetup` in any text-based interface, for instance a plain text editor. This will ask you for an LLM key. The extension will create a folder called `EspansoLLM` in your user directory. Your OpenRouter LLM will be stored in an **unencrypted** `openrouter.txt` file inside a `config` subfolder.

# Using the extension

As it is the extension defines the following commands:
