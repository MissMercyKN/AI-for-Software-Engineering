def sort_dictionaries_pythonic(list_of_dicts, key):
  """Sorts a list of dictionaries by a specific key using Python's built-in sorted function.

  Args:
    list_of_dicts: The list of dictionaries to sort.
    key: The key to sort by.

  Returns:
    A new list of dictionaries sorted by the specified key.
  """
  return sorted(list_of_dicts, key=lambda x: x[key])

# Example usage:
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data_pythonic = sort_dictionaries_pythonic(data, 'age')
print("Pythonic sorted data:")
print(sorted_data_pythonic)