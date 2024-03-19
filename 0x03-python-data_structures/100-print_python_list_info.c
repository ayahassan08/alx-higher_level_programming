#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python object list
 * Return: Always 0 (Success)
*/

void print_python_list_info(PyObject *p);
{
	int size, allo, x;
	PyObject *objec;

	size = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allo);

	for (x = 0; x < size; x += 1)
	{
		printf("Element %d: ", x);

		objec = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(objec)->tp_name);
	}
}
