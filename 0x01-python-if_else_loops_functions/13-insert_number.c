#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a head to be checked
 * @number: a number to be inserted
 * Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *inode = *head, *nNode = malloc(sizeof(listint_t));

	if (!nNode)
	{
		return (NULL);
	}

	nNode->n = number;
	nNode->next = NULL;

	if (!inode || nNode->n < inode->n)
	{
		nNode->next = inode;
		return (*head = nNode);
	}

	while (inode)
	{
		if (!inode->next || nNode->n < inode->next->n)
		{
			nNode->next = inode->next;
			inode->next = nNode;
			return (inode);
		}

		inode = inode->next;
	}

	return (NULL);
}
