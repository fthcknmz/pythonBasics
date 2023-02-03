"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
x = "Hello World"	                            # type of str	
print(x, " (str)")
x = 20	                                        # type of int	
print(x, " (int)")
x = 20.5	                                    # type of float	
print(x, " (float)")
x = 1j	                                        # type of complex	
print(x, " (complex)")
x = ["apple", "banana", "cherry"]	            # type of list	
print(x, " (list)")
x = ("apple", "banana", "cherry")	            # type of tuple	
print(x, " (tuple)")
x = range(6)	                                # type of range	
print(x, " (range)")
x = {"name" : "John", "age" : 36}	            # type of dict	
print(x, " (dict)")
x = {"apple", "banana", "cherry"}	            # type of set	
print(x, " (set)")
x = frozenset({"apple", "banana", "cherry"})	# type of frozenset	
print(x, " (frozenset)")
x = True	                                    # type of bool	
print(x, " (bool)")
x = b"Hello"	                                # type of bytes	
print(x, " (bytes)")
x = bytearray(5)	                            # type of bytearray	
print(x, " (bytearray)")
x = memoryview(bytes(5))                        # type of memoryview
print(x, " (memoryview)")