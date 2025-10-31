import ctypes


# extract from .so file
lib = ctypes.CDLL('./example.so')

if __name__ == "__main__":
    lib.hello_from_c()
