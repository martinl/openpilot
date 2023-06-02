## General

- Document process for adding new members with commit rights to subaru-community github repos
- Create subaru-community release workflow
  - devel branch
  - release3 branch
- Create subaru-community-c2 branch based on dragonpilot-community
- Create subaru-community-c2 release workflow
  - devel branch
  - release2 branch
- Enable Pre-Global dash lanelines display [good first PR]
  - more info: https://github.com/martinl/openpilot/issues/25

## New models support

- Crosstrek Hybrid support
  - find a openpilot user who can provide route for testing (Dave32?)
  - find ES_Status CAN message equivalent (Cruise_Activated signal)
  - find ES_Distance CAN message equivalent (Cruise disengage, Car_Follow, Close_Distance)
  - more info: https://github.com/martinl/openpilot/issues/94
  - more info: https://github.com/martinl/openpilot/issues/56
  - PR: https://github.com/commaai/openpilot/pull/25378
- Subaru Ascent 2023 support
  - PR: https://github.com/commaai/openpilot/pull/27583
- Subaru Forester 2022 support
  - openpilot PR: https://github.com/commaai/openpilot/pull/26700
  - opendbc PR: https://github.com/commaai/opendbc/pull/758
- Global Gen1 Stop and Go autoresume
  - find diagnostic message for resume OR do AEB tests for current implementation
  - find a method for detecting electronic parking brake (remove UI toggle)
  - openpilot PR: https://github.com/commaai/openpilot/pull/28064
  - panda PR: https://github.com/commaai/panda/pull/1379
- Global Gen2 Stop and Go autoresume
- Subaru Global Gen1 Experimental longitudinal control
  - PR: https://github.com/commaai/openpilot/pull/25345
- Pre-Global Stop and Go autoresume
  - find a way to autoresume for manual parking brake cars

PS. Feel free to work on any of those whenever you have some free time and submit PR-s with relevant route
