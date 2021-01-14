# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Xinyi Wang  260849970

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################
# helper functions
def sum_of_5_multi_tonnes(a,b,c,d,e):
    '''(num) -> float
    convert multiple kilograms into tonnes at the same time
    >>> sum_of_5_multi_tonnes(1000,2000,3000,4000,5000)
    15.0
    '''
    summation=a+b+c+d+e
    summation_in_tonnes=kg_to_tonnes(summation)
    return summation_in_tonnes

def ft_of_annual_online_use(daily_online_use):
    """(num) ->float
    returns the emission of CO2E in kg through online usage
    >>> round(ft_of_annual_online_use(1),4)
    20.0883
    >>> round(ft_of_annual_online_use(2),4)
    40.1767
    """
    #need to multiple 1/1000 to convert g to kg
    kg_of_daily_online_usage=daily_online_use*55/1000
    kg_of_annual_online_usage=daily_to_annual(kg_of_daily_online_usage)
    return kg_of_annual_online_usage
    
######################################

def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    #Here I use my helper function
    kg_of_annual_online_usage=ft_of_annual_online_use(daily_online_use)
    #compute annual phone usage,multiple daily usage hours by 1250kg/(year,hour)
    kg_of_annual_phone_usage=daily_phone_use*1250 
    kg_of_new_light_devices=new_light_devices*75
    kg_of_medium_devices=new_medium_devices*200
    kg_of_heavy_devices=new_heavy_devices*800
    total_ft=sum_of_5_multi_tonnes(kg_of_annual_online_usage,\
                                   kg_of_annual_phone_usage, \
                                   kg_of_new_light_devices,\
                                   kg_of_medium_devices,kg_of_heavy_devices)
    
    return total_ft


######################################

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    annual_kg_of_vagen=daily_to_annual(2.89)
    annual_kg_of_meat=daily_to_annual(daily_g_meat*0.0268)
    annual_kg_of_cheese=daily_to_annual(daily_g_cheese*0.012)
    annual_kg_of_milk=daily_to_annual(daily_L_milk*0.2677777)
    annual_kg_of_egg=daily_to_annual(daily_num_eggs*0.3)
    tonnes_of_diet=sum_of_5_multi_tonnes(annual_kg_of_vagen, \
                                         annual_kg_of_meat,\
                                         annual_kg_of_cheese,\
                                         annual_kg_of_milk,annual_kg_of_egg)
    return tonnes_of_diet


#################################################

if __name__ == '__main__':
    doctest.testmod()

