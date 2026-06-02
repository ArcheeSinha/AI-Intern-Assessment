from utils.chatbot import get_response
from utils.validator import validate_query
from utils.logger import save_conversation

chat_history = []

while True:

    user_query = input("You: ")

    if user_query.lower() == "exit":
        break

    if not validate_query(user_query):

        print(
            "\nAssistant: Please enter a valid question."
        )

        continue

    answer = get_response(user_query)

    save_conversation(
        user_query,
        answer
    )

    chat_history.append(
        {
            "user": user_query,
            "assistant": answer
        }
    )

    print("\nAssistant:")
    print(answer)

    print("\n===== CHAT HISTORY =====")

    for chat in chat_history:

        print(f"\nUser: {chat['user']}")
        print(f"Assistant: {chat['assistant']}")