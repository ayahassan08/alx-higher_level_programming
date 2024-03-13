#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slower = list, *faster = list;

	while (faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;

		if (slower == faster)
		{
			return (1);
		}
	}

	return (0);
}
