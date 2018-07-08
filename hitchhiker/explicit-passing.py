def format_output(code, args):
    if not args['color']: 
        return code
    lexer = None 

    # try to find a lexer using the Stack overflow tags
    # or query args 
    for keyword in args['query'].split() + args['tags']:
        try:
            lexer = get_lexer_by_name(keyword)
            break
        except ClassNotFound:
            pass

    # no lexer found above, use the guesser
    if not lexer:
        lexer = guess_lexer(code)

    return highlight(code,
                     lexer,
                     TerminalFormatter(bg="dark")) 

    format_output()
