"""
Binary Tree Implementation with YAML Support - ALL IN ONE FILE

This is a complete, standalone implementation.
No folder structure needed - just run this file!

Educational comments included throughout.
"""

from typing import Optional, Any, Dict
import yaml


# ============================================================================
# NODE CLASS
# ============================================================================

class Node:
    """
    A node that can be used for both binary trees and general trees.
    
    For binary tree: Use only left and right
    For general tree: Use children list
    
    Attributes:
        value: The data stored in this node
        left: Left child (for binary tree compatibility)
        right: Right child (for binary tree compatibility)
        children: List of all children (for general tree)
    
    Example:
        # Binary tree usage
        >>> node = Node(10)
        >>> node.left = Node(5)
        >>> node.right = Node(15)
        
        # General tree usage
        >>> node = Node(10)
        >>> node.add_child(Node(5))
        >>> node.add_child(Node(15))
        >>> node.add_child(Node(20))  # Can have more than 2 children!
    """
    
    def __init__(self, value: Any) -> None:
        """
        Initialize a tree node that works for both binary and general trees.
        
        Args:
            value: The value to store in this node
        """
        self.value: Any = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.children: List['Node'] = []  # For general tree support
    
    def add_child(self, child: 'Node') -> None:
        """
        Add a child to this node (for general tree).
        
        Also maintains binary tree compatibility by setting left/right
        for the first two children.
        """
        self.children.append(child)
        # Maintain binary tree compatibility
        if len(self.children) == 1:
            self.left = child
        elif len(self.children) == 2:
            self.right = child
    
    def __repr__(self) -> str:
        return f"Node({self.value})"

# ============================================================================
# TREE CREATION AND MANIPULATION FUNCTIONS
# ============================================================================

def create_tree(value: Any) -> Node:
    """
    Create a new binary tree with a single root node.
    
    Args:
        value: The value for the root node
    
    Returns:
        A new Node instance
    
    Example:
        >>> root = create_tree(10)
        >>> root.value
        10
    """
    return Node(value)


def add_node_by_path(root: Optional[Node], path: str, value: Any, 
                     is_general: bool = False) -> Optional[Node]:
    """
    Add a node at a specific path - works for BOTH binary and general trees.
    
    For Binary Tree:
        Path uses 'L' and 'R': "L", "R", "LL", "LR", "RL", "RR"
        
    For General Tree:
        Path uses indices: "0", "1", "2", "0-1", "2-0-1"
        Use is_general=True
    
    Args:
        root: The root node of the tree
        path: Direction string
        value: The value for the new node
        is_general: True for general tree, False for binary tree
    
    Returns:
        The root node
    
    Examples:
        # Binary tree
        >>> root = Node(10)
        >>> add_node_by_path(root, "L", 5)
        >>> add_node_by_path(root, "R", 15)
        
        # General tree
        >>> root = Node(10)
        >>> add_node_by_path(root, "0", 5, is_general=True)
        >>> add_node_by_path(root, "1", 15, is_general=True)
        >>> add_node_by_path(root, "2", 20, is_general=True)  # 3 children!
    """
    if root is None:
        raise ValueError("Cannot add node to None root")
    
    if not path:
        raise ValueError("Path cannot be empty")
    
    if is_general:
        # General tree mode - use numeric indices
        indices = path.split('-')
        current = root
        
        # Navigate to parent
        for idx_str in indices[:-1]:
            try:
                idx = int(idx_str)
            except ValueError:
                raise ValueError(f"Invalid path index: {idx_str}")
            
            if idx >= len(current.children):
                raise ValueError(f"Child at index {idx} does not exist")
            current = current.children[idx]
        
        # Add new child
        try:
            final_idx = int(indices[-1])
        except ValueError:
            raise ValueError(f"Invalid path index: {indices[-1]}")
        
        new_node = Node(value)
        if final_idx == len(current.children):
            current.add_child(new_node)
        else:
            raise ValueError(f"Index {final_idx} out of range. Use {len(current.children)}")
    
    else:
        # Binary tree mode - use L/R
        current = root
        
        # Navigate to parent
        for direction in path[:-1]:
            if direction.upper() == 'L':
                if current.left is None:
                    raise ValueError(f"Cannot follow path '{path}': left child does not exist")
                current = current.left
            elif direction.upper() == 'R':
                if current.right is None:
                    raise ValueError(f"Cannot follow path '{path}': right child does not exist")
                current = current.right
            else:
                raise ValueError(f"Invalid direction '{direction}'. Use 'L' or 'R'.")
        
        # Add at final position
        last_direction = path[-1].upper()
        if last_direction == 'L':
            if current.left is not None:
                raise ValueError(f"Node already exists at path '{path}'")
            current.left = Node(value)
            current.children.append(current.left)  # Keep children list updated
        elif last_direction == 'R':
            if current.right is not None:
                raise ValueError(f"Node already exists at path '{path}'")
            current.right = Node(value)
            if len(current.children) == 0:
                current.children.append(None)  # Placeholder for left
            current.children.append(current.right)
        else:
            raise ValueError(f"Invalid direction '{last_direction}'. Use 'L' or 'R'.")
    
    return root

