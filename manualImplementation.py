def sort_dictionaries_manual(list_of_dicts, key):
  """Manually sorts a list of dictionaries by a specific key.

  Args:
    list_of_dicts: The list of dictionaries to sort.
    key: The key to sort by.

  Returns:
    A new list of dictionaries sorted by the specified key.
  """
  # Implement manual sorting logic here
  sorted_list = list_of_dicts[:] # Create a copy to avoid modifying the original list
  n = len(sorted_list)
  for i in range(n):
    for j in range(0, n - i - 1):
      if sorted_list[j][key] > sorted_list[j + 1][key]:
        sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
  return sorted_list

# Example usage:
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data = sort_dictionaries_manual(data, 'age')
print("Manually sorted data:")
print(sorted_data)