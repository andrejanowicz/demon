# about
Demon is a <b>dep</b>arture <b>mon</b>itor written in python. It connects to VRR's EFA interface and prints the results in a way to mimic the look of EVAG's public departure displays.

# setup
- install requests module
- set executable bit
> pip3 install requests</br>
> chmod +x demon.py

# usage
> ./demon.py city station offset --platform 1,2,3,n --rows 5

make sure to mask spaces in station names with a backslash or put station name in quotation marks.

# example

> /demon.py essen "Abzweig Aktienstr" 25 --platform 1,2 --rows 5
>
> 105&nbsp;&nbsp;&nbsp;&nbsp;Finefraustraße&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28 min</br>
> 104&nbsp;&nbsp;&nbsp;&nbsp;Mülheim Hauptfriedhof&nbsp;&nbsp;28 min</br> 
> 105&nbsp;&nbsp;&nbsp;&nbsp;Unterstraße&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33 min</br>
> 105&nbsp;&nbsp;&nbsp;&nbsp;Finefraustraße&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;43 min</br> 
> 105&nbsp;&nbsp;&nbsp;&nbsp;Unterstraße&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;48 min</br>
