contacts = {}
def add_contact(name, phone, email)
    if name in contacts:
        return f"Error: Contact '{name}' already exists."
    contacts[name] = {"phone": phone, "email": email}
    return f"Success: Contact '{name}' has been added."

def main():
    print(add_contact("Alice", "555-1234", "alice@email.com"))
    print(add_contact("Bob", "555-5678", "bob@email.com"))
    print(add_contact("Alice", "555-9999", "alice2@email.com"))



if __name__ == "__main__":
    main()
