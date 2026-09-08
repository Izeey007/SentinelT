# 2.4 GHz RC Control

SentinelT is controlled by a human operator using a **2.4 GHz transmitter/receiver system**, as required for Robo Wars.

## Planned Channel Mapping

| Function | Control |
|---|---|
| Forward / reverse | Throttle channel |
| Left / right steering | Steering channel |
| Stop | Neutral throttle/steering |
| Auxiliary mechanism enable | Dedicated switched channel |

## Failsafe Behaviour

- Invalid or lost RC signal -> drive outputs disabled.
- Controller reset/startup -> all actuator outputs disabled.
- E-Stop active -> actuator power disabled independently of normal RC commands.
- Auxiliary enable defaults to OFF.

## Final Integration TODO

The exact receiver model, channel order, pulse ranges/protocol, failsafe settings and ESC calibration values will be added after the selected physical hardware is obtained and bench-tested.
