from reduce_expr import main_reduce_expr

#testy
def tests():
    data = ['a>(b&c)', '(a|b)|(c|a|b) ', '~(~a|~b)', '~a|~~b', '(p/q)/(p/q)' , 'a|~a&(b|~b)|F' , '(a&~b)|(~a&b) ']
    data.extend(['(a&b)&c|b&(a&c)', '(a|~a)&b', '(a&~b)|(~a&b)', '~b&~a|c', 'a>(b&c)', '(a|b)|(c|a|b)', '~(~a|~b)', '~a|~~b', '(p/q)/(p/q)', 'a|~a&(b|~b)|F', '(a&~b)|(~a&b)'])
    logic_expressions = [
        'a', 'b', 'c', '~a', '~b', '~c',
        'a&b', '~a&b', 'a&~b', '~a&~b', 'a|b', '~a|b', 'a|~b', '~a|~b',
        'a&~b|c', 'a|~b&c', '(a&b)|(~c&d)', '~(a|b)&(c|d)',
        '~a&~b', '~(a&b)', '~(~a|b)', '~~a&~b',
        'a&(b|c)', '(a&b)|c', 'a|(~b&c)', '~(a&b&c)',
        'a&b|c', '~(a|b)&c', '((a&b)|c)&~(a|(b&c))  ', 'a&(~b|(c&d))|~(~a&b)|c'
    ]

    data.extend(logic_expressions)
    data.extend(["" , 'a<(b&c)'])
    for d in data: print(d , '-->' ,main_reduce_expr(d))

if __name__ == '__main__':
    tests()