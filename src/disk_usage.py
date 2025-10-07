
# src/disk_usage.py

def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    # Defensive handling for malformed input
    if node is None:
        return 0

    node_type = node.get("type")

    if node_type == "file":
        # missing size defaults to 0
        return node.get("size", 0)
    elif node_type == "dir":
        # missing children defaults to empty list
        children = node.get("children") or []
        return sum(total_size(child) for child in children)
    else:
        # Unknown types are ignored and contribute 0 size
        return 0


# Example usage / test
if __name__ == "__main__":
    # Example nested directory tree
    tree = {
        "type": "dir",
        "name": "root",
        "children": [
            {"type": "file", "name": "a.txt", "size": 120},
            {"type": "dir", "name": "subdir", "children": [
                {"type": "file", "name": "b.txt", "size": 200},
                {"type": "file", "name": "c.txt", "size": 350},
                {"type": "dir", "name": "innerdir", "children": [
                    {"type": "file", "name": "d.txt", "size": 50}
                ]}
            ]},
        ],
    }

    print("Total size:", total_size(tree))
