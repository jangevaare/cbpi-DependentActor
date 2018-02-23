# cbpi-dependent-actors
A CraftBeerPi 3 plugin which provides dependent actors. Two new actor types are
provided:
* Actor with Restriction
* Actor with Prerequisite

This plugin is not a substitute for properly rated hardware components and safety features.

## Actor with Restriction
This is an actor that can *NOT* be activated when it's restricting actor is already active. A notification message will be provided if activation of an actor has been prevented.

## Actor with Prerequisite
This is an actor that can *ONLY* be activated when it's prerequisite actor is already active. A notification message will be provided if activation of an actor has been prevented.