def print_tree(root: Optional[Node], prefix: str = "Root:", 
               is_general: bool = False) -> None:
    """
    Print the tree - works for BOTH binary and general trees.
    
    Automatically detects if tree has more than 2 children per node.
    
    Args:
        root: The root node to start printing from
        prefix: Text to display before the node value
        is_general: Force general tree display (auto-detected if not set)
    
    Example:
        >>> root = Node(10)
        >>> root.add_child(Node(5))
        >>> root.add_child(Node(15))
        >>> print_tree(root)  # Auto-detects and uses appropriate format
    """
    if root is None:
        return
    
    print(f"{prefix}{root.value}")
    
    # Auto-detect if this is a general tree (more than 2 children)
    if not is_general and len(root.children) > 2:
        is_general = True
    
    if is_general or len(root.children) > 2:
        # General tree display
        for i, child in enumerate(root.children):
            is_last_child = (i == len(root.children) - 1)
            
            if prefix == "Root:":
                child_prefix = " "
            else:
                child_prefix = prefix.replace("├──", "│  ").replace("└──", "   ")
            
            if is_last_child:
                print_tree(child, child_prefix + "└──", is_general)
            else:
                print_tree(child, child_prefix + "├──", is_general)
    else:
        # Binary tree display
        if prefix == "Root:":
            child_prefix = " "
        else:
            child_prefix = prefix.replace("L---", " ").replace("R---", " ") + " "
        
        if root.left is not None:
            print_tree(root.left, child_prefix + "L---", False)
        
        if root.right is not None:
            print_tree(root.right, child_prefix + "R---", False)

def find_node(root: Optional[Node], value: Any) -> Optional[Node]:
    """
    Find a node - works for BOTH binary and general trees.
    
    Uses breadth-first search to find the node.
    
    Args:
        root: The root node of the tree
        value: The value to search for
    
    Returns:
        The node with the specified value, or None if not found
    
    Works with both binary and general trees automatically.
    """
    if root is None:
        return None
    
    from collections import deque
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        if current.value == value:
            return current
        
        # Works for both: binary tree uses left/right, general tree uses children
        if len(current.children) > 0:
            queue.extend(current.children)
        else:
            # Fallback to binary tree mode
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return None

def edit_node(root: Optional[Node], old_value: Any, new_value: Any) -> bool:
    """
    Edit a node's value - works for BOTH binary and general trees.
    
    Args:
        root: The root node of the tree
        old_value: The current value to search for
        new_value: The new value to set
    
    Returns:
        True if the node was found and edited, False otherwise
    
    Example:
        >>> root = Node(10)
        >>> root.add_child(Node(5))
        >>> edit_node(root, 5, 7)
        True
    """
    node = find_node(root, old_value)
    if node is not None:
        node.value = new_value
        return True
    return False

