# For everyone reading this, anything here is subject to change.
A risk like game
starts around 1800s up to 8 players
can build up your own or expand out
resources are discovers over time
realtime multiplayer


# Primary rules - 
Everything is pretty private. Only thing on the board is troops (not subs), 
cites and what land belongs to who


# possible buildings 
upgradable (town hall) 

# resources 
I would really like to see 3 more resources. Not super complex, and could could easily fit on a bar on the side/bottom of the screen
tier one (easy to get):
```
People //agreed on this one already
Wood // ^
metal// ^
```
tier two:
```
oil // could give purpose to ocean areas 
gold // Agreed on this one
silcon //used for tech stuff later in the game
```
tier three
```
Uranium
```
# we could possibly have a bloons like system where you could spend resources to get different types of troops
- ex. upgrade basic troop (which could start off as a rifleman) to sniper, heavy gunner or a plane to fighter plane, bomber

# possible buildable troops
- Basic troop (only deployable in hundreds)
- Tank (possibly replace with a generic vehicle type, tank is just a type of vehicle that can be "trained" once researched)
- plane
- boat
- carriers (boat type: transport troops, planes, tanks, etc over water to another area over water in case we are doing islands)
// I like these, we need to consider things like water depth maybe, we dont have to but just an idea - bryce
- missile trucks (fire missiles from a distance (a cell or two over), not crazy damage but could kill basic unmoving infantry, counter by moving troops)

## special troops 
- spy plane
- submarine

# possible future features
- pause
- random 
- Research plot to upgrade things like troop training times, less resources to train troops, research new troops etc // I like this idea alot = bryce
- players can possibly find abandoned bunkers around the map to find basic 
resources early game, gives incentive to explore map early to get ahead of others // There is a few questions about how we would implement this, but this is
very doable - bryce






# the tech
Would be hosted on a server, and one person would be able to start said game 



The map would be divied into chunks 
Each chunk would have - 
8 by 8 grid
What ores are underneath
ownership (to a player , or unclaimed)
what things are drawn in the grid (and where)
as an object:
```
drawn = {lvl_one_jet[0][1], oil_rig[4][4]} //This could be its own array
ores = {oil} //only oil true for this grid 
owner = "Bryce" //who owns tile
```
