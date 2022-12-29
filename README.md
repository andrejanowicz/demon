# About
Demon is a <b>dep</b>arture <b>mon</b>itor written in python. It connects to VRR's EFA interface and prints the results in a way to mimic the look of EVAG's public departure displays.

# Setup
- install requests module
- set executable bit

``` 
pip3 install requests
chmod +x demon.py
```

# Usage
`./demon.py city "station name" offset_in_minutes --platform 1,2,3,n --rows 5`

make sure to mask spaces in station names with a backslash or put station name in quotation marks.

# Output

``` ./demon.py Essen "Abzweig Aktienstr" 25 --platform 1,2 --rows 5

105  Finefraustraße          28 min
104  Mülheim Hauptfriedhof   28 min 
105  Unterstraße             33 min
105  Finefraustraße          43 min 
105  Unterstraße             48 min
```
