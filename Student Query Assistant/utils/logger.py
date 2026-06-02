import csv
import os

from datetime import datetime


def save_conversation(
    user_query,
    assistant_response
):

    file_path = "logs/conversations.csv"

    file_exists = os.path.isfile(
        file_path
    )

    with open(
        file_path,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow(
                [
                    "Timestamp",
                    "User Query",
                    "Assistant Response"
                ]
            )

        writer.writerow(
            [
                datetime.now(),
                user_query,
                assistant_response
            ]
        )