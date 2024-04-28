

def parse_input(user_input: str) -> str | list:
    """
    splits string into 2 parts: cmd and *args
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



def parse_args(args: list) -> str:
    """
    splits args into name and phone. Returns empty values if less args provided
    """
    name = ""
    phone = ""
    if len(args) == 2:
        name, phone = args
    elif len(args) == 1:
        name = args[0]        
    return name, phone



