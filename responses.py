def handle_response(message) -> str:
    p_message = message.lower()
   
    if p_message == "hello":
        return "Hey there"
   
    if p_message == "roll":
        return str(random.randint(1, 6))
   
    if p_message == "!help":
        return "This is HELP"
    
    if "@adi-bot" in p_message:
        return "SIKE: "
    
    return ""  # Return an empty string if no matching response is found
