from injector import Injector
from core.account_module import AccountModule

container = Injector([AccountModule()])