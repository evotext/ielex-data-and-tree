# Indo-European Good Enough Tree

This repository contains data and scripts for producing a Baysian phylogenetic tree sample of for the Indo-European family which is *good enough* for use in phylogenetic comparative methods. There are persistent rumours that something better will be available soon, but in the meantime, this is the best we can do.

## Design principles

- The cognate coding is borrowed from Andrew Garrett's corrections of the IELex database (published in supplementary materials to Chang et al. 2015).
- Generated with standard BEAST2 (no customisation). This means we cannot use the Chang et al 2015 notion of ancestry constraints (and there are theoretical and empirical reasons that make these controversial in any case).
- Ultimately we will offer control files generated using the beastling package (Maurits et al. 2017), which would make it very easy for users to change data and model settings; unfortunately we have found some bugs in the current iteration of beastling which makes it unsuitable. 

## The "Broad data set"

- Use the Bouckaert et al. 2013 language sample minus sparsly attested languages (following Chang et al 2015). This is a tradeoff between quality of the wordlist and quantity of languages in the sample. 
- Slightly truncated meaning list:

    The broad data set consists of ninety-four languages and 197 meaning
    classes.  Of the 207 meaning classes in IELEX, three (‘blow’, ‘father’,
    ‘mother’) were excluded as being especially susceptible to sound symbolism,
    and seven others were excluded because they were unattested in more than
    30% of the languages, probably due to the fact that they are not in the
    Dyen data set, which was constructed around the 200 items proposed by
    Swadesh (1952).  (Chang et al 2015:213)

  Dropped meanings are: blow breast father fingernail full horn knee moon mother round

## Calibrations

Calibrations are derived from Chang et al. 2015 (for calibrations of individual languages; 0-50 year calibrations on the modern languages are *not* included) and Bouckaert et al. 2012 (for the family level calibrations). These are listed in beastling-compatible format ("X - Y" indicates a uniform distribution between X and Y; for normal and rlognormal the first parameter is the mean and second parameter is standard deviation)

Chang et al. 2015 calibrations:

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

Bouckaert et al. 2012 calibrations:

- Latvian, Lithuanian = normal(1350.0,25.0)
- Balto_Slavic = normal(3100.0,600.0)
 
  [ XXX Balto_Slavic distribution should be truncated from 2000-3400]
  
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

## Tree samples

### IE-trees-v1

The control file IE-trees-v1/ie-v1.xml was made manually by Tiago Tresoldi. The model was built in BEAUTi, following the parameters of the original beastling configuration. We use a Binary Covarion model for a coalescent tree with constant population. Missing data is encoded as `?`; we only used concepts that had at least 90% coverage across the doculects. Concepts were divided in four different partitions, each with its individual site model, with each partition holding roughly the same number of concepts each and concept divided by the cardinality of their corresponding sets of individual cognate sets (25%, 50%, 75%, and 100% percentiles). We used a chain length of 10^8 and a burn-in of 50%. The tree includes multimonophyletic constraints, as given in the corresponding Newick tree, and date calibrations for both tips and splits as given above.

## References

Maurits, Luke, Robert Forkel, Gereon A. Kaiping, and Quentin D. Atkinson. 2017. “BEASTling: A Software Tool for Linguistic Phylogenetics Using BEAST 2.” PLOS ONE 12 (8): e0180908. https://doi.org/10.1371/journal.pone.0180908.

<!--
vim:ft=markdown
-->
