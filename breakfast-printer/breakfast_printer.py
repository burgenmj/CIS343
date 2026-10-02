class Node:
    def __str__(self):
        raise NotImplementedError


class Crispiness(Node):
    def __init__(self, more=None):
        self.more = more

    def __str__(self):
        count, node = 1, self.more
        while node is not None:
            count += 1
            node = node.more
        return " ".join(["really"] * count)


class Cooked(Node):
    def __init__(self, style):
        self.style = style  # "scrambled" | "poached" | "fried"

    def __str__(self):
        return self.style


class Protein(Node):
    """Base class for the three protein productions."""


class Bacon(Protein):
    def __init__(self, crispiness):
        self.crispiness = crispiness

    def __str__(self):
        return f"{self.crispiness} crispy bacon"


class Sausage(Protein):
    def __init__(self):
        pass

    def __str__(self):
        return "sausage"


class Eggs(Protein):
    def __init__(self, cooked):
        self.cooked = cooked

    def __str__(self):
        return f"{self.cooked} eggs"


class Bread(Node):
    def __init__(self, kind):
        self.kind = kind  # "toast" | "biscuits" | "English muffin"

    def __str__(self):
        return self.kind


class Breakfast(Node):
    def __init__(self, main, side=None):
        if side is not None and not isinstance(main, Protein):
            raise ValueError("Only a protein can have a breakfast on the side.")
        self.main = main
        self.side = side

    def _mains(self):
        """Walk the side chain and collect each level's main item."""
        mains, node = [], self
        while node is not None:
            mains.append(str(node.main))
            node = node.side
        return mains

    def __str__(self):
        mains = self._mains()
        return " with ".join(mains) + " on the side" * (len(mains) - 1)

    def pretty(self):
        mains = self._mains()
        out = f"({mains[-1]})"
        for main in reversed(mains[:-1]):
            out = f"({main} with {out} on the side)"
        return out


if __name__ == "__main__":
    breakfast = Breakfast(
        main=Bacon(Crispiness(Crispiness())),
        side=Breakfast(
            main=Eggs(Cooked("scrambled")),
            side=Breakfast(Bread("toast")),
        ),
    )
    print(breakfast)
    print(breakfast.pretty())