from lab2.decorators import bracket

#TODO NWM czy to ma sens i jak jest 2**ilosc grupek dnf

def to_implications(dnf_expr:str , a:str , b:str) -> str:
    dnf_expr = dnf_expr.replace(f'~{a}|{b}', f'{a}>{b}')
    dnf_expr = dnf_expr.replace(f'{b}|~{a}', f'{a}>{b}')
    return dnf_expr


def match_patters(dnf_expr , variables):
    dnf_expr_list = dnf_expr.split('|')
    dnf_expr_list = [bracket(e) for e in dnf_expr_list]
    dnf_expr_list = [e for e in dnf_expr_list if 1<len(e)<=4]



    #wybieram po 2 grupki i prubuje laczyc

