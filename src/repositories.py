from src.models import Account
from src.schemas import AccountLoggedinInfo
from src.db import get_session


class BaseRepository:
    MODEL_CLS = None

    @property
    def _session(self):
        return get_session()

    def add(self, entity):
        self._session.add(entity)
        self._session.flush()
        return entity


class AccountRepository(BaseRepository):
    MODEL_CLS = Account

    def login(self, username: str, password: str) -> AccountLoggedinInfo:
        account = (
            self._session.query(self.MODEL_CLS)
            .filter_by(username=username)
            .one_or_none()
        )
        if not account:
            return AccountLoggedinInfo(status=False, message="user not found")
        elif not self.verify_password(account, password):
            return AccountLoggedinInfo(
                status=False, message="incorrect password"
            )
        else:
            return AccountLoggedinInfo(status=True, message="success")

    def verify_password(self, account: Account, password: str) -> bool:
        return account.password == password


account_repo = AccountRepository()
