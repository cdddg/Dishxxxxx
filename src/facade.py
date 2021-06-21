from src.repositories import account_repo


def login(username: str, password: str):
    return account_repo.login(username=username, password=password)
