import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["char", "freq"])):
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}

    # Построение дерева Хаффмана
    def build_tree(self):
        # Подсчет частоты символов
        freq = Counter(self.text)
        priority_queue = [HuffmanNode(char, freq) for char, freq in freq.items()]
        heapq.heapify(priority_queue)

        # Построение дерева
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = HuffmanNode(None, left.freq + right.freq, left, right)
            heapq.heappush(priority_queue, merged)

        self.root = priority_queue[0] if priority_queue else None
        self._generate_codes(self.root, "")

    # Генерация кодов символов
    def _generate_codes(self, node, current_code):
        if node:
            if node.char is not None:
                self.codes[node.char] = current_code
            self._generate_codes(node.left, current_code + "0")
            self._generate_codes(node.right, current_code + "1")

    # Обход дерева (прямой обход)
    def preorder(self, node, level=0):
        if node:
            print(" " * (level * 4) + (f"'{node.char}'({node.freq})" if node.char else f"Node({node.freq})"))
            self.preorder(node.left, level + 1)
            self.preorder(node.right, level + 1)

    # Визуализация структуры дерева
    def display(self):
        print("Кодовое дерево Хаффмана:")
        self.preorder(self.root)

    # Кодирование текста
    def encode(self):
        if not self.codes:
            self.build_tree()
        return "".join(self.codes[char] for char in self.text)

    # Декодирование текста
    def decode(self, encoded_text):
        decoded = []
        node = self.root
        for bit in encoded_text:
            node = node.left if bit == "0" else node.right
            if node.char:
                decoded.append(node.char)
                node = self.root
        return "".join(decoded)

# Пример использования
if __name__ == "__main__":
    text = input("Введите текст для кодирования: ")

    tree = HuffmanTree(text)
    tree.build_tree()

    print("\nВизуализация дерева:")
    tree.display()

    encoded = tree.encode()
    print(f"\nЗакодированный текст: {encoded}")

    decoded = tree.decode(encoded)
    print(f"Декодированный текст: {decoded}")
