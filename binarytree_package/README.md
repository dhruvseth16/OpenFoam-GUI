# Binary Tree Package with YAML Support

A Python package for creating and manipulating binary trees with YAML file integration.

## 📁 Project Structure

```
binarytree_package/
├── src/
│   └── binarytree/
│       ├── __init__.py          # Package initialization
│       └── node.py              # Main implementation with extensive comments
├── tests/
│   └── (test files will go here)
├── setup.py                     # Pip installation configuration
├── requirements.txt             # Package dependencies
├── main.py                      # Test script (run this!)
├── test_data.yaml              # Sample YAML file for testing
└── README.md                    # This file
```

## 🚀 Quick Start - How to Test on Your PC

### Option 1: Run Directly (No Installation)

This is the **easiest way** to test the code:

```bash
# 1. Navigate to the package directory
cd binarytree_package

# 2. Install PyYAML dependency
pip install PyYAML

# 3. Run the test script
python main.py
```

The script will:
- Create binary trees manually
- Add nodes using paths ("L", "R", "LL", etc.)
- Load a tree from `test_data.yaml`
- Save a tree to `output_tree.yaml`

### Option 2: Install as Package

If you want to use it like a real Python package:

```bash
# 1. Navigate to the package directory
cd binarytree_package

# 2. Install in editable mode
pip install -e .

# 3. Now you can import from anywhere
python
>>> from binarytree import Node, build_tree_from_yaml
>>> root = build_tree_from_yaml("test_data.yaml")
```

### Option 3: Use PYTHONPATH (Alternative)

```bash
# Set PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH}:/path/to/binarytree_package/src"

# Or on Windows:
set PYTHONPATH=%PYTHONPATH%;C:\path\to\binarytree_package\src

# Then run
python main.py
```

## 📖 Understanding the Code

The main implementation is in `src/binarytree/node.py` with **extensive educational comments** explaining:

1. **Basic Tree Operations**
   - `Node` class - represents a tree node
   - `create_tree()` - create a new tree
   - `add_node_by_path()` - add nodes using directional paths
   - `print_tree()` - visualize the tree

2. **YAML Integration** (with detailed recursion explanations)
   - `build_tree_from_yaml()` - read YAML file and build tree
   - `tree_to_yaml()` - save tree to YAML file
   - `_dict_to_tree()` - recursive helper (extensively commented)
   - `_tree_to_dict()` - recursive helper (extensively commented)

### Key Concepts Explained in Code Comments:

- **How YAML represents hierarchical data** using indentation
- **How recursion builds nested structures** step-by-step
- **Base cases and recursive cases** in tree algorithms
- **Why recursion is perfect for trees** (a tree is made of subtrees!)

## 📝 YAML File Format

The YAML structure represents tree hierarchy:

```yaml
value: 10           # Root node value
left:               # Left subtree
  value: 5          # Left child value
  left:
    value: 3        # Left-left grandchild
  right:
    value: 7        # Left-right grandchild
right:              # Right subtree
  value: 15         # Right child value
  left:
    value: 12
  right:
    value: 18
```

**This represents the tree:**
```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

## 🔧 Usage Examples

### Example 1: Create Tree Manually

```python
from binarytree import Node, print_tree

# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Print the tree
print_tree(root)
# Output:
# Root:10
#  L---5
#  R---15
```

### Example 2: Add Nodes Using Paths

```python
from binarytree import Node, add_node_by_path, print_tree

root = Node(10)
add_node_by_path(root, "L", 5)    # Left child
add_node_by_path(root, "R", 15)   # Right child
add_node_by_path(root, "LL", 3)   # Left-left grandchild
add_node_by_path(root, "LR", 7)   # Left-right grandchild

print_tree(root)
```

### Example 3: Load Tree from YAML

```python
from binarytree import build_tree_from_yaml, print_tree

# Load from YAML file
root = build_tree_from_yaml("test_data.yaml")

# Display it
print_tree(root)
```

### Example 4: Save Tree to YAML

```python
from binarytree import Node, add_node_by_path, tree_to_yaml

# Create a tree
root = Node(100)
add_node_by_path(root, "L", 50)
add_node_by_path(root, "R", 150)

# Save to YAML file
tree_to_yaml(root, "my_tree.yaml")
```

## 🧪 Testing

Run the provided test script:

```bash
python main.py
```

Expected output:
```
============================================================
BINARY TREE - TEST SCRIPT
============================================================

[TEST 1] Creating a simple binary tree manually:
------------------------------------------------------------
Root:1
 L---2
  L---4
  R---5
 R---3

[TEST 2] Creating tree using add_node_by_path:
------------------------------------------------------------
Initial tree:
Root:10

Adding nodes:

Tree after additions:
Root:10
 L---5
  L---3
  R---7
 R---15
  L---12
  R---18
  
... (more test output)
```

## 📚 Functions Reference

### Core Functions

- **`Node(value)`** - Create a new tree node
- **`create_tree(value)`** - Create a tree with root node
- **`add_node_by_path(root, path, value)`** - Add node at path
- **`print_tree(root)`** - Display tree structure

### YAML Functions

- **`build_tree_from_yaml(file_path)`** - Load tree from YAML
- **`tree_to_yaml(root, file_path)`** - Save tree to YAML

## 🎓 Learning Resources in Code

The `node.py` file includes:

1. **Detailed function docstrings** explaining what each function does
2. **Step-by-step recursion walkthrough** with examples
3. **Visual diagrams in comments** showing tree transformations
4. **Educational explanations** of YAML format and structure
5. **Base case and recursive case explanations**

## 🐛 Troubleshooting

**Error: ModuleNotFoundError: No module named 'binarytree'**
- Make sure you're running from the `binarytree_package` directory
- OR install the package: `pip install -e .`
- OR use: `PYTHONPATH=src python main.py`

**Error: No module named 'yaml'**
- Install PyYAML: `pip install PyYAML`

**Error: FileNotFoundError: test_data.yaml**
- Make sure you're running the script from the directory containing `test_data.yaml`
- OR provide full path: `build_tree_from_yaml("/full/path/to/test_data.yaml")`

## 📦 Requirements

- Python 3.8 or higher
- PyYAML 6.0 or higher

## 🤝 Contributing

This is an educational project. Feel free to:
- Read the extensively commented code
- Modify and experiment
- Add more features
- Create additional test cases

## 📄 License

MIT License - Free to use for educational purposes

## ✨ Key Features

- ✅ Complete binary tree implementation
- ✅ YAML file integration (load and save)
- ✅ Path-based node insertion ("L", "R", "LL", etc.)
- ✅ Extensively commented code for learning
- ✅ Detailed recursion explanations
- ✅ Test script with multiple examples
- ✅ Pip-installable package structure

---

**Happy Learning! 🎓**

Read the code comments in `src/binarytree/node.py` to understand how recursion handles nested YAML structures!
