from typing import TypedDict, Optional

class MA_CFG(TypedDict):
    short_window: int
    mid_window: Optional[int]
    long_window: int

class MOVING_AVERAGE_MODEL:
    
    def calc_ma():
        pass

    def calc_wma():
        pass

    def calc_ema():
        pass


class DOUBLE_MOVING_AVERAGE_MODEL:
    """
    - short_window
    - long_window
    """

    pass


class TRIPLE_MOVING_AVERAGE_MODEL:
    """
    - short_window
    - mid_window
    - long_window
    """
    pass
