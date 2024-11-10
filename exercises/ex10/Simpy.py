"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730566506"


class Simpy:
    """Docstring for the lint thing."""

    values: list[float]

    def __init__(self, input: list[float]):
        """Docstring for the lint thing."""
        self.values = input

    def __str__(self) -> str:
        """Docstring for the lint thing."""
        return (f"Simpy({self.values})")
    
    def fill(self, input: float, num: int) -> None:
        """Docstring for the lint thing."""
        result: list[float] = []
        for i in range(num):
            result.append(input)
        
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Docstring for the lint thing."""
        assert step != 0.0
        result: list[float] = []
        i: float = start
        while (i < stop):
            result.append(i)
            i += step
        if step < 0:
            while (i > stop):
                result.append(i)
                i += step
        
        self.values = result

    def sum(self) -> float:
        """Docstring for the lint thing."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Docstring for the lint thing."""
        result = Simpy([])
        if type(rhs) == float:
            for val in self.values:
                result.values.append(val + rhs)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Docstring for the lint thing."""
        result = Simpy([])
        if type(rhs) == float:
            for val in self.values:
                result.values.append(val ** rhs)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Docstring for the lint thing."""
        result: list[bool] = []
        if type(rhs) == float:
            for val in self.values:
                if val == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Docstring for the lint thing."""
        result: list[bool] = []
        if type(rhs) == float:
            for val in self.values:
                if val > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Docstring for the lint thing."""
        if type(rhs) == int:
            return self.values[rhs]  
        result = Simpy([])
        for i in range(len(rhs)):
            if rhs[i]:
                result.values.append(self.values[i])
        return result