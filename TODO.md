## General

- Requirements for new members to get commit rights to subaru-community github repos
  - must finish a port of one sub 10 second car (Subaru preferred) and get the PR merged to upstream or subaru-community
  - must fix at least 1 bug in upstream master branch panda safety and get PR merged (any make or model)
  - must find at least one undocumented canbus signal and submit PR to opendbc upstream or subaru-community

## TODO

### Release management and CI

- Fix and document updating reference replay routes procedure
  - [Initial documentation](https://github.com/martinl/openpilot/wiki/openpilot-process-replay-logs-storage)
- Test and document subaru-community release workflow
  - devel branch
  - release3 branch
- Create new subaru-community-c2 branch (based on dragonpilot-community?)
  - basic functionality based on 0.8.13 ml models
  - all compatible changes merged from upstream
- Test and document subaru-community-c2 release workflow
  - devel branch
  - release2 branch
- move repos to openpilot-subaru-community github org?
- EU GDPR compliance
  - add option to disable uploading all openpilot logs and videos to comma cloud storage
  - add option to upload logs and videos to private cloud instances or on-prem storage services (S3/Google Drive/Azure/Nextcloud/etc)
  - add option to post-process recorded videos offline to blur peoples faces and car license plates before uploading

### Adding support for new models and model years, fixing bugs and finding missing signals for WIP models

- Enable Pre-Global dash lanelines display [good first PR]
  - more info: https://github.com/martinl/openpilot/issues/25
- Crosstrek Hybrid support
  - find a openpilot user who can provide route for testing (Dave32?)
  - find ES_Status CAN message equivalent (Cruise_Activated signal)
  - find ES_Distance CAN message equivalent (Cruise disengage, Car_Follow, Close_Distance)
  - get stock and openpilot engaged routes with uploaded logs
      - set route as preserved and public after logs upload is complete
  - more info: https://github.com/martinl/openpilot/issues/94
  - more info: https://github.com/martinl/openpilot/issues/56
  - PR: https://github.com/commaai/openpilot/pull/25378
- Subaru Ascent 2023 support
  - PR: https://github.com/commaai/openpilot/pull/27583
- Subaru Forester 2022 support
  - openpilot PR: https://github.com/commaai/openpilot/pull/26700
  - opendbc PR: https://github.com/commaai/opendbc/pull/758
  - get stock and openpilot engaged routes with uploaded logs
      - set route as preserved and public after logs upload is complete
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

### Car Harnesses
- Subaru D

More info in Openpilot Subaru community [wiki](https://github.com/commaai/openpilot/wiki/Subaru) page

PS. Feel free to work on any of those whenever you have some free time and submit PR-s with relevant route
PS2. Have fun but do not mess with panda safety, safety limits and make sure all CI tests pass before testing on road
