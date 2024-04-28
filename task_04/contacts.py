

def add_contact(name: str, phone: str, contacts: dict) -> str | dict:
    """
    add new contact to contacts
    """
    if name and phone:
        if name not in contacts.keys():
            contacts[name] = phone
            result = "Contact added."
        else:
            result = "The contact with name " + name + " already exists; phone: " + contacts[name]
    else:
        result = "Provide name and phone."
    return result, contacts



def change_contact(name: str, phone: str, contacts: dict) -> str | dict:
    """
    change phone number for existing contact in contacts
    """
    if name and phone:
        if name in contacts.keys():
            contacts[name] = phone
            result =  "Contact updated."
        else:
            result = "The contact with name " + name + " not found."
    else:
        result = "Provide name and phone."
    return result, contacts
 


def show_phone(name: str, contacts: dict) -> str:
    """
    show phone number for existing contact in contacts
    """
    if name:
        if name in contacts.keys():
            result =  contacts[name]
        else:
            result = "The contact with name " + name + " not found."
    else:
        result = "Entry contact name."
    return result

