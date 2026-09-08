/*
  SentinelT Robo Wars - control/safety skeleton
  Designer: Thato Glen Assegaai

  IMPORTANT:
  - Human-operated 2.4 GHz RC concept only.
  - Hardware-specific receiver protocol, pin assignments, ESC calibration,
    voltage/current limits and actuator ratings must be validated on the
    selected physical hardware before use.
  - The E-Stop is a hardware safety function and must not rely on software.
*/

#include <Arduino.h>

struct RcCommand {
  int throttle;      // expected normalized range: -1000 .. +1000
  int steering;      // expected normalized range: -1000 .. +1000
  bool auxiliaryEnable;
  bool valid;
};

enum RobotState {
  SAFE_DISABLED,
  RC_READY,
  OPERATING
};

RobotState state = SAFE_DISABLED;
unsigned long lastValidRcMs = 0;
const unsigned long RC_TIMEOUT_MS = 250;

bool hardwareEStopActive() {
  // TODO: replace with the final verified E-Stop status input/interlock.
  // The physical E-Stop must independently disable actuator power.
  return false;
}

RcCommand readRcReceiver() {
  RcCommand cmd{};
  // TODO: implement selected 2.4 GHz receiver protocol and channel mapping.
  cmd.throttle = 0;
  cmd.steering = 0;
  cmd.auxiliaryEnable = false;
  cmd.valid = false;
  return cmd;
}

void disableAllActuators() {
  // TODO: send neutral/disable command to both drive outputs.
  // TODO: force auxiliary actuator controller to disabled state.
}

void applyDriveCommand(int throttle, int steering) {
  // Differential-drive mixing example only.
  int left  = constrain(throttle + steering, -1000, 1000);
  int right = constrain(throttle - steering, -1000, 1000);

  // TODO: convert normalized commands to the selected ESC/motor-driver signals.
  (void)left;
  (void)right;
}

void setAuxiliaryEnabled(bool enabled) {
  // TODO: map to the selected auxiliary controller enable input.
  // Default must remain disabled.
  (void)enabled;
}

void setup() {
  disableAllActuators();
  state = SAFE_DISABLED;
}

void loop() {
  if (hardwareEStopActive()) {
    disableAllActuators();
    state = SAFE_DISABLED;
    return;
  }

  RcCommand cmd = readRcReceiver();

  if (cmd.valid) {
    lastValidRcMs = millis();
    state = RC_READY;
  }

  const bool rcTimedOut = (millis() - lastValidRcMs) > RC_TIMEOUT_MS;
  if (!cmd.valid || rcTimedOut) {
    disableAllActuators();
    state = SAFE_DISABLED;
    return;
  }

  applyDriveCommand(cmd.throttle, cmd.steering);
  setAuxiliaryEnabled(cmd.auxiliaryEnable);
  state = OPERATING;
}
