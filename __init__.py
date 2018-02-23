from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase
from modules.core.hardware import SensorPassive

@cbpi.actor
class Actor_with_Restriction(ActorBase):
    base = Property.Actor("Base Actor", description="Select the actor you would like to limit to when it's restriction is off")
    restriction = Property.Actor("Actor Restriction", description="Select the actor that will prevents the base actor from becoming active, when it itself is active")
    #
    # def init(self):
    #     self.base.hide == TRUE

    def set_power(self, power):
        if self.exclusion.state == 0:
            self.api_actor_power(self.base, power=power)
        else:
            self.notify(headline="Set power prevented", message="Could not set power to %s, since %s is currently on" % (self.base, self.exclusion), timeout=None)

    def on(self, power=None):
        if self.exclusion.state == 0:
            self.api.switch_actor_on(self.base, power=power)
        else:
            self.notify(headline="Actor activation prevented", message="Could not turn %s on, since %s is currently on" % (self.base, self.exclusion), timeout=None)

    def off(self):
        self.api.switch_actor_off(self.base)

@cbpi.actor
class Actor_with_Prerequisite(ActorBase):
    base = Property.Actor("Base Actor", description="Select the actor you would like to limit to when it's prerequisite is on")
    requisite = Property.Actor("Actor Prerequisite", description="Select the actor that enables the base actor to become active, when it itself is active")

    def set_power(self, power):
        if self.requisite.state == 1:
            self.api_actor_power(self.base, power=power)
        else:
            self.notify(headline="Set power prevented", message="Could not set power to %s, since %s is currently off" % (self.base, self.exclusion), timeout=None)

    def on(self, power=None):
        if self.requisite.state == 1:
            self.api.switch_actor_on(self.base, power=power)
        else:
            self.notify(headline="Actor activation prevented", message="Could not turn %s on, since %s is currently off" % (self.base, self.exclusion), timeout=None)

    def off(self):
        self.api.switch_actor_off(self.base)
