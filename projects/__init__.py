class work:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        self.left += other.left
        self.right += other.right
        return work(self.left, self.right)

    def __sub__(self, other):
        self.left -= other.left
        self.right -= other.right
        return work(self.left, self.right)

    def __mul__(self, other):
        self.left *= other.left
        self.right *= other.right
        return work(self.left, self.right)

    def __repr__(self):
        return f'({self.left}i, {abs(self.right)}j)'

c1 = work(5,7)
c2 = work(2,-9)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
