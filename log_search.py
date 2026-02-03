import sys

class FileNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __repr__(self):
        return f"<{self.name}>"

def depth_limited_search(node, depth, current_path, log_files):
    """Поиск файлов .log с ограничением глубины."""
    if node is None or depth < 0:
        return
    
    if node.is_file and node.name.endswith('.log'):
        log_files.append(f"{current_path}/{node.name}")
    
    if depth == 0:
        return
    
    # Рекурсивный поиск в дочерних узлах
    for child in node.children:
        depth_limited_search(child, depth - 1, f"{current_path}/{node.name}", log_files)

def iterative_deepening_log_search(root, max_depth=20):
    """Поиск всех файлов .log с итеративным углублением."""
    all_log_files = []
    
    for depth in range(max_depth + 1):
        log_files_on_level = []
        depth_limited_search(root, depth, "", log_files_on_level)

        for log_file in log_files_on_level:
            if log_file not in all_log_files:
                all_log_files.append(log_file)
    
    return all_log_files

def build_synthetic_filesystem():
    """Создание синтетической файловой системы с не менее 10 уровнями."""
    
    # Создаем корневой каталог
    root = FileNode("root", is_file=False)
    
    current = root
    for i in range(1, 12):  # Создаем 11 уровней
        dir_node = FileNode(f"dir{i}", is_file=False)
        current.add_child(dir_node)
        
        for j in range(1, 4):
            if j == 1:
                if i % 3 == 0:
                    current.add_child(FileNode(f"file{i}_{j}.log", is_file=True))
                else:
                    current.add_child(FileNode(f"file{i}_{j}.txt", is_file=True))
            elif j == 2:
                current.add_child(FileNode(f"file{i}_{j}.dat", is_file=True))
            else:
                current.add_child(FileNode(f"file{i}_{j}.tmp", is_file=True))
        
        current = dir_node
    
    current.add_child(FileNode("final1.log", is_file=True))
    current.add_child(FileNode("final2.log", is_file=True))
    current.add_child(FileNode("final3.txt", is_file=True))
    current.add_child(FileNode("final4.dat", is_file=True))
    
    root.add_child(FileNode("root_log.log", is_file=True))
    
    level5_dir = root.children[0]
    for i in range(1, 4):
        level5_dir = level5_dir.children[0]
    level5_dir.add_child(FileNode("level5_log.log", is_file=True))
    
    level8_dir = root.children[0]
    for i in range(1, 7):
        level8_dir = level8_dir.children[0]
    level8_dir.add_child(FileNode("level8_log.log", is_file=True))
    
    return root

root = build_synthetic_filesystem()

print("Поиск всех файлов с расширением .log с использованием алгоритма итеративного углубления")

log_files = iterative_deepening_log_search(root)

print(f"\nНайдено {len(log_files)} файлов с расширением .log:\n")
for i, log_file in enumerate(log_files, 1):
    print(f"{i}. {log_file[1:]}")  # Убираем первый "/" из пути