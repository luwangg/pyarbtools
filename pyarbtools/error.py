"""
error
Author: Morgan Allison, Keysight RF/uW Application Engineer
Custom error classes for pyarbtools.
"""

class WfmBuilderError(Exception):
    """Waveform Builder Exception class"""


class GranularityError(Exception):
    """Waveform Granularity Exception class"""


class AWGError(Exception):
    """AWG Exception class"""


class VSGError(Exception):
    """Signal Generator Exception class"""


class BinblockError(Exception):
    """Binary Block Exception class"""
    pass


class SockInstError(Exception):
    """Socket Instrument Exception class"""
    pass
