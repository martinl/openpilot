2023-06-12
==========
* FPv2 updates
  * Subaru Forester Wilderness 2023 / @FutureGhost

2023-05-01
==========
* FPv2 updates
  * Subaru Impreza 2019 / @chasebolt

2023-04-28
==========
* FPv2 updates
  * Subaru Legacy 3.6R Limited 2016 / @John

2023-04-24
==========
* FPv2 updates
  * Subaru Crosstrek 2023 / @Wafflles

2023-04-23
==========
* FPv2 updates
  * Subaru Forester 2017 / @boettler

2023-04-09
==========
* FPv2 updates
  * Subaru Forester 2020 / @Decosta

2023-03-05
==========
* FPv2 updates
  * Subaru Forester 2019 / @PlanZ
* Forester 2022 support / @martinl

2023-03-04
==========
* openpilot 0.9.1
  * New driving model
    * 30% improved height estimation resulting in better driving performance for tall cars
  * Driver monitoring: removed timer resetting on user interaction if distracted
  * UI updates
    * Adjust alert volume using ambient noise level
    * Driver monitoring icon shows driver's head pose
    * German translation thanks to Vrabetz and CzokNorris!
  * Cadillac Escalade 2017 support thanks to rickygilleland!
  * Chevrolet Bolt EV 2022-23 support thanks to JasonJShuler!
  * Genesis GV60 2023 support thanks to sunnyhaibin!
  * Hyundai Tucson 2022-23 support
  * Kia K5 Hybrid 2020 support thanks to sunnyhaibin!
  * Kia Niro Hybrid 2023 support thanks to sunnyhaibin!
  * Kia Sorento 2022-23 support thanks to sunnyhaibin!
  * Kia Sorento Plug-in Hybrid 2022 support thanks to sunnyhaibin!
  * Toyota C-HR 2021 support thanks to eFiniLan!
  * Toyota C-HR Hybrid 2022 support thanks to Korben00!
  * Volkswagen Crafter and MAN TGE 2017-23 support thanks to jyoung8607!

2023-01-29
==========
* FPv2 updates
  * Subaru Outback 2017 / @rikinmshah

2022-12-27
==========
* Restore pid tuning values for preglobal models / @martinl

2022-12-06
==========
* FPv2 updates
  * 2022 Impreza / @Frob
  * 2019 Legacy / @jwithing
  * 2020 Levorg / @lonelyju

2022-11-29
==========
* FPv2 updates
  * 2023 Crosstrek Limited / @JWynegar

2022-11-27
==========
* FPv2 updates
  * 2022 Forester Wilderness / @FutureGhost

2022-11-18
==========
* FPv2 updates
  * 2022 Outback Wilderness / @valtou

2022-11-16
==========
* openpilot 0.9.0
  * New driving model
    * Internal feature space information content increased tenfold during training to ~700 bits, which makes the model dramatically more accurate
    * Less reliance on previous frames makes model more reactive and snappy
    * Trained in new reprojective simulator
    * Trained in 36 hours from scratch, compared to one week for previous releases
    * Training now simulates both lateral and longitudinal behavior, which allows openpilot to slow down for turns, stop at traffic lights, and more in experimental mode
  * Experimental driving mode
    * End-to-end longitudinal control
    * Stops for traffic lights and stop signs
    * Slows down for turns
    * openpilot defaults to chill mode, enable experimental mode in settings
  * Driver monitoring updates
    * New bigger model with added end-to-end distracted trigger
    * Reduced false positives during driver calibration
  * Self-tuning torque controller: learns parameters live for each car
  * Torque controller used on all Toyota, Lexus, Hyundai, Kia, and Genesis models
  * UI updates
    * Matched speeds shown on car's dash
    * Multi-language in navigation
    * Improved update experience
    * Border turns grey while overriding steering
    * Bookmark events while driving; view them in comma connect
    * New onroad visualization for experimental mode
  * tools: new and improved cabana thanks to deanlee!
  * Experimental longitudinal support for Volkswagen, CAN-FD Hyundai, and new GM models
  * Genesis GV70 2022-23 support thanks to zunichky and sunnyhaibin!
  * Hyundai Santa Cruz 2021-22 support thanks to sunnyhaibin!
  * Kia Sportage 2023 support thanks to sunnyhaibin!
  * Kia Sportage Hybrid 2023 support thanks to sunnyhaibin!
  * Kia Stinger 2022 support thanks to sunnyhaibin!

