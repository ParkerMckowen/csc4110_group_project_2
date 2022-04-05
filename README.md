Bar Master Needs:
=================
	- Track inventory
		- how much drink we have
		- how much drink have we served
		- can we serve a drink with the inventory we have
		- when drink was served
	- Track Sales *Optional*
		- how much money we have earned
		- how much we spend on re-orders
	- Employees
		- who's working
		- how long have they been working
		- how long they have worked
	- Output File
		- json file
		- {ingredients: {"vodka": 400ml, "bourbon": 400ml},
		   employees: {employee1: [employee data]},
		   drinkSales: {transactionid : [drinkname, time of sale, ingredients?, who served it]}
		   }

Questions:
==========
	- Do we need to be able to add to the inventory? Answer: Yes
	- Do we need to track sales? Answer: Yes


Bar Master Features:
====================
	- Employees
		- add a new employee
		- delete existing employee
		- employee clock-in/out
		- employee hours worked storage
		
