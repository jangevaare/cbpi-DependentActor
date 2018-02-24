from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase

@cbpi.actor
class DependentActor(ActorBase):
    base = Property.Actor(label="Base Actor", description="Select the actor you would like to add a dependency to.")
    dependency_type = Property.Select(label="Dependency Type", options=["Restriction", "Prerequisite"], description="Select the dependency type. With 'Restriction', the 'Actor Dependency' is required to be OFF in order to switch the 'Base Actor' ON. With 'Prerequisite', the 'Actor Dependency' is required to be ON in order to switch the 'Base Actor' ON.")
    dependency = Property.Actor(label="Actor Dependency", description="Select the actor that the base actor will depend upon.")

    def init(self):
        # Make sure the Base Actor is off
        self.api.switch_actor_off(int(self.base))
        # Hide Base Actor
        for idx, value in cbpi.cache["actors"].iteritems():
            if idx == int(self.base):
                value.hide = True
        # Synchronize current power setting with the Base Actor
        # TODO

    def set_power(self, power):
        self.api.actor_power(int(self.base), power=power)

    def off(self):
        self.api.switch_actor_off(int(self.base))

    def on(self, power=None):
        dependency_name = ""
        for idx, value in cbpi.cache["actors"].iteritems():
            if idx == int(self.dependency):
                dependency_name = value.name
        for idx, value in cbpi.cache["actors"].iteritems():
            if idx == int(self.dependency):
                if (value.state == 0) & (self.dependency_type == "Restriction"):
                    self.api.switch_actor_on(int(self.base), power=power)
                elif (value.state == 1) & (self.dependency_type == "Prerequisite"):
                    self.api.switch_actor_on(int(self.base), power=power)
                else:
                    self.api.notify(headline="Powering of actor prevented", message="This is due to the current power state of it's dependency, %s" % (dependency_name), timeout=None, type="danger")
                    raise UserWarning("Powering of actor prevented by the state of it's dependency")