2022-10-15
==========
* FPv2 updates
  * Forester 2018 / @ganny

2022-09-09
==========
* openpilot 0.8.16
  * New driving model
    * Reduced turn cutting
  * Auto-detect right hand drive setting with driver monitoring model
  * Improved fan controller for comma three
  * New translations
    * Japanese thanks to cydia2020!
    * Brazilian Portuguese thanks to AlexandreSato!
  * Chevrolet Bolt EUV 2022-23 support thanks to JasonJShuler!
  * Chevrolet Silverado 1500 2020-21 support thanks to JasonJShuler!
  * GMC Sierra 1500 2020-21 support thanks to JasonJShuler!
  * Hyundai Ioniq 5 2022 support thanks to sunnyhaibin!
  * Hyundai Kona Electric 2022 support thanks to sunnyhaibin!
  * Hyundai Tucson Hybrid 2022 support thanks to sunnyhaibin!
  * Subaru Legacy 2020-22 support thanks to martinl!
  * Subaru Outback 2020-22 support

* refactored panda safety to align with upstream / @martinl
  * Subaru Forester Hybrid
  * Subaru Crosstrek Hybrid

2022-08-14
==========
* FPv2 updates
  * 2021 Forester / @meeeeeeeeeee

2022-07-20
==========
* openpilot 0.8.15
  * New driving model
    * Path planning uses end-to-end output instead of lane lines at all times
    * Reduced ping pong
    * Improved lane centering
  * New lateral controller based on physical wheel torque model
    * Much smoother control that's consistent across the speed range
    * Effective feedforward that uses road roll
    * Simplified tuning, all car-specific parameters can be derived from data
    * Used on select Toyota and Hyundai models at first
    * Significantly improved control on TSS-P Prius
  * New driver monitoring model
    * Bigger model, covering full interior view from driver camera
    * Works with a wider variety of mounting angles
    * 3x more unique comma three training data than previous
  * Navigation improvements
    * Speed limits shown while navigating
    * Faster position fix by using raw GPS measurements
  * UI updates
    * Multilanguage support for settings and home screen
    * New font
    * Refreshed max speed design
    * More consistent camera view perspective across cars
  * Reduced power usage: device runs cooler and fan spins less
  * AGNOS 5
    * Support VSCode remote SSH target
    * Support for delta updates to reduce data usage on future OS updates
  * Chrysler ECU firmware fingerprinting thanks to realfast!
  * Honda Civic 2022 support
  * Hyundai Tucson 2021 support thanks to bluesforte!
  * Kia EV6 2022 support
  * Lexus NX Hybrid 2020 support thanks to AlexandreSato!
  * Ram 1500 2019-21 support thanks to realfast!

2022-07-05
==========
* Initial lateral torque control support for all subaru-community supported models / @martinl

2022-06-15
==========
* 2020 Forester Hybrid support / @martinl

2022-06-07
==========
* openpilot 0.8.14
  * New driving model
    * Bigger model, using both of comma three's road-facing cameras
    * Better at cut-in detection and tight turns
  * New driver monitoring model
    * Tweaked network structure to improve output resolution for DSP
    * Fixed bug in quantization aware training to reduce quantizing errors
    * Resulted in 7x less MSE and no more random biases at runtime
  * Added toggle to disable disengaging on the accelerator pedal
  * comma body support
  * Audi RS3 support thanks to jyoung8607!
  * Hyundai Ioniq Plug-in Hybrid 2019 support thanks to sunnyhaibin!
  * Hyundai Tucson Diesel 2019 support thanks to sunnyhaibin!
  * Toyota Alphard Hybrid 2021 support
  * Toyota Avalon Hybrid 2022 support
  * Toyota RAV4 2022 support
  * Toyota RAV4 Hybrid 2022 support
