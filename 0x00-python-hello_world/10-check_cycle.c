#include "lists.h"
#include "stdio.h"
/**
 * function that checks if list contains cycle
 * Return 1 if list has cycle
 * Return 0 if it does not
 */
int check_cyc(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && (*fast).next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			break;
	}
	if (fast == NULL || (*fast).next == NULL)
		return(0);
	else
		return(1);
}
