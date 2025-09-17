
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
        if cls._instance is None:
          inst = super().__new__(cls)
          inst._balance = float(initial_amount)
          cls._instance = inst

        return cls._instance

    def allocate(self, amount: float) -> None:
        if amount is None or amount <= 0:
          raise ValueError("Allocation amount must be positive")
        if amount > self._balance:
          raise ValueError(
            f"Insufficient funds: tried to allocate {amount}, only {self._balance} remaining"
          )
        self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
