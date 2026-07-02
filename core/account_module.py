from injector import Module, provider, singleton
from core.account_service import AccountService
from rest.account_endpoints import AccountResource


class AccountModule(Module):

    @provider
    @singleton
    def account_service(self) -> AccountService:
        return AccountService()

    @provider
    @singleton
    def account_resource(self, service: AccountService) -> AccountResource:
        return AccountResource(service)