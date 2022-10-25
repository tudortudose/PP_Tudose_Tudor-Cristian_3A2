def build_xlm_element(tag, content, **args):
    string = "<" + tag + " "
    for arg in args:
        print(arg, args[arg])
        string += arg + " = \\\"" + args[arg] + "\\\""
    string += "> " + content + " </" + tag + ">"
    return string
