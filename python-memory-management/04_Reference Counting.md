# Reference Counting

### Reference Counting

1. Reference counting is a memory management technique where each object tracks how many references (or variables) point to it.
2. Implemented in Cpython.
3. **Reference counting** optimizes memory management by automatically freeing memory when an object’s reference count reaches zero.

---

### **How Does it Work**

- Each object (PyObject) has a field for reference count (ob_refcnt).
- When a variable references an object, its reference count increases.
- When a reference to the object is deleted or reassigned, the count decreases.
- If the reference count drops to zero, the object is deallocated.

**Examples:**

- `x` references `20` (ref count = 1).
- `y = x` adds another reference to `20` (ref count = 2).
- `x` now references `25`.
- Ref count for `20` decreases (ref count = 1).
- If no references remain, the object is garbage collected.

**How to Check Reference Count?**

```python
import sys

_variable = 25
print(sys.getrefcount(_variable))
# adds 1 to the count including temp reference.
```

---

### **Deleting a reference**

- when a reference is reassigned, the reference count is decreased.
- `del x`- deletes the reference, not the object.

---

### **Circular References**

- Reference counting cannot handle **circular references.**
- **Cyclic references**: Objects referring to each other create a cycle, preventing their reference counts from reaching zero.
(e.g., two objects referencing each other but no external references).
- Python's **garbage collector** (GC) detects and cleans circular references.