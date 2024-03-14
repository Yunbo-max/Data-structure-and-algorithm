# -*- coding: utf-8 -*-
# @Author: Yunbo
# @Date:   2024-03-14 20:51:44
# @Last Modified by:   Yunbo
# @Last Modified time: 2024-03-14 21:08:00
import argparse
parser = argparse.ArgumentParser(description="calculating the area of rectangle")

parser.add_argument("--length",type=int,default=10,help="The length of the rectangle!")
parser.add_argument("--width",type=int,default=2,help="The width of rectangle!")

args = parser.parse_args()





if __name__ == "__main__":
    results = args.length*args.width
    print("the rectangle area is " + str(results))
