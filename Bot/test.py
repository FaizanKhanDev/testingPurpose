from ccxt.base.decimal_to_precision import decimal_to_precision  # noqa F401
from ccxt.base.decimal_to_precision import TRUNCATE  # noqa F401
from ccxt.base.decimal_to_precision import ROUND  # noqa F401
from ccxt.base.decimal_to_precision import DECIMAL_PLACES  # noqa F401
from ccxt.base.decimal_to_precision import SIGNIFICANT_DIGITS  # noqa F401
from ccxt.base.decimal_to_precision import TICK_SIZE  # noqa F401
from ccxt.base.decimal_to_precision import PAD_WITH_ZERO  # noqa F401
from ccxt.base.decimal_to_precision import NO_PADDING  # noqa F401
from ccxt.base.decimal_to_precision import number_to_string


min_amount_m = 0.009300000000000001
round_size = 2

quantity_m = float(decimal_to_precision(min_amount_m,
                                        ROUND,
                                        round_size,
                                        DECIMAL_PLACES))


print(
    quantity_m
)