def delete_node(root: Optional[Node], value: Any) -> Optional[Node]:
    """
    Delete a node - works for BOTH binary and general trees.
    
    For binary trees: Replaces with deepest rightmost node
    For general trees: Removes the node and its subtree
    
    Args:
        root: The root node of the tree
        value: The value of the node to delete
    
    Returns:
        The root of the tree after deletion, or None if tree becomes empty
    """
    if root is None:
        return None
    
    # If deleting root
    if root.value == value:
        return None
    
    from collections import deque
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        # Check children
        for i, child in enumerate(current.children):
            if child.value == value:
                current.children.pop(i)
                # Update binary tree pointers
                if i == 0 and len(current.children) >= 1:
                    current.left = current.children[0]
                elif i == 0:
                    current.left = None
                if i <= 1 and len(current.children) >= 2:
                    current.right = current.children[1]
                elif i == 1:
                    current.right = None
                return root
            queue.append(child)
        
        # Fallback for binary tree without children list
        if len(current.children) == 0:
            if current.left and current.left.value == value:
                current.left = None
                return root
            if current.right and current.right.value == value:
                current.right = None
                return root
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return root

def delete_tree(root: Optional[Node]) -> None:
    """
    Delete entire tree - works for BOTH binary and general trees.
    
    Args:
        root: The root node of the tree to delete
    """
    if root is None:
        return
    
    # Delete all children
    for child in root.children:
        delete_tree(child)
    
    # Clear references
    root.children.clear()
    root.left = None
    root.right = None

def print_tree_range(root: Optional[Node], min_depth: int = 0, 
                     max_depth: int = 999) -> None:
    """
    Print a specific depth range of the binary tree.
    
    Args:
        root: The root node of the tree
        min_depth: The minimum depth to start printing (0-indexed)
        max_depth: The maximum depth to print (inclusive)
    
    Example:
        >>> root = Node(10)
        >>> root.left = Node(5)
        >>> root.right = Node(15)
        >>> print_tree_range(root, 0, 1)
    """
    def _print_helper(node: Optional[Node], current_depth: int, 
                     prefix: str) -> None:
        if node is None or current_depth > max_depth:
            return
        
        if current_depth >= min_depth:
            print(f"{prefix}{node.value}")
        
        if current_depth < max_depth:
            # Prepare prefix for children
            if prefix == "Root:":
                child_prefix = " "
            else:
                child_prefix = prefix.replace("L---", " ").replace("R---", " ") + " "
            
            if node.left:
                _print_helper(node.left, current_depth + 1, 
                            child_prefix + "L---" if current_depth + 1 >= min_depth else "")
            if node.right:
                _print_helper(node.right, current_depth + 1,
                            child_prefix + "R---" if current_depth + 1 >= min_depth else "")
    
    _print_helper(root, 0, "Root:")

# ============================================================================
# BONUS FEATURE: GENERAL TREE (N-ARY TREE) SUPPORT
# ============================================================================

class GeneralNode:
    """
    A node for a general tree (n-ary tree) that can have any number of children.
    
    Attributes:
        value: The data stored in this node
        children: List of child nodes
    
    Example:
        >>> node = GeneralNode(10)
        >>> node.add_child(GeneralNode(5))
        >>> node.add_child(GeneralNode(15))
        >>> node.add_child(GeneralNode(20))
    """
    
    def __init__(self, value: Any) -> None:
        """
        Initialize a general tree node.
        
        Args:
            value: The value to store in this node
        """
        self.value: Any = value
        self.children: List['GeneralNode'] = []
    
    def add_child(self, child: 'GeneralNode') -> None:
        """Add a child node to this node."""
        self.children.append(child)
    
    def __repr__(self) -> str:
        return f"GeneralNode({self.value})"


def create_general_tree(value: Any) -> GeneralNode:
    """
    Create a new general tree with a single root node.
    
    Args:
        value: The value for the root node
    
    Returns:
        A new GeneralNode instance
    
    Example:
        >>> root = create_general_tree(10)
    """
    return GeneralNode(value)


