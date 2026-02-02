# 🚀 QUICK START GUIDE

## How to Test This Package on Your PC

### Step 1: Download the Package
Download the entire `binarytree_package` folder to your computer.

### Step 2: Install PyYAML
Open your terminal/command prompt and run:
```bash
pip install PyYAML
```

### Step 3: Navigate to the Package
```bash
cd path/to/binarytree_package
```

### Step 4: Run the Test Script
```bash
python main.py
```

That's it! You should see the test output.

---

## What Each File Does

| File | Purpose |
|------|---------|
| `src/binarytree/node.py` | **Main code** - All the tree operations with extensive comments |
| `src/binarytree/__init__.py` | Package initialization |
| `main.py` | **Test script** - Run this to see everything work! |
| `test_data.yaml` | Sample YAML file (from PDF example) |
| `setup.py` | Pip installation config |
| `requirements.txt` | Lists PyYAML dependency |
| `README.md` | Full documentation |
| `output_tree.yaml` | Created when you run `main.py` |

---

## Understanding the YAML Format

### Simple Example:
```yaml
value: 10
left:
  value: 5
right:
  value: 15
```

This creates:
```
    10
   /  \
  5    15
```

### Nested Example (from test_data.yaml):
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

This creates:
```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

**Key Points:**
- Indentation shows hierarchy (like in Python!)
- `value:` is the node's data
- `left:` defines the left subtree
- `right:` defines the right subtree

---

## How the Recursion Works (Simplified)

When loading from YAML:

1. Read the file → Get a nested dictionary
2. Create root node with `value: 10`
3. See `left:` key → **Recursively** build left subtree
4. See `right:` key → **Recursively** build right subtree
5. Return the complete tree

**The magic**: Each subtree is itself a tree, so we call the same function again!

Read `src/binarytree/node.py` for **detailed step-by-step explanations** with examples.

---

## Common Issues

### "ModuleNotFoundError: No module named 'binarytree'"

**Solution**: Run from the package directory, or use:
```bash
PYTHONPATH=src python main.py
```

Or on Windows:
```bash
set PYTHONPATH=src
python main.py
```

### "ModuleNotFoundError: No module named 'yaml'"

**Solution**: Install PyYAML:
```bash
pip install PyYAML
```

### "FileNotFoundError: test_data.yaml"

**Solution**: Make sure you're running from the `binarytree_package` directory where `test_data.yaml` exists.

---

## Next Steps

1. **Read the code**: Open `src/binarytree/node.py` and read the educational comments
2. **Modify test_data.yaml**: Try changing values and running again
3. **Create your own YAML**: Make a new tree structure
4. **Experiment**: Try the examples in the README

---

## Need Help?

- Read `README.md` for detailed documentation
- Check the comments in `node.py` for explanations
- Run `main.py` to see working examples

**Happy Coding! 🎉**
