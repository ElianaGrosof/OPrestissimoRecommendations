# DOCUMENTATION AND TEST LOG
# Oprestissimo Recomendation Project
# May 2019

@author Leah Yassky
@author Eliana Grosof
@author Olivia Vasquez

#This log will serve as a record of our tests, how we interacted with different files, and what our findings are

confidence (connection between class a and class b, how much they occur together)
lift (confidence/support, ties connection with popularity)
support (how popular)

#May1
-- using apyori.py 
python3 test_apyori.py 0.015 cartsf2014.csv >> 
-- higher lift is more interesting - sorted by lift
-- findings for today
	-- there are connections between athletic classes 
	-- support as .02
	-- GOAL1: can we sort by list? going through apyori.py to figure out
-- next steps
	-- understanding the SupportRecord, RelationRecord, OrderedStatistic to be able to sort by lift
	-- can we separate these or funnel them into output in a different way by manipulating the apyori.py doc?
	-- convert it into class names (using dictionary)
	-- make pretty

#May2



	

