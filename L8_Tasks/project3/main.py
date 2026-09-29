from config import get_bank_name
from accounts.account import create_account
from accounts.authentication import login
from payments.fee import calculate_fee
from payments.payment import make_payment



get_bank_name()
create_account()
login()
calculate_fee()
make_payment()
