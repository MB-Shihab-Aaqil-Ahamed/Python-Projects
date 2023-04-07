# Electricity Bill Calculator

This program calculates the monthly electricity bill based on the units consumed.

## Tariff Plan

The charges differ according to the following domestic purpose plan from Ceylon Electricity Board.

If the consumption is between 0-60 kWh per month the following tariffs will be applicable.

| Monthly Consumption (kWh) | Unit Charge (Rs/kWh) | Fixed Charge (Rs/month) |
|---------------------------|----------------------|-------------------------|
| 0-30                      | 2.50                 | 30.00                    |
| 31-60                     | 4.85                 | 60.00                    |

If the consumption is above 60 kWh per month the following tariffs will be applicable.

| Monthly Consumption (kWh) | Unit Charge (Rs/kWh) | Fixed Charge (Rs/month) |
|---------------------------|----------------------|-------------------------|
| 0-60                      | 7.85                 | -                        |
| 61-90                     | 10.00                | 90.00                   |
| 91-120                    | 27.75                | 480.00                  |
| 121-180                   | 32.00                | 480.00                  |
| >180                      | 45.00                | 540.00                  |

## Usage

Enter the units of electricity (number of kWh) consumed monthly and the program will output the calculated electricity bill for that month.

For example:

Input | Result
----- | ------
45    | 207.75
65    | 611.0

