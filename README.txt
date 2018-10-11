The purpose of this library is to provide implementation of an Abstract Data Type, named Collection, which I have found very handy while solving many coding problems.

Collection:
========== 
Generically speaking, a Collection is a set of items. 
It is an abstract data type to store information which has no relative fixed order.
Although items are unordered in Collection, duplicate entries are possible.
A collection is expected to support the following basic functionality:
A> Add an item
B> Remove an item
C> Find an item

Additionally it can support the functionality which can answer the following questions:
1> If the collection is empty?
2> What is the total number of items in collection?
3> How many times a particular item present in collection?
4> Which item/s occur/s the most?
5> Which item/s occur/s the least?

Current Implementation:
======================
With the current implementation items can not be list or any other mutable objects. Try converting into something hashable before storing it as an item in the collection.
In general items can be of any type. Based on the feedback and usecases, it might be supported in later versions. Same is true for additional functionality.

Details about current implementation:
Method				Asymptotic Complexity		Details
======				=====================		=======
is_collection_empty()		O(1)				Returns True if no item is present in the collection; False otherwise.
total_items()			O(1)				Returns total cumulative occurrances of all the items present in the collection
is_present(item)		O(1)				Returns True if the item is present in the collection; False otherwise.
frequency(item)			O(1)				Returns the number of time the item is present in the collection.
add(item)			O(1)				Adds the item in the collection
remove(item)			O(1)				Removes the item from the collection, if present. Does nothing if item is absent.
most_frequent()			O(n)				Returns the list of the most occurring items and their (common) frequency
least_frequent()		O(n)				Returns the list of the least occurring items and their (common) frequency
pretty_print()			O(n)				Prints the collection in human readable form by clubing duplicates together
print(c)			O(n)				Prints items in the collection 