def add_general_node_by_path(root: Optional[GeneralNode], path: str, 
                             value: Any) -> Optional[GeneralNode]:
    """
    Add a node to a general tree using a path.
    
    Path format: "0", "1", "2" for children at index 0, 1, 2
    Can chain: "0-1" means first child's second child
    
    Args:
        root: The root node of the general tree
        path: String like "0", "1", "0-1", "2-0-1" etc.
        value: The value for the new node
    
    Returns:
        The root node
    
    Example:
        >>> root = GeneralNode(10)
        >>> root.add_child(GeneralNode(5))
        >>> add_general_node_by_path(root, "0-0", 3)  # Add to first child
    """
    if root is None:
        raise ValueError("Cannot add node to None root")
    
    if not path:
        raise ValueError("Path cannot be empty")
    
    # Split path by delimiter
    indices = path.split('-')
    current = root
    
    # Navigate to parent
    for idx_str in indices[:-1]:
        try:
            idx = int(idx_str)
        except ValueError:
            raise ValueError(f"Invalid path index: {idx_str}")
        
        if idx >= len(current.children):
            raise ValueError(f"Child at index {idx} does not exist")
        current = current.children[idx]
    
    # Add new child at final position
    try:
        final_idx = int(indices[-1])
    except ValueError:
        raise ValueError(f"Invalid path index: {indices[-1]}")
    
    # Add the new child at the specified index
    new_node = GeneralNode(value)
    if final_idx == len(current.children):
        current.children.append(new_node)
    elif final_idx < len(current.children):
        current.children.insert(final_idx, new_node)
    else:
        raise ValueError(f"Index {final_idx} out of range")
    
    return root


def print_general_tree(root: Optional[GeneralNode], prefix: str = "Root:", 
                       is_last: bool = True) -> None:
    """
    Print a general tree in a visual hierarchical format.
    
    Args:
        root: The root node of the general tree
        prefix: Text prefix (used for recursion)
        is_last: Whether this is the last child (used for recursion)
    
    Example output:
        Root:10
         ├──5
         │  └──3
         ├──15
         └──20
    """
    if root is None:
        return
    
    print(f"{prefix}{root.value}")
    
    # Print all children
    for i, child in enumerate(root.children):
        is_last_child = (i == len(root.children) - 1)
        
        if prefix == "Root:":
            child_prefix = " "
        else:
            child_prefix = prefix.replace("├──", "│  ").replace("└──", "   ")
        
        if is_last_child:
            print_general_tree(child, child_prefix + "└──", True)
        else:
            print_general_tree(child, child_prefix + "├──", False)


def find_general_node(root: Optional[GeneralNode], value: Any) -> Optional[GeneralNode]:
    """
    Find a node in a general tree.
    
    Args:
        root: The root of the general tree
        value: The value to search for
    
    Returns:
        The node if found, None otherwise
    """
    if root is None:
        return None
    
    if root.value == value:
        return root
    
    for child in root.children:
        result = find_general_node(child, value)
        if result:
            return result
    
    return None


def edit_general_node(root: Optional[GeneralNode], old_value: Any, 
                     new_value: Any) -> bool:
    """
    Edit a node's value in a general tree.
    
    Args:
        root: The root of the general tree
        old_value: Value to find
        new_value: New value to set
    
    Returns:
        True if node was found and edited, False otherwise
    """
    node = find_general_node(root, old_value)
    if node is not None:
        node.value = new_value
        return True
    return False


def delete_general_node(root: Optional[GeneralNode], value: Any) -> Optional[GeneralNode]:
    """
    Delete a node from a general tree.
    
    If the node has children, they are removed too.
    
    Args:
        root: The root of the general tree
        value: The value of the node to delete
    
    Returns:
        The root after deletion, or None if root was deleted
    """
    if root is None:
        return None
    
    if root.value == value:
        return None  # Deleting root
    
    # Search in children
    for i, child in enumerate(root.children):
        if child.value == value:
            root.children.pop(i)
            return root
        
        # Recursively search in child's subtree
        delete_general_node(child, value)
    
    return root


def delete_general_tree(root: Optional[GeneralNode]) -> None:
    """
    Delete an entire general tree.
    
    Args:
        root: The root of the tree to delete
    """
    if root is None:
        return
    
    for child in root.children:
        delete_general_tree(child)
    
    root.children.clear()

