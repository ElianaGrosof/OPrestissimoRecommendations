# OPrestissimoRecommendations
recommendation engine script project for OPrestissimo

Make sure that you have pandas installed. To install,
> pip3 install pandas

To run:

Run test_apyroi.py, which takes three arguments: the support value, the .csv file containing the list of carts, the .csv file containing the complete list of courses

Ex:
> python3 test_apyroi.py 0.01 s2014.csv courses.csv
or 
> python3 test_apyroi.py 0.01 ./semester_csvs/s2015.csv courses.csv

Output will be the top best relationships, as determined by a mix of Lift and Support. 
Example output (given arguments as above):

                                                 Items  \
120  {Eco Perspect Forager Lifeways, Earth's Enviro...   
121  {Eco Perspect Forager Lifeways, Earth's Enviro...   
118   {US Foreign Policy and MENA, Beginning Arabic I}   
119   {US Foreign Policy and MENA, Beginning Arabic I}   
114                   {Music Theory I, Aural Skills I}   

                          Antecedent                       Consequent  \
120           {Earth's Environments}  {Eco Perspect Forager Lifeways}   
121  {Eco Perspect Forager Lifeways}           {Earth's Environments}   
118             {Beginning Arabic I}     {US Foreign Policy and MENA}   
119     {US Foreign Policy and MENA}             {Beginning Arabic I}   
114                 {Aural Skills I}                 {Music Theory I}   

      Support  Confidence       Lift  
120  0.012698    0.285714  15.000000  
121  0.012698    0.666667  15.000000  
118  0.015873    0.833333  47.727273  
119  0.015873    0.909091  47.727273  
114  0.015873    0.769231  34.615385 
