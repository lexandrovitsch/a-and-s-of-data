class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка узла в дерево
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    # Прямой обход (Pre-order)
    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Симметричный обход (In-order)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    # Обратный обход (Post-order)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    # Визуализация структуры дерева
    def display(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                self.display(node.left, level + 1, "L--- ")
                self.display(node.right, level + 1, "R--- ")

    # Проверка сбалансированности
    def is_balanced(self, node):
        def check_height(node):
            if node is None:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return check_height(node) != -1


# Пример использования
if __name__ == "__main__":
    tree = BinarySearchTree()

    # Ввод узлов вручную
    while True:
        try:
            value = int(input("Введите значение узла (или '0' для завершения): "))
            if value == 0:
                break
            tree.insert(value)
        except ValueError:
            print("Введите корректное число.")

    print("\nДерево (визуализация):")
    tree.display(tree.root)

    print("\nПрямой обход (Pre-order):")
    tree.preorder(tree.root)

    print("\n\nСимметричный обход (In-order):")
    tree.inorder(tree.root)

    print("\n\nОбратный обход (Post-order):")
    tree.postorder(tree.root)

    print("\n\nСбалансировано ли дерево?")
    print("Да" if tree.is_balanced(tree.root) else "Нет")
