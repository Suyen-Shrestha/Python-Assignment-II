

def valid_parantheses(input_str):
    par_dict = {'(':')','{':'}','[':']'} # dictionary where open parantheses are mapped with closing parantheses.
    par_list = []

    for p in input_str:
        if p in par_dict:
            par_list.append(p)
        elif len(par_list) == 0 or par_dict[par_list.pop()] != p:
            return False
    return len(par_list) == 0

sample_parantheses = "()[{)}"
output = valid_parantheses(sample_parantheses)
print(f'Sample paranthesis string: "{sample_parantheses}"')
if output:
    print('Valid paranthesis string!')
else:
        print('Invalid paranthesis string!')         