# ============================================================================
# YAML INTEGRATION FUNCTIONS
# ============================================================================

def build_tree_from_yaml(file_path: str) -> Optional[Node]:
    """
    Build a binary tree from a YAML file.
    
    EDUCATIONAL EXPLANATION:
    ========================
    
    YAML (YAML Ain't Markup Language) is a human-readable data format.
    It represents hierarchical data using indentation (like Python).
    
    Example YAML structure for a tree:
    
    value: 10
    left:
      value: 5
      left:
        value: 3
      right:
        value: 7
    right:
      value: 15
    
    How this function works:
    1. Read the YAML file into a Python dictionary
    2. Pass the dictionary to a helper function that builds the tree recursively
    3. Return the root node
    
    Args:
        file_path: Path to the YAML file
    
    Returns:
        The root node of the constructed tree, or None if file is empty
    
    Raises:
        FileNotFoundError: If the YAML file doesn't exist
        yaml.YAMLError: If the YAML file is malformed
    
    Example:
        >>> root = build_tree_from_yaml("tree.yaml")
        >>> print_tree(root)
    """
    try:
        # Step 1: Open and read the YAML file
        with open(file_path, 'r') as file:
            # yaml.safe_load() converts YAML text into a Python dictionary
            # safe_load is safer than load() as it only constructs simple Python objects
            tree_data = yaml.safe_load(file)
        
        # Step 2: Build the tree from the dictionary
        # We call the recursive helper function
        return _dict_to_tree(tree_data)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found: {file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {file_path}: {e}")


def _dict_to_tree(tree_dict: Optional[Dict[str, Any]]) -> Optional[Node]:
    """
    RECURSIVE helper function to convert a dictionary to a tree.
    
    EDUCATIONAL EXPLANATION OF RECURSION:
    =====================================
    
    Recursion is when a function calls itself to solve smaller versions
    of the same problem. For trees, this is perfect because:
    - A tree is made of a root node and two subtrees (left and right)
    - Each subtree is itself a tree!
    
    How this recursion works:
    
    1. BASE CASE: If tree_dict is None or invalid, return None
       (This stops the recursion)
    
    2. RECURSIVE CASE:
       a. Create a node with the 'value' from the dictionary
       b. If there's a 'left' key, RECURSIVELY build the left subtree
       c. If there's a 'right' key, RECURSIVELY build the right subtree
       d. Return the node
    
    Example walkthrough:
    
    Input dictionary:
    {
        'value': 10,
        'left': {'value': 5, 'left': {'value': 3}},
        'right': {'value': 15}
    }
    
    Step 1: Create node with value 10
    Step 2: See 'left' key exists, so RECURSE:
            - Create node with value 5
            - See 'left' key exists, so RECURSE again:
                * Create node with value 3
                * No 'left' or 'right' keys, return this node
            - Attach the node(3) as left child of node(5)
            - No 'right' key, so right child stays None
            - Return node(5)
    Step 3: Attach node(5) as left child of node(10)
    Step 4: See 'right' key exists, so RECURSE:
            - Create node with value 15
            - No 'left' or 'right' keys, return this node
    Step 5: Attach node(15) as right child of node(10)
    Step 6: Return node(10) - the complete tree!
    
    Args:
        tree_dict: Dictionary representing a tree or subtree
    
    Returns:
        Root node of the tree/subtree, or None
    """
    # BASE CASE: If dictionary is None or empty, return None
    if tree_dict is None:
        return None
    
    # Validate that the dictionary has the required 'value' key
    if not isinstance(tree_dict, dict) or 'value' not in tree_dict:
        return None
    
    # STEP 1: Create the root node with the value from the dictionary
    root = Node(tree_dict['value'])
    
    # STEP 2: RECURSIVELY build the left subtree
    # If 'left' key exists in the dictionary, it contains another tree/subtree
    if 'left' in tree_dict:
        # RECURSION HAPPENS HERE!
        # We call _dict_to_tree on the left subtree dictionary
        # This will create the entire left subtree and return its root
        root.left = _dict_to_tree(tree_dict['left'])
    
    # STEP 3: RECURSIVELY build the right subtree
    # Same logic as above, but for the right child
    if 'right' in tree_dict:
        # RECURSION HAPPENS HERE!
        # We call _dict_to_tree on the right subtree dictionary
        # This will create the entire right subtree and return its root
        root.right = _dict_to_tree(tree_dict['right'])
    
    # STEP 4: Return the root node with its children attached
    return root


def tree_to_yaml(root: Optional[Node], file_path: str) -> None:
    """
    Export a binary tree to a YAML file.
    
    EDUCATIONAL EXPLANATION:
    ========================
    
    This function does the opposite of build_tree_from_yaml():
    1. Convert the tree to a dictionary (using recursion)
    2. Write the dictionary to a YAML file
    
    Args:
        root: The root node of the tree to export
        file_path: Path where the YAML file should be saved
    
    Example:
        >>> root = Node(10)
        >>> root.left = Node(5)
        >>> root.right = Node(15)
        >>> tree_to_yaml(root, "output.yaml")
        # Creates output.yaml with the tree structure
    """
    # Step 1: Convert the tree to a dictionary using recursion
    tree_dict = _tree_to_dict(root)
    
    # Step 2: Write the dictionary to a YAML file
    with open(file_path, 'w') as file:
        # yaml.dump() converts a Python dictionary to YAML format
        # default_flow_style=False makes it use block style (more readable)
        # sort_keys=False preserves the order of keys
        yaml.dump(tree_dict, file, default_flow_style=False, sort_keys=False)


def _tree_to_dict(root: Optional[Node]) -> Optional[Dict[str, Any]]:
    """
    RECURSIVE helper function to convert a tree to a dictionary.
    
    EDUCATIONAL EXPLANATION OF RECURSION:
    =====================================
    
    This is the reverse of _dict_to_tree(). We traverse the tree
    and build a dictionary representation.
    
    How this recursion works:
    
    1. BASE CASE: If root is None, return None
    
    2. RECURSIVE CASE:
       a. Create a dictionary with 'value' key
       b. If left child exists, RECURSIVELY convert it and add to dict
       c. If right child exists, RECURSIVELY convert it and add to dict
       d. Return the dictionary
    
    Example walkthrough:
    
    Input tree:
         10
        /  \
       5    15
      /
     3
    
    Step 1: At node(10), create dict {'value': 10}
    Step 2: Left child exists (node 5), so RECURSE:
            - At node(5), create dict {'value': 5}
            - Left child exists (node 3), so RECURSE:
                * At node(3), create dict {'value': 3}
                * No children, return {'value': 3}
            - Add left child dict: {'value': 5, 'left': {'value': 3}}
            - No right child, return this dict
    Step 3: Add left subtree to main dict:
            {'value': 10, 'left': {'value': 5, 'left': {'value': 3}}}
    Step 4: Right child exists (node 15), so RECURSE:
            - At node(15), create dict {'value': 15}
            - No children, return {'value': 15}
    Step 5: Add right child: 
            {'value': 10, 
             'left': {'value': 5, 'left': {'value': 3}},
             'right': {'value': 15}}
    Step 6: Return complete dictionary
    
    Args:
        root: The root node of the tree/subtree
    
    Returns:
        Dictionary representation of the tree, or None
    """
    # BASE CASE: If node is None, return None
    if root is None:
        return None
    
    # STEP 1: Create dictionary with the node's value
    tree_dict: Dict[str, Any] = {'value': root.value}
    
    # STEP 2: RECURSIVELY convert left subtree
    if root.left is not None:
        # RECURSION HAPPENS HERE!
        # Convert the entire left subtree to a dictionary
        tree_dict['left'] = _tree_to_dict(root.left)
    
    # STEP 3: RECURSIVELY convert right subtree
    if root.right is not None:
        # RECURSION HAPPENS HERE!
        # Convert the entire right subtree to a dictionary
        tree_dict['right'] = _tree_to_dict(root.right)
    
    # STEP 4: Return the complete dictionary
    return tree_dict