The issue is cannot get all traffic signs in specified area:
```
center at (45.464664,9.18854) with radius 3000: 117 traffic signs in 2310 attributes
center at (45.464664,9.18854) with radius 5000: 118 traffic signs in 3635 attributes
center at (45.464664,9.18854) with radius 7000: 118 traffic signs in 4178 attributes
center at (45.464664,9.18854) with radius 10000: 118 traffic signs in 4430 attributes
```
Note the number of traffic signs increased only by 1 after expanding the area.

Cause is the max search results limit of the Map Attributes API of 1000:
https://smap.hereapi.com/serviceconfiguration.json
```
"maxSearchResults":1000
```
The solution is applying a filter to traffic signs in the initial request:
```
center at (45.464664,9.18854) with radius 3000: 245 traffic signs
center at (45.464664,9.18854) with radius 5000: 515 traffic signs
center at (45.464664,9.18854) with radius 7000: 881 traffic signs
center at (45.464664,9.18854) with radius 10000: 1065 traffic signs
```

This repo shares the Python codes for demonstrating the issue and solution.