from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def indicator():
        pass

    @abstractmethod
    def signal():
        pass