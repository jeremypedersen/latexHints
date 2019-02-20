#
# A Rangoli Generator
#
# Author: Jeremy Pedersen
# Date: 2019-02-18
# License: "the unlicense" (Google it)
#

# Define letters for use in rangoli
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

# Read in rangoli size
size = int(input("Set size of rangoli: "))

# Calculate maximum linewidth (how much fill do we need per line)
maxWidth = size*2 - 1 + (size - 1)*2

# Generate rangoli
for i in list(range(size-1,0,-1)) + list(range(0,size)):
	left = alphabet[1+i:size]
	left.reverse()
	right = alphabet[0+i:size]

	center = '-'.join(left + right)

	padding = '-'*((maxWidth - len(center))//2)
	
	print(padding+center+padding)
	