"""
Basic tests for binary tree package.
"""

from binarytree import *


def test_node_creation():
    """Test creating a node."""
    node = Node(10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None
    print("✓ test_node_creation passed")


def test_add_node_by_path():
    """Test adding nodes using path."""
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    
    assert root.left.value == 5
    assert root.right.value == 15
    print("✓ test_add_node_by_path passed")


def test_add_nested_nodes():
    """Test adding nested nodes."""
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    
    assert root.left.left.value == 3
    assert root.left.right.value == 7
    print("✓ test_add_nested_nodes passed")


def test_find_node():
    """Test finding a node."""
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    
    node = find_node(root, 5)
    assert node is not None
    assert node.value == 5
    
    node = find_node(root, 99)
    assert node is None
    print("✓ test_find_node passed")


def test_edit_node():
    """Test editing a node value."""
    root = Node(10)
    add_node_by_path(root, "L", 5)
    
    success = edit_node(root, 5, 7)
    assert success is True
    assert root.left.value == 7
    
    success = edit_node(root, 99, 100)
    assert success is False
    print("✓ test_edit_node passed")


def test_delete_node():
    """Test deleting a node."""
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    
    root = delete_node(root, 5)
    node = find_node(root, 5)
    assert node is None
    print("✓ test_delete_node passed")


def test_yaml_round_trip():
    """Test saving and loading from YAML."""
    import os
    
    # Create a tree
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    
    # Save to YAML
    test_file = "test_temp.yaml"
    tree_to_yaml(root, test_file)
    
    # Load back
    loaded_root = build_tree_from_yaml(test_file)
    
    assert loaded_root.value == 10
    assert loaded_root.left.value == 5
    assert loaded_root.right.value == 15
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("✓ test_yaml_round_trip passed")


def test_general_tree():
    """Test general tree with 3+ children (BONUS)."""
    root = Node(10)
    add_node_by_path(root, "0", 5, is_general=True)
    add_node_by_path(root, "1", 15, is_general=True)
    add_node_by_path(root, "2", 20, is_general=True)
    
    assert len(root.children) == 3
    assert root.children[0].value == 5
    assert root.children[1].value == 15
    assert root.children[2].value == 20
    print("✓ test_general_tree passed")


if __name__ == "__main__":
    print("Running tests...")
    print("=" * 60)
    
    test_node_creation()
    test_add_node_by_path()
    test_add_nested_nodes()
    test_find_node()
    test_edit_node()
    test_delete_node()
    test_yaml_round_trip()
    test_general_tree()
    
    print("=" * 60)
    print("✅ All tests passed!")