from core.domains.account import Account

class AccountService:

    @classmethod
    def get_by_code(cls, code: str) -> Account:
        return Account("id-1", "demo_acc", "Demo Account", True)