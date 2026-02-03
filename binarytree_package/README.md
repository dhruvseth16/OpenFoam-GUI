# Binary Tree Package with YAML Integration

A Python package implementing binary tree and general tree (n-ary tree) data structures with YAML file support. This package can be installed via pip and provides comprehensive tree manipulation capabilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [YAML Integration](#yaml-integration)
- [Bonus Feature: General Trees](#bonus-feature-general-trees)
- [Testing](#testing)
- [Project Structure](#project-structure)

---

## Features

### Feature Set 1: Binary Tree Operations
✅ **Node Class** - Binary tree node with value, left, and right children  
✅ **Create Tree** - Initialize a new binary tree  
✅ **Add Node** - Add nodes using directional paths (e.g., "L", "R", "LL", "LR")  
✅ **Delete Node** - Remove a specific node from the tree  
✅ **Delete Tree** - Delete the entire tree structure  
✅ **Print Tree** - Visual hierarchical display of the tree  
✅ **Print Range** - Display specific depth levels of the tree  
✅ **Edit Node** - Modify node values  
✅ **Find Node** - Search for nodes by value  

### Feature Set 2: YAML Integration
✅ **Build from YAML** - Parse YAML files and construct trees  
✅ **Export to YAML** - Serialize trees to YAML format  
✅ **Nested Structure Support** - Handles complex hierarchical YAML data  

### Bonus Feature: General Trees (N-ary Trees)
✅ **Multiple Children** - Support for nodes with any number of children  
✅ **Unified API** - Same functions work for both binary and general trees  
✅ **Auto-detection** - Automatically detects tree type for printing  

---

## Installation

### Method 1: Install from Source (Recommended)

```bash
# Navigate to package directory
cd binarytree_package

# Install the package in editable mode
pip install -e .
```

### Method 2: Install Dependencies Only

```bash
pip install -r requirements.txt
```

**Required Dependencies:**
- Python >= 3.7
- PyYAML >= 6.0

---

## Quick Start to run a custom test script

### 1. Basic Binary Tree Usage

```python
from binarytree import *

# Create a binary tree manually
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Print the tree
print_tree(root)
```

**Output:**
```
Root:10
 L---5
 R---15
```

### 2. Add Nodes Using Paths

```python
from binarytree import *

# Create root
root = Node(10)

# Add nodes using directional paths
# L = left, R = right
add_node_by_path(root, "L", 5)
add_node_by_path(root, "R", 15)
add_node_by_path(root, "LL", 3)    # Left-left child
add_node_by_path(root, "LR", 7)    # Left-right child
add_node_by_path(root, "RL", 12)   # Right-left child
add_node_by_path(root, "RR", 18)   # Right-right child

print_tree(root)
```

**Output:**
```
Root:10
 L---5
  L---3
  R---7
 R---15
  L---12
  R---18
```

### 3. Load Tree from YAML

```python
from binarytree import *

# Load tree from YAML file
root = build_tree_from_yaml("test_data.yaml")

# Display the tree
print_tree(root)
```

### 4. Save Tree to YAML

```python
from binarytree import *

# Create a tree
root = Node(100)
add_node_by_path(root, "L", 50)
add_node_by_path(root, "R", 150)

# Save to YAML file
tree_to_yaml(root, "output.yaml")
```

### 5. Edit and Delete Operations

```python
from binarytree import *

# Create a tree
root = Node(50)
add_node_by_path(root, "L", 30)
add_node_by_path(root, "R", 70)
add_node_by_path(root, "LL", 20)

# Find a node
node = find_node(root, 30)
print(f"Found: {node.value}")  # Output: Found: 30

# Edit a node
edit_node(root, 30, 35)
print(f"After edit: {root.left.value}")  # Output: After edit: 35

# Delete a node
root = delete_node(root, 20)
print_tree(root)
```

### 6. General Tree (Bonus Feature)

```python
from binarytree import *

# Create a general tree with 3+ children
root = Node("CEO")
add_node_by_path(root, "0", "CTO", is_general=True)
add_node_by_path(root, "1", "CFO", is_general=True)
add_node_by_path(root, "2", "COO", is_general=True)  # More than 2 children!

# Add nested children
add_node_by_path(root, "0-0", "Dev Manager", is_general=True)
add_node_by_path(root, "0-1", "QA Manager", is_general=True)

# Print automatically detects general tree format
print_tree(root)
```

**Output:**
```
Root:CEO
 ├──CTO
 │  ├──Dev Manager
 │  └──QA Manager
 ├──CFO
 └──COO
```

---

## API Reference

### Node Class

```python
class Node:
    """
    A node that supports both binary trees and general trees.
    
    Attributes:
        value: Data stored in the node
        left: Left child (binary tree)
        right: Right child (binary tree)
        children: List of all children (general tree)
    """
```

### Core Functions

#### `create_tree(value) -> Node`
Create a new tree with a root node.

**Parameters:**
- `value`: The value for the root node

**Returns:** Node instance

**Example:**
```python
root = create_tree(10)
```

---

#### `add_node_by_path(root, path, value, is_general=False) -> Node`
Add a node at a specific path in the tree.

**Parameters:**
- `root`: Root node of the tree
- `path`: Directional path string
  - Binary tree: "L", "R", "LL", "LR", "RL", "RR", etc.
  - General tree: "0", "1", "2", "0-1", "2-0-1", etc.
- `value`: Value for the new node
- `is_general`: True for general tree, False for binary tree

**Returns:** Root node (for chaining)

**Example:**
```python
add_node_by_path(root, "L", 5)           # Binary tree
add_node_by_path(root, "0", 5, True)     # General tree
```

---

#### `find_node(root, value) -> Node | None`
Find a node with the specified value.

**Parameters:**
- `root`: Root node of the tree
- `value`: Value to search for

**Returns:** Node if found, None otherwise

**Example:**
```python
node = find_node(root, 10)
if node:
    print(f"Found: {node.value}")
```

---

#### `edit_node(root, old_value, new_value) -> bool`
Edit a node's value.

**Parameters:**
- `root`: Root node of the tree
- `old_value`: Current value to find
- `new_value`: New value to set

**Returns:** True if successful, False otherwise

**Example:**
```python
success = edit_node(root, 5, 7)
```

---

#### `delete_node(root, value) -> Node | None`
Delete a node from the tree.

**Parameters:**
- `root`: Root node of the tree
- `value`: Value of the node to delete

**Returns:** Root node after deletion

**Example:**
```python
root = delete_node(root, 5)
```

---

#### `delete_tree(root) -> None`
Delete the entire tree.

**Parameters:**
- `root`: Root node of the tree to delete

**Example:**
```python
delete_tree(root)
```

---

#### `print_tree(root, prefix="Root:", is_general=False) -> None`
Print the tree in visual hierarchical format.

**Parameters:**
- `root`: Root node to print
- `prefix`: Display prefix (default: "Root:")
- `is_general`: Force general tree display (auto-detected)

**Example:**
```python
print_tree(root)
```

---

#### `print_tree_range(root, min_depth=0, max_depth=999) -> None`
Print specific depth levels of the tree.

**Parameters:**
- `root`: Root node
- `min_depth`: Minimum depth to display (0-indexed)
- `max_depth`: Maximum depth to display (inclusive)

**Example:**
```python
print_tree_range(root, 0, 2)  # Print levels 0, 1, and 2
```

---

### YAML Functions

#### `build_tree_from_yaml(file_path) -> Node`
Build a tree from a YAML file.

**Parameters:**
- `file_path`: Path to the YAML file

**Returns:** Root node of the constructed tree

**Raises:**
- `FileNotFoundError`: If file doesn't exist
- `yaml.YAMLError`: If YAML is malformed

**Example:**
```python
root = build_tree_from_yaml("tree.yaml")
```

---

#### `tree_to_yaml(root, file_path) -> None`
Save a tree to a YAML file.

**Parameters:**
- `root`: Root node of the tree
- `file_path`: Path where YAML file will be saved

**Example:**
```python
tree_to_yaml(root, "output.yaml")
```

---

## YAML Integration

### YAML File Format

The package uses a nested dictionary structure to represent tree hierarchy:

```yaml
value: 10
left:
  value: 5
  left:
    value: 3
  right:
    value: 7
right:
  value: 15
  left:
    value: 12
  right:
    value: 18
```

This represents the following tree:

```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

### How YAML Parsing Works

The package uses **recursive parsing** to convert YAML to trees:

1. **Read YAML** → Python dictionary
2. **Create root node** from `value` key
3. **Recursively process** `left` and `right` keys
4. **Build subtrees** using the same logic

See `src/binarytree/node.py` for detailed implementation with extensive comments explaining the recursion.

---

## Bonus Feature: General Trees

The Node class supports **general trees** (n-ary trees) where each node can have any number of children.

### Key Differences

| Aspect | Binary Tree | General Tree |
|--------|-------------|--------------|
| Children per node | Maximum 2 | Unlimited |
| Path format | "L", "R", "LL" | "0", "1", "2", "0-1" |
| Display format | L---, R--- | ├──, └── |
| Function parameter | `is_general=False` | `is_general=True` |

### Example: Organization Chart

```python
# Create CEO node
root = Node("CEO")

# Add C-level executives (3 children)
add_node_by_path(root, "0", "CTO", is_general=True)
add_node_by_path(root, "1", "CFO", is_general=True)
add_node_by_path(root, "2", "COO", is_general=True)

# Add department heads under CTO (index 0)
add_node_by_path(root, "0-0", "Engineering Manager", is_general=True)
add_node_by_path(root, "0-1", "QA Manager", is_general=True)
add_node_by_path(root, "0-2", "DevOps Manager", is_general=True)

# Display
print_tree(root)
```

**Output:**
```
Root:CEO
 ├──CTO
 │  ├──Engineering Manager
 │  ├──QA Manager
 │  └──DevOps Manager
 ├──CFO
 └──COO
```

---

## Testing

The package includes a comprehensive test suite in the `tests/` directory.

### Run All Tests

```bash
# Run test file directly
python tests/test_basic.py

# Or using pytest (if installed)
pytest tests/
```

### Run Demo Script

```bash
python main.py
```

This runs all feature demonstrations including:
- Binary tree creation
- Path-based node addition
- YAML import/export
- Edit and delete operations
- General tree demonstration

### Test Coverage

The test suite (`tests/test_basic.py`) includes:
- ✅ Node creation
- ✅ Add nodes by path
- ✅ Nested node addition
- ✅ Find operations
- ✅ Edit operations
- ✅ Delete operations
- ✅ YAML round-trip (save & load)
- ✅ General tree with 3+ children

---

## Project Structure

```
binarytree_package/
├── src/
│   └── binarytree/
│       ├── __init__.py          # Package exports
│       └── node.py              # Core implementation (extensively commented)
├── tests/
│   ├── __init__.py              # Test package
│   └── test_basic.py            # Test suite
├── main.py                      # Demo script
├── test_data.yaml              # Sample YAML file
├── setup.py                     # Package configuration
├── requirements.txt            # Dependencies
└── README.md                    # This file
```

### Key Files

**`src/binarytree/node.py`** (420+ lines)
- Node class with binary and general tree support
- All tree manipulation functions
- YAML integration with detailed recursion explanations
- Extensive educational comments

**`tests/test_basic.py`** (150+ lines)
- 8 comprehensive test functions
- Covers all Feature Sets 1 & 2
- Includes bonus feature testing

**`main.py`** (100+ lines)
- 6 demonstration tests
- Shows all package capabilities
- Matches PDF sample output format

---

## Requirements

- **Python:** 3.7 or higher
- **PyYAML:** 6.0 or higher

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage Examples from PDF

The package matches the screening task sample output exactly:

### Example 1: Manual Tree Creation
```python
from binarytree import *

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print_tree(root)
```

**Output:**
```
Root:1
 L---2
  L---4
  R---5
 R---3
```

### Example 2: Path-Based Addition
```python
from binarytree import *

root = Node(10)
add_node_by_path(root, "L", 5)
add_node_by_path(root, "R", 15)
add_node_by_path(root, "LL", 3)
add_node_by_path(root, "LR", 7)
add_node_by_path(root, "RL", 12)
add_node_by_path(root, "RR", 18)
print_tree(root)
```

**Output:**
```
Root:10
 L---5
  L---3
  R---7
 R---15
  L---12
  R---18
```

### Example 3: YAML Loading
```python
from binarytree import *

root = build_tree_from_yaml("test_data.yaml")
print_tree(root)
```

**Output:**
```
Root:10
 L---5
  L---3
  R---7
 R---15
  L---12
  R---18
```

---

## Code Quality

- ✅ **Full Type Hinting** - All functions use PEP 484 type hints
- ✅ **Comprehensive Docstrings** - Every function documented with Args, Returns, Examples
- ✅ **Educational Comments** - Detailed explanations of recursion in YAML functions
- ✅ **Error Handling** - Proper exceptions for invalid operations
- ✅ **PEP 8 Compliant** - Follows Python style guidelines

---

## License

MIT License - Free for educational and commercial use.

---

## Author

Created by Dhruv Seth for CFD-FOSSEE OpenFOAM GUI Project Screening Task

---

## Support

For issues or questions:
1. Check the test suite in `tests/test_basic.py` for usage examples
2. Review the extensive comments in `src/binarytree/node.py`
3. Run `python main.py` to see all features in action

---

**✨ Features Summary:**
- ✅ All Feature Set 1 requirements (create, add, delete, print, edit)
- ✅ All Feature Set 2 requirements (YAML import/export)
- ✅ Bonus Feature (general trees with n children)
- ✅ Comprehensive test suite
- ✅ Pip installable package
- ✅ Production-ready code quality
