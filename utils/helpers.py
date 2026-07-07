import hashlib


def generate_document_id(text):

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def format_distance(distance):

    if distance is None:

        return 0

    return round(distance, 4)