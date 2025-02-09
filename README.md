# What is this application?

This [Espanso](https://espanso.org/) snippet allows you to use a text expander to make requests to Large Language Models routed by OpenRouter. With it, you can perform the following tasks in most user interfaces that accept text intput:

- Have a chat with an LLM
- Ask a single question to an LLM
- Ask an LLM to check, correct or translate text in Chinese, English, French, Brazilian Portuguese or Spanish

If you are willing to edit YAML and Python files, you can also define your own Espanso shortcuts and associate them with custom prompts, or change the LLM client to connect to any OpenAI compatible LLM API.

# Who wrote this?

I didn't. The files in this repository were copied and adapted from Play by the Writing, a larger application meant to provide several utilities to TTRPG players:

- https://github.com/saif-ellafi/play-by-the-writing
- https://jeansenvaars.itch.io/play-by-the-writing

I merely extracted the functionality that I thought would be useful to a broader user base. I also renamed a bunch of variables, so that the present extension can be used alongside Play by the Writing.

If you like this extension, you can:

- support JeansenVaars by purchasing Play by the Writing from [itch.io](https://jeansenvaars.itch.io/play-by-the-writing)
- support the creator of Espanso by [making a small donation](https://espanso.org/donate/)

# Installation guide

1. [Install Espanso](https://espanso.org/install/) and [check that it's working on your machine](https://espanso.org/docs/get-started/)
2. Install [Python](https://www.python.org/downloads/) and [make sure you have a working pip](https://pip.pypa.io/en/stable/getting-started/)
3. Install the [Python openai library](https://pypi.org/project/openai/)
4. Locate your [espanso directory](https://espanso.org/docs/configuration/basics/)
5. Drop the file `espanso_llm.yml` in the `match` directory of your `espanso` directory
6. If there isn't a `scripts` directory in your `espanso` directory, create one
7. Drop the files `espanso_llm.py`, `espanso_llm_common.py` and `espanso_llm_core.py` in the `scripts` directory

# Setup

After the files have been copied to their respective directories, you need to set up LLM access. First, you need to get an [OpenRouter key](https://openrouter.ai/docs/api-reference/authentication). Then, with Espanso running, type `:llmsetup` in any text-based interface, for instance a plain text editor. This will open a form that requests an OpenRouter API key. The setup script will create a directory named `EspansoLLM` in your user directory. Your API key will be stored in an **unencrypted** `openrouter.txt` file inside a `config` subdirectory.

# Using the extension

In its present form, the snippet defines the following triggers (see `espanso_llm.yml` for a full list with trigger aliases):

| Trigger | Output |
| --- | --- |
| `:llmsetup` | Setup OpenRouter API Key |
| `:llmcall` | Open command menu |
| `:llmnew` | New LLM conversation |
| `:llmchat` | Continue LLM conversation |
| `:llmsingle` | Single LLM question |
| `:llmclear` | Clear LLM conversation |
| `:llmlog` | Show LLM conversation history |
| `:quick` | Send request in clipboard to LLM |
| `:check_cn` | Check Chinese clipboard content |
| `:check_en` | Check English clipboard content |
| `:check_fr` | Check French clipboard content |
| `:check_pt` | Check Brazilian Portuguese clipboard content |
| `:check_sp` | Check Spanish clipboard content |
| `:cr_cn` | Correct Chinese clipboard content |
| `:cr_en` | Correct English clipboard content |
| `:cr_fr` | Correct French clipboard content |
| `:cr_pt` | Correct Brazilian Portuguese clipboard content |
| `:cr_sp` | Correct Spanish clipboard content |
| `:tr_cn` | Translate clipboard content to Chinese |
| `:tr_en` | Translate clipboard content to English |
| `:tr_fr` | Translate clipboard content to French |
| `:tr_pt` | Translate clipboard content to Brazilian Portuguese |
| `:tr_sp` | Translate clipboard content to Spanish |
