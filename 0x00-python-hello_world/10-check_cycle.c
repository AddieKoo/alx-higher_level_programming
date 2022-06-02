#include "lists.h"
#include "stdio.h"
/**
 * function that checks if list contains cycle
 * Return 1 if list has cycle
 * Return 0 if it does not
 */
int check_cyc(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;
	if (!list)
		return (0);
	while (slow && fast && fast -> next)
	{
		slow = slow -> next;
		fast = fast -> next -> next;
		if (fast == slow)
			return(1);
	}
	return (0);
}
