import secrets
import string


alphabet = string.ascii_letters + string.digits


def random_string(length: int) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


def to_url(query_parameters: dict) -> str:
    return "?" + "&".join(map(lambda x: f"{x[0]}={x[1]}", query_parameters.items()))
