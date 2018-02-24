# cbpi-dependent-actors
This is a CraftBeerPi 3 plugin that provides a new actor type called DependentActor. These actors are containers for an existing actor, which implements dependency on another actor. The dependency may either work as a restriction or a prerequisite.

A DependentActor, can even use some other DependentActor as a base or dependency.

When a DependentActor is created, the Base Actor is automatically hidden from the dashboard (if it was not already). When configuring kettles and fermentors, make sure to select your new DependentActor, as the Base Actor is not currently automatically replaced in these.

This plugin is not a substitute for properly rated hardware components and safety features.

## Examples
* An actor with a restriction may be used in the case of wishing to prevent multiple heating elements from being on at the same time. 
* An actor with a prerequisite may be used if you wish to only have a heating element on if a recirculating pump is on at the same time.
* Many other uses!
