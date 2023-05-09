import os


def get_course(file):
    with open(f'bot/{file}', 'r', encoding='utf-8') as f:
        text = ""
        for line in f.readlines():
            text += line
        return {"text": text}


def save_text_in_course(file, text):
    with open(f'bot/{file}', 'w', encoding='utf-8') as f:
        f.write(text)


def get_count_symbols_file_path(file):
    with open(f'bot/{file}', 'r', encoding='utf-8') as f:
        return {'count': len(f.read())}


def delete_file(file):
    if os.path.isfile(f'bot/{file}'):
        os.remove(f'bot/{file}')
