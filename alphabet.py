from abc import ABC, abstractmethod


class Alphabet(ABC):
    @abstractmethod
    def get_symbol(self, index: int) -> str: ...
    @abstractmethod
    def get_index(self, symbol: str) -> int: ...    
    @abstractmethod
    def get_size(self) -> int: ...


class UnicodeAlphabet(Alphabet):
    def get_symbol(self, index: int) -> str: return chr(index)
    def get_index(self, symbol: str) -> int: return ord(symbol)
    def get_size(self) -> int: return 0x110000


class AsciiAlphabet(Alphabet):
    def get_symbol(self, index: int) -> str:
        assert index < self.get_size()
        return chr(index)
    
    def get_index(self, symbol: str) -> int:
        index = ord(symbol)
        assert index < self.get_size()
        return index
    
    def get_size(self) -> int:
        return 128


class StringAlphabet(Alphabet):
    def __init__(self, symbols: str):
        assert len(set(symbols)) == len(symbols)
        self._symbols: str = symbols
        self._indexes: dict[str, int] = {}
        for index, symbol in enumerate(symbols):
            self._indexes[symbol] = index

    def get_symbol(self, index: int) -> str:
        return self._symbols[index]

    def get_index(self, symbol: str) -> int:
        return self._indexes[symbol]

    def get_size(self) -> int:
        return len(self._symbols)
