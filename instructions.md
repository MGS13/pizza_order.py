#  Romino's Pizza

Romino's Pizza are a legally distinct rip-off of a more popular brand and they are setting up shop in your town! You have been asked to build a system that takes orders of pizzas and customer information ready for delivery, calculating the cost based on expected inputs. You will need to remember that the end user of this system will not be a computer expert so the user interface needs to be appropriate for their needs despite it being command line.

You will be expected to include a menu, validation and output the results of your calculations. You should ensure to use subroutines throughout.

---

## Your Task
Please make sure you read *the entire* task before you start, there are some thing that you'll need to think about that aren't discussed until the end. It's much easier to plan ahead than the go back and change the code later!

### Create the Menu

1. Build a menu that uses good UX practices to contain the following options
	* Create a new order
	* Exit the program

### Data Input and Validation

2. Create a new order that:
	* Allows multiple pizzas to be ordered
	* Takes in relevant information about the pizza order and uses at least three kinds of validation
	* Calculates the subtotal, and shows the ongoing total of the entire order
	* Allows you to exit the new order subroutine

### Calculate the Price

The pizza selected is mainly based on size and the base used, take a look at the table below which shows how the prices are calculated


|         | Small | Medium | Large |
|---------|:-----:|:------:|:-----:|
| Thin    |  4.99 |  7.99  | 10.99 |
| Italian |  5.49 |  8.99  | 12.49 |
| Pan     |  5.99 |  9.99  | 13.99 |


There is also a charge for delivery or collection, and if you need to pizza as a rush order or done in a standard timescale.


|            | Rush | Standard |
|------------|:----:|:--------:|
| Delivery   | 3.99 |   0.99   |
| Collection | 1.99 |     0    |


So, if we wanted to order a Large Pan Pizza on a Rush collection we would calculate the cost like this `13.99 + 1.99 = 15.98`

If the customer orders more than three pizzas **overall** then there is a 33% discount to be applied to the overall cost of the order.

3. Build the algorithm that calculates the cost of the pizzas and include it in the previous algorithm
