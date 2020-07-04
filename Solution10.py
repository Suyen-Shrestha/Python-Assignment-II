
def snake_case(text,separator=None):
    final_text = [text[0].lower() if text[0].isupper() else text[0]]
    for ch in text[1:]:
        if ch.isupper():
            final_text.append('_')
            final_text.append(ch.lower())
        elif ch == separator:
            final_text.append('_')    
        else:
            final_text.append(ch)

    return ''.join(final_text)


sample_camel_case = 'ThisIsCamelCased'
sample_kebab_case = 'this-is-camel-case'

print(f'The sample camel-cased string: {sample_camel_case}')
print(f'The sample kebab-cased string: {sample_kebab_case}')

print(f'The snake cased output for camel-cased string: {snake_case(sample_camel_case)}')    
print(f'The snake cased output for kebab-cased string: {snake_case(sample_kebab_case,"-")}')    