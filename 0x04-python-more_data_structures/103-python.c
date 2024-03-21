#include <Python.h>

/**
 * print_python_list - a list to be used to print some basic info about
 * @p: a pointer
 * Return: Always 0 (Success)
*/

void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("[*] Invalid Python list\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
}

/**
 * print_python_bytes - python bytes to be used to print some basic info about
 * @p: a pointer
 * Return: Always 0 (Success)
*/

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Python bytes object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));

	// Print the first 10 bytes (or less if the size is smaller)
	printf("  trying string: ");
	Py_ssize_t size = PyBytes_Size(p);
	for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}