* FPv2 updates
  * 2020 Subaru Outback 2.5i Touring / @CheckYourSix
  * 2020 Impreza / @R0B

2022-05-18
==========
* FPv2 updates
  * 2020 Forester Hybrid - AUDM / @aztan

2022-05-09
==========
* FPv2 updates
  * 2022 Outback XT Touring - UDM / @cook.w.ryan
  * 2021 Legacy - UDM / @duchuy1993

2022-05-05
==========
* FPv2 updates
  * 2018 Legacy - UDM / @Brycey92

2022-05-04
==========
* FPv2 updates
  * 2022 Outback - UDM / @duchuy1993

2022-04-27
==========
* openpilot 0.8.13.1
  * NEOS 20: improved reliability

2022-04-02
==========
* FPv2 updates
  * 2018 Outback - UDM / @TaylorH

2022-03-10
==========
* FPv2 updates
  * 2019 Impreza Sport - UDM / @Milkdud
  * 2018 Legacy - UDM / @Hassan

2022-02-22
==========
* Firmware query delay toggle / @martinl
* Global SNG distance in meters / @martinl
* FPv2 updates
  * 2016 Outback 2.5i - AUDM / @marls
  * 2018 Crosstrek 2.0 - AUDM / @marls

2022-02-20
==========
* Merge upstream (0.8.13) / @martinl

2022-02-19
==========
* FPv2 updates
  * 2017 Impreza Limited - UDM / @Houston2222

2022-02-07
==========
* Fix for preglobal models FPv2 issue / @martinl
* Fix for disengage on gas LKAS fault / @martinl

2022-02-05
==========
* Merge upstream (0.8.13) / @martinl
* Subaru car interface refactoring / @martinl
* FPv2 retry always on if no candidates match after first pass / @martinl

2022-01-30
==========
* FPv2 updates
  * Impreza 2020 - UDM / @Chickens

2022-01-26
==========
* FPv2 updates
  * 2018 Legacy - UDM / @Hassan

2021-12-28
==========
* FPv2 updates
  * 2017 Impreza 2.0 - UDM / @prlifestyle93

2021-12-17
==========
* FPv2 updates
  * 2019 Forester - UDM / @Patienc3

2021-12-16
==========
* Merge upstream (0.8.12) / @martinl

2021-12-01
==========
* Merge upstream (0.8.11) / @martinl

2021-11-19
==========
* FPv2 updates
  * 2019 Crosstrek - UDM / @AJInvesting

2021-11-17
==========
* Fast FPv2 fingerprinting when Community Features toggle is off / @martinl

2021-11-16
==========
* FPv2 updates
  * 2019 Impreza - UDM / @phosphor

2021-11-10
==========
* FPv2 updates
  * 2018 Forester - UDM / @2018NissanRogue

2021-11-07
==========
* FPv2 updates
  * 2022 Outback - UDM / @atran913

2021-11-01
==========
* merge upstream (0.8.10) / @martinl

2021-10-22
==========
* FPv2 updates
  * 2017 Impreza 1.6 - UDM / @Moodkiller

2021-10-22
==========
* FPv2 updates
  * 2016 WRX - UDM / @Hexinator

2021-10-03
==========
* FPv2 updates
  * 2021 Crosstrek Premium - UDM / @pemerick07

2021-09-30
==========
* Fix for preglobal LKAS fault / @martinl

2021-09-29
==========
* Merge upstream (0.8.9) / @martinl
  * Improved fan control on comma three
  * AGNOS 1.5: improved stability
  * Honda e 2020 support

2021-09-05
==========
* FPv2 updates
  * 2019 Forester Sport - UDM / @Zapman

2021-08-29
==========
* FPv2 updates
  * 2018 Forester 2.5i Premium - UDM / @Diesel Monkey

