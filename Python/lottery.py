# expected earnings from buying 1 Mega-Millions ticket
# with 1.6 billion jackpot

x = {
	2 : 1/37.0,
	4 : 1/89.0,
	10: 1/693.0+1/606.0,
	200: 1/14547.0,
	500: 1/38792.0,
	10000: 1/931001.0,
	1000000: 1/12607306.0,
	1600000000: 1/302575350
}
sum = 0
for val in x:
	sum+= val * x[val]

print sum


