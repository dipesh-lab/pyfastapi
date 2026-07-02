import logging

from fastapi import status, APIRouter
from core.account_service import AccountService
from rest.models.common_models import DataWrapper

from core.domains import account

logger = logging.getLogger("account_resource")

class AccountResource:

    def __init__(self, service: AccountService):
        self.service = service
        self.router = APIRouter()
        self.router.add_api_route(
            "/accounts",
            self.get_account,
            methods=["GET"],
            response_model=DataWrapper[account.Account]
        )

    async def get_account(self) -> DataWrapper[account.Account]:
        logger.info("Root endpoint called")
        acc = self.service.get_by_code("demo_acc")
        return DataWrapper(data=acc)