2021-08-26
==========
* Merge upstream (0.8.8) / @martinl
  * New driving model with improved laneless performance
    * Trained on 5000+ hours of diverse driving data from 3000+ users in 40+ countries
    * Better anti-cheating methods during simulator training ensure the model hugs less when in laneless mode
    * All new desire ground-truthing stack makes the model better at lane changes
  * New driver monitoring model: improved performance on comma three
  * NEOS 18 for comma two: update packages
  * AGNOS 1.3 for comma three: fix display init at high temperatures
  * Improved auto-exposure on comma three
  * Honda Accord 2021 support thanks to csouers!
  * Honda Accord Hybrid 2021 support thanks to csouers!
  * Hyundai Kona Hybrid 2020 support thanks to haram-KONA!
  * Hyundai Sonata Hybrid 2021 support thanks to Matt-Wash-Burn!
  * Kia Niro Hybrid 2021 support thanks to tetious!

2021-08-21
==========
* Merge upstream master (0.8.8) / @martinl

2021-08-15
==========
* FPv2 updates
  * 2018 Impreza Limited - UDM / @isaacdchan

2021-08-14
==========
* FPv2 updates
  * 2020 Ascent - UDM / @ndtran

2021-08-04
==========
* Merge upstream (0.8.7) / @martinl
* FPv2 updates
  * 2018 Forester - UDM / @sarvcomp

2021-08-03
==========
* FPv2 updates
  * 2021 Crosstrek Limited - UDM / @AdamSLevy

2021-08-02
==========
* Removed last remaining Subaru FPv1 fingerprints / @martinl
* Minor carstate signal fixes / @martinl

2021-08-01
==========
* Add Legacy 2018+ as separate model, has flipped triver torque signal / @martinl

2021-07-31
==========
* Update LKAS alert filtering for Outback 2020+ and Forester 2021+ / @martinl

2021-07-29
==========
* FPv2 updates
  * 2020 Forester Sport - UDM / @RyanYo

2021-07-26
==========
* FPv2 updates
  * 2018 Crosstrek - UDM / @dnewstat

2021-07-25
==========
* FPv2 updates
  * 2019 Outback - UDM / @Steven C

2021-07-24
==========
* Merge upstream (0.8.6) / @martinl
* Stop and go manual hold support for Global EPB models / @martinl
* Use alternative steering signal for WRX / @martinl
* FPv2 updates
  * 2015 Outback - UDM / @chk_null

2021-07-21
==========
* FPv2 updates
  * 2021 Forester - UDM / @umby24

2021-07-14
==========
* FPv2 updates
  * 2015 Outback 3.6R - UDM / @bitwaster

2021-07-12
==========
* FPv2 updates
  * 2020 Outback 2.4 Touring XT  - UDM / @chrissantamaria
  * 2021 Ascent - UDM / @Sandy

2021-07-10
==========
* FPv2 updates
  * 2020 Outback 2.4 XT Limited - UDM / @KingChalupa
* Disable LKAS alert filtering for Outback 2020

2021-07-07
==========
* FPv2 updates
  * 2017 Impreza - UDM (@Fidel)
  * 2019 Outback Touring 3.6R - UDM (@danyo)
  * 2020 Impreza Premium - UDM (@KeetsScrimalittle)
  * 2020 Forester - UDM / (@TH156UY)

2021-07-06
==========
* Stop and Go support for preglobal Forester, Levorg and WRX (@martinl)

2021-07-04
==========
* Levorg 2016 support (@jpgnz)

2021-07-02
==========
* Removed ASCENT, IMPREZA, OUTBACK FPv1 due to car identification issues (@martinl)

2021-07-01
==========
* FPv2 updates
  * 2019 Forester - UDM (@clockenessmnstr)
  * 2021 Forester - UDM (@gotham)

2021-06-28
==========
* Crosstrek Hybrid 2020 support (WIP) (@martinl)

2021-06-27
==========
* Outback 2020 support (WIP) (@martinl)
* Disable Openpilot disengage on gas press via toggle (@sshane)

2021-06-26
==========
* New subaru-community branch based on subaru-PR-test
* Stock LKAS alerts filtering when openpilot is enabled (@trailtacos)
* Subaru Stop and Go (both EPB and experimental MPB via toggle) (@letsdudiss)
* New ACC set speed unit signals for Global and Pre-global models (@martinl)
