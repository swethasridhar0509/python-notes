# Garbage Collection

1. Garbage collection is a memory management technique that frees memory by removing unused objects from the heap.
2. In C/C++, users are responsible for memory management.
3. Python does Automatic memory management.
4. Python lets us interact with the garbage collector via the built-in `gc` module.

**Mechanism**

- **Reference Counting**: Keeps track of the number of references to an object; when it drops to zero, the object is destroyed.
- **Cyclic Garbage Collector**: Detects and collects cyclic references (objects referring to each other) that reference counting cannot handle.

**GC module**

The gc module can be used to:

- Control the garbage collector (`gc.enable()`, `gc.disable()`).
- Force collection (`gc.collect()`).
- Debug memory leaks.

**Cyclic References**

- Occur when objects refer to each other, preventing reference count from dropping to zero.
- Resolved by Python’s garbage collector.

**Weak References**

- `weakref.ref(obj)` creates a reference that doesn’t increase the reference count.
- Prevents cycles while allowing objects to be collected when no strong references remain.