# Notice: as of May 22, 2019 this plugin is no longer being developed or maintained. For my recent work with brewery control software, please see my open-source brewing dashboard, [brew2](https://github.com/jangevaare/brew2).

## cbpi-DependentActor
This CraftBeerPi 3.0 plugin provides a new actor type called DependentActor. DependentActors are containers for existing Base Actors, which will only power ON if their Actor Dependency is in the correct state. The Actor Dependency must be ON if it is set as a prerequisite, and OFF if it is set as a restriction.

A DependentActor, can even use some other DependentActor as a base or dependency.

When a DependentActor is created, the Base Actor is automatically hidden from the dashboard (if it was not already). When configuring kettles and fermentors, make sure to select your new DependentActor, as the Base Actor is not currently automatically replaced in these.

This plugin is not a substitute for properly rated hardware components and safety features.

## Examples
* An actor with a restriction may be used in the case of wishing to prevent multiple heating elements from being on at the same time. 
* An actor with a prerequisite may be used if you wish to only have a heating element on if a recirculating pump is on at the same time.
* Many other uses!
