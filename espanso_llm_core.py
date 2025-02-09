# Original author: JeansenVaars
# Modified by: Guillaume Thomas
# Donations to JeansenVaars' ko-fi account  -> https://ko-fi.com/JeansenVaars
# JeansenVaars' website -> https://jvhouse.xyz/
# Use at your OWN RISK

import argparse
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

parser = argparse.ArgumentParser(description='LLM calls for Espanso')
parser.add_argument('action', type=str)
parser.add_argument('--prompt', type=str, default=0, help='Text to prompt the AI')
parser.add_argument('--model', type=str, default=None, help='Model to use in OpenRouter')
parser.add_argument('--temperature', type=float, help='Determines randomness levels, where 1 is full risk and 0 certain')
parser.add_argument('--tokens', type=int, help='Max tokens in the response')
parser.add_argument('--remember', type=str, help='Whether to keep the answer in AI memory')
parser.add_argument('--forget', type=str, help='Whether to forget all AI memories and start clean')
parser.add_argument('--memories', type=str, help='Whether to use memories stored so far')
#parser.add_argument('--img_format', type=str, default='markdown', help='Dall-E response format. url, markdown or b64_json')
#parser.add_argument('--img_size', type=str, default='1024x1024', help='Image size for dall-e request')
#parser.add_argument('--img_quality', type=str, default='standard', help='Image quality for dall-e response. standard or hd')
#parser.add_argument('--img_style', type=str, default='vivid', help='Image style for dall-e response. vivid or natural')

args = vars(parser.parse_args())

action = args['action']

if 'CONFIG' not in os.environ:
    raise Exception("Espanso LLM Error: CONFIG key not found. Espanso is not installed?")


# Ensure user config folder structure exists, otherwise opening files will fail due to missing directory.
def check_folders():
    empty_user_folders = ['data_llm', 'config']
    from espanso_llm_common import PBWDIR
    for folder in empty_user_folders:
        fpath = os.path.join(PBWDIR, folder)
        if not os.path.exists(fpath):
            os.makedirs(fpath, exist_ok=True)


if action == 'llm_setup':
    from espanso_llm import setup_llm
    check_folders()
    setup_llm(args['prompt'])
    print("Done")
elif action == 'llm_chat_init':
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        from espanso_llm import *
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        memory_save(prompt, answer, 'w')
        chat_save(messages)
        print(prompt + '\n\n' + answer)
elif action == 'llm_chat':
    check_folders()
    from espanso_llm import *
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    elif not os.path.exists(AI_HISTORY_FILE):
        print('Espanso LLM Error: Call `:llmstart` to begin a chat first.')
    else:
        messages = chat_load()
        messages.append({
            "role": "user",
            "content": prompt
        })
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        memory_save(prompt, answer, 'a')
        chat_save(messages)
        print(prompt + '\n\n' + answer)
elif action == 'llm_chat_isolate':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(prompt + '\n\n' + answer)
# The next clause deals with image generation using Dall-E. It is commented out since it won't work with OpenRouter. I left it here in case a user wants to restore OpenAI access in the script and use Dall-E
# elif action == 'ai_image':
#     from espanso_ai import get_client
#     check_folders()
#     prompt = args['prompt'].strip()
#     img_size = args['img_size']
#     img_format = args['img_format']
#     img_quality = args['img_quality']
#     img_style = args['img_style']
#     client = get_client()
#     response = client.images.generate(
#         prompt=prompt,
#         size=img_size,
#         quality=img_quality,
#         style=img_style,
#         response_format='url' if img_format=='markdown' else img_format,
#         n=1,
#         model='dall-e-3'
#     )
#     if img_format == 'b64_json':
#         answer = response.data[0].b64_json.strip()
#     else:
#         answer = response.data[0].url.strip()
#     if img_format == 'markdown':
#         print('%s\n![%s](%s)' % (prompt, prompt, answer))
#     else:
#         print(answer)
elif action == 'llm_knowledge':
    from espanso_llm import memory_read
    check_folders()
    print(memory_read())
elif action == 'llm_forget':
    from espanso_llm import memory_erase
    check_folders()
    memory_erase()
    print("Espanso AI Memory erased.")
# New functions defined below
elif action == 'quick':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'check_cn':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'check_en':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'check_fr':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'check_pt':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'check_sp':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'cr_cn':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'cr_en':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'cr_fr':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'cr_pt':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'cr_sp':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'tr_cn':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'tr_en':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'tr_fr':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'tr_pt':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
elif action == 'tr_sp':
    from espanso_llm import get_client
    check_folders()
    prompt = args['prompt'].strip()
    if not prompt:
        print('Espanso LLM Error: No prompt given')
    else:
        messages = [{
            "role": "system",
            "content": prompt
        }]
        model = args['model']
        temperature = args['temperature']
        tokens = args['tokens']
        client = get_client()
        response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=tokens)
        answer = response.choices[0].message.content.strip()
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
else:
    raise Exception("Wrong Function argument!")