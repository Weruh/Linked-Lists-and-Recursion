from linked_list import LinkedList

if __name__ == "__main__":
    """
    Build a small roster of employee IDs and demonstrate the recursive
    sum, search, and reverse operations.
    """

    roster = LinkedList()

    # Insert sample IDs using both insertion methods.
    for employee_id in [103, 102, 101]:
        roster.insert_at_front(employee_id)
    for employee_id in [104, 105]:
        roster.insert_at_end(employee_id)

    print("Employee ID roster:")
    roster.display()

    print(f"\nSum of all IDs: {roster.recursive_sum()}")

    print()
    for target in [103, 999]:
        found = roster.recursive_search(target)
        print(f"Search for ID {target}: {'found' if found else 'not found'}")

    roster.recursive_reverse()
    print("\nRoster after in-place reverse:")
    roster.display()
