def validate_query(user_query):

    if not user_query:
        return False

    if len(user_query.strip()) == 0:
        return False

    return True