The beast xml control files to produce this sample was made by Tiago Tresoldi using the beauti tool in August 2021.

Calibrations are derived from Chang et al. 2015 (for calibrations of individual languages; 0-50 year calibrations on the modern languages are *not* included) and Bouckaert et al. 2012 (for the family level calibrations)

### Chang et al. 2015 calibrations

- Old_Irish = 1100 - 1300
- Cornish = 200 - 400
- Latin = 2100 - 2200
- Gothic = 1625 - 1675
- Old_West_Norse = 750 - 850
- Old_English = 950 - 1050
- Old_High_German = 1100 - 1200
- Ancient_Greek = 2400 - 2500
- Classical_Armenian = 1500 - 1600
- Old_Prussian = 500 - 600
- Old_Church_Slavic = 950 - 1050
- Avestan = 2450 - 2550
- Sogdian = 1200 - 1400
- Vedic_Sanskrit = 3000 - 3500
- Tocharian_A = 1200 - 1500
- Tocharian_B = 1200 - 1500
- Hittite = 3300 - 3500

### Bouckaert et al. 2012 calibrations

- Latvian, Lithuanian = normal(1350.0,25.0)
- Balto_Slavic = normal(3100.0,600.0)
  # XXX Balto_Slavic distribution should be truncated from 2000-3400
- Northwest_Germanic = normal(1875.0,67.0)
- Indo_Iranian = 3000 - 10000
- Iranian = 2600 + rlognormal(400.0,0.8)
- Tocharic = 1650 + rlognormal(200.0,0.9)
- West_Germanic = normal(1550.0,25.0)
- French_Iberian = normal(1400.0,100.0)
- Indic = 2150 + rlognormal(1000.0,1.0)
- Celtic = 1200 + rlognormal(2000.0,0.6)
- Latin_Romance = normal(2000.0,135.0)
- Slavic = 1200 + rlognormal(300.0,0.6)
- originate(Brythonic) = normal(1500.0,25.0)
- Greek_split = > 2500
