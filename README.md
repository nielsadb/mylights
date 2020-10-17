Simplest possible Philips Hue lights control app.


Python-based. Simpler for me than learning a new language.


# Design
As a library. The specific code is in control.
Offers convenient access to the bridge.
The bridge state is kept in dictionaries. Simple to/from JSON.
Convenience functions only for really repetative work, keep to a mimimum.



# Ideas for Applications

## Script that configures my system

* Check if all scenes are there. Else create them.
  - Tryout: create a scene with current lights.
  - Tryout: delete that scene.
  - Tryout: create a new room scene: set lights and create scene with light group.
  - Tryout: same for full house scene.
* Configure all motion sensors.
* 

* Re-usable configuration parts (e.g. colors), to make it easy to keep things consistent.
* Re-usable configuration adapters, e.g. to indicate what it means to dim something.
  - Also modeled as functions.
* Consistency in behavior of buttons, but more advanced as what Philips app offers.
  - Configuration of buttons via 1 method.
* Identification of unused scenes and other garbage. Automated cleaning.
  - Management via CSV file. Editable in Excel.
* Consistency in naming of scenes, lights, etc.
  - Structured names via some formatting, only place is entered manually. Use model info.
* Mimick the Philips Hue app with cycling between scenes. HueLight's hold is not nice.
  - TBD how to do this. Configure a switch + peek in JSON.
* Use capabilities API call to avoid overruns of capabilities.
* Batched commit of changes. Only execute when sure it will work.
* Negating sets of lights: all but ...

* Tuning of lights: let lights always be a certain % brightness of the room setting. Hue constant.

* Modes: system-level behavior determined by time of day or explicit trigger.
  - Translates into devices enabled/disabled or reconfigured.

* Mimick dimming behavior via scene cycling: allow + to act as an ON switch.

Scenes are used when:
* They are used by a device, e.g. a 







# OLD: PLUG-IN DESIGN

```
$ mylights -h
usage: mylights ( plugin-name -options? )*

plug-ins:
  server    block and run read-only RESTful webservice
  repl      run Python REPL after start-up

```

## Default plug-ins
Some directory in the default $MYLIGHTS_PATH.
These can be added to plug-in pipeline by the mylights application itself.

bridge_access
bridge_read
bridge_write

Suppressed by -nob(ridge).

These plugins simply call mylights.plugin.xyz_bridge(). So these functions are also availble for plug-ins.

## Plug-in interaction
The `globals` parameter is used to pass package-private data/callbacks.

Parameters have generic syntax:
`-name`: boolean argument (True)
`-name:value`: string argument
These parameters are passed to the factory function.


Code consists of:
- A REST API server for read-only control.
- 
  - No configuration or detection of new lights.
* Offer powerful abstractions to keep configuration consistent.
  - Read and write configuration via Python objects.
  - Consistency via code processing these objects.
  - Use the REPL for interactive ad hoc changes.

Implementation 

New concept: controls.
These do some task, which just runs Python 

REST API:
/controls
Ordered list of controls.







# 18/04/2020 22:45

A mode:
- Configuration of the motion sensors.
- Configurstion of the dimmer switches.
- Rotating scenes: initial, second, third, ...
  Definition of nearly off and off.
  This information is not mirrored in a Philip bridge concept.
  Refer to in dimmer switch and motion sensor config.
- An initial scene to apply.

Prototype:
Can you reprogram a dimmer switch via an action?