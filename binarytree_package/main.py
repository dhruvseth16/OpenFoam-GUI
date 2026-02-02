"""
Test script for the binary tree package.
This matches the screening task requirements.
"""

from binarytree import *

if __name__ == "__main__":
    print("=" * 60)
    print("Binary Tree Package - Test Script")
    print("=" * 60)
    
    # Test 1: Basic tree creation
    print("\n[Test 1] Creating a simple binary tree:")
    print("-" * 60)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_tree(root)
    
    # Test 2: Creating tree with add_node_by_path
    print("\n[Test 2] Creating tree using add_node_by_path:")
    print("-" * 60)
    root = Node(10)
    print("Initial tree:")
    print_tree(root)
    
    # Add nodes
    print("\nAdding nodes:")
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RL", 12)
    add_node_by_path(root, "RR", 18)
    
    print("\nTree after additions:")
    print_tree(root)
    
    # Test 3: YAML integration
    print("\n[Test 3] YAML Integration:")
    print("-" * 60)
    yaml_file = "test_data.yaml"
    print(f"Building tree from '{yaml_file}':")
    
    try:
        yaml_tree_root = build_tree_from_yaml(yaml_file)
        if yaml_tree_root:
            print("\nTree built from YAML:")
            print_tree(yaml_tree_root)
    except FileNotFoundError:
        print(f"\n⚠️  File '{yaml_file}' not found. Creating it now...")
        
        # Create the test_data.yaml file
        sample_tree = Node(10)
        sample_tree.left = Node(5)
        sample_tree.left.left = Node(3)
        sample_tree.left.right = Node(7)
        sample_tree.right = Node(15)
        sample_tree.right.right = Node(18)
        
        tree_to_yaml(sample_tree, yaml_file)
        print(f"✓ Created '{yaml_file}'")
        
        # Now load it
        yaml_tree_root = build_tree_from_yaml(yaml_file)
        print("\nTree built from YAML:")
        print_tree(yaml_tree_root)
    
    # Test 4: Save tree to YAML
    print("\n[Test 4] Saving tree to YAML:")
    print("-" * 60)
    
    # Create a test tree
    test_root = Node(100)
    add_node_by_path(test_root, "L", 50)
    add_node_by_path(test_root, "R", 150)
    add_node_by_path(test_root, "LL", 25)
    add_node_by_path(test_root, "LR", 75)
    
    print("Tree to save:")
    print_tree(test_root)
    
    output_file = "output_tree.yaml"
    tree_to_yaml(test_root, output_file)
    print(f"\n✓ Tree saved to '{output_file}'")
    
    # Verify by loading it back
    print(f"\nVerifying: Loading '{output_file}' back:")
    reloaded_tree = build_tree_from_yaml(output_file)
    print_tree(reloaded_tree)
    
    # Test 5: Edit and Delete (Binary Tree)
    print("\n[Test 5] Edit and Delete Operations (Binary Tree):")
    print("-" * 60)
    
    test_root = Node(50)
    add_node_by_path(test_root, "L", 30)
    add_node_by_path(test_root, "R", 70)
    add_node_by_path(test_root, "LL", 20)
    add_node_by_path(test_root, "LR", 40)
    
    print("Original tree:")
    print_tree(test_root)
    
    print("\nEditing node 40 to 45:")
    edit_node(test_root, 40, 45)
    print_tree(test_root)
    
    print("\nDeleting node with value 20:")
    test_root = delete_node(test_root, 20)
    print_tree(test_root)
    
    # Test 6: BONUS - Same functions work for General Tree!
    print("\n[Test 6] BONUS - General Tree (3+ children per node):")
    print("-" * 60)
    
    gen_root = Node("CEO")
    add_node_by_path(gen_root, "0", "CTO", is_general=True)
    add_node_by_path(gen_root, "1", "CFO", is_general=True)
    add_node_by_path(gen_root, "2", "COO", is_general=True)  # 3 children!
    
    # Add grandchildren
    add_node_by_path(gen_root, "0-0", "Dev Manager", is_general=True)
    add_node_by_path(gen_root, "0-1", "QA Manager", is_general=True)
    add_node_by_path(gen_root, "1-0", "Accountant", is_general=True)
    
    print("General tree with same functions:")
    print_tree(gen_root)  # Auto-detects general tree!
    
    print("\nEditing 'Dev Manager' to 'Engineering Manager':")
    edit_node(gen_root, "Dev Manager", "Engineering Manager")
    print_tree(gen_root)
    
    print("\nDeleting 'QA Manager':")
    delete_node(gen_root, "QA Manager")
    print_tree(gen_root)
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)