# Indo-European Good Enough Tree

This repository contains data and scripts for producing a Baysian phylogenetic tree sample of for the Indo-European family which is *good enough* for use in phylogenetic comparative methods. There are persistent rumours that something better will be available soon, but in the meantime, this is the best we can do.

## Design principles

- The cognate coding is borrowed from Andrew Garrett's corrections of the IELex database (published in supplementary materials to Chang et al. 2015).
- Generated with standard BEAST2, without further customisation (Bouckaert et al., 2019). This means we cannot use the Chang et al 2015 notion of ancestry constraints (and there are theoretical and empirical reasons that make these controversial in any case).
- Ultimately we will offer control files generated using the beastling package (Maurits et al. 2017), which would make it very easy for users to change data and model settings; unfortunately we have found some bugs in the current iteration of beastling which makes it unsuitable. 

## The "Broad data set"

- Use the Bouckaert et al. (2012) language sample minus sparsly attested languages, following Chang et al. (2015). This is a tradeoff between quality of the wordlist and quantity of languages in the sample. 
- Slightly truncated meaning list:

    The broad data set consists of ninety-four languages and 197 meaning
    classes.  Of the 207 meaning classes in IELEX, three (‘blow’, ‘father’,
    ‘mother’) were excluded as being especially susceptible to sound symbolism,
    and seven others were excluded because they were unattested in more than
    30% of the languages, probably due to the fact that they are not in the
    Dyen data set, which was constructed around the 200 items proposed by
    Swadesh (1952).  (Chang et al 2015:213)

  Dropped meanings are: "blow", "breast", "father", "fingernail", "full", "horn", "knee",
    "moon", "mother", "round".

## Calibrations

Calibrations are derived from Chang et al. (2015) for individual languages (but 0-50 year calibrations on the modern languages are *not* included) and Bouckaert et al. (2012) for the family level calibrations. These are listed in `beastling`-compatible format ("X - Y" indicates a uniform distribution between X and Y; for `normal` and `rlognormal` the first parameter is the mean and second parameter is standard deviation).

| Language/Clade       | Calibration                    | Source                  |
|----------------------|--------------------------------|-------------------------|
| Old Irish            | 1100-1300                      | Chang et al. (2015)     |
| Cornish              | 200-400                        | Chang et al. (2015)     |
| Latin                | 2100-2200                      | Chang et al. (2015)     |
| Gothic               | 1625-1675                      | Chang et al. (2015)     |
| Old West Norse       | 750-850                        | Chang et al. (2015)     |
| Old English          | 900-1050                       | Chang et al. (2015)     |
| Old High German      | 1100-1200                      | Chang et al. (2015)     |
| Ancient Greek        | 2400-2500                      | Chang et al. (2015)     |
| Classical Armenian   | 1500-1600                      | Chang et al. (2015)     |
| Old Prussian         | 500-600                        | Chang et al. (2015)     |
| Old Church Slavic    | 950-1050                       | Chang et al. (2015)     |
| Avestan              | 2450-2550                      | Chang et al. (2015)     |
| Sogdian              | 1200-1400                      | Chang et al. (2015)     |
| Vedic Sanskrit       | 3000-3500                      | Chang et al. (2015)     |
| Tocharian A          | 1200-1500                      | Chang et al. (2015)     |
| Tocharian B          | 1200-1500                      | Chang et al. (2015)     |
| Hittite              | 3300-3500                      | Chang et al. (2015)     |
| Latvian, Lithuanian  | normal(1350.0, 25.0)           | Bouckaert et al. (2012) |
| Balto Slavic         | normal(3100.0, 600.0)          | Bouckaert et al. (2012) |
| Northwest Germanic   | normal(1875.0, 67.0)           | Bouckaert et al. (2012) |
| Indo-Iranian         | 3000-10000                     | Bouckaert et al. (2012) |
| Iranian              | 2600 + rlognormal(400.0, 0.8)  | Bouckaert et al. (2012) |
| Tocharic             | 1650 + rlognormal(200.0, 0.9)  | Bouckaert et al. (2012) |
| West Germanic        | normal(1550.0, 25.0)           | Bouckaert et al. (2012) |
| French Iberian       | normal(1400.0, 100.0)          | Bouckaert et al. (2012) |
| Indic                | 2150 + rlognormal(1000.0, 1.0) | Bouckaert et al. (2012) |
| Celtic               | 1200 + rlognormal(2000.0, 0.6) | Bouckaert et al. (2012) |
| Latin Romance        | normal(2000.0, 135.0)          | Bouckaert et al. (2012) |
| Slavic               | 1200 + rlognormal(300.0, 0.6)  | Bouckaert et al. (2012) |
| originate(Brythonic) | normal(1500.0, 25.0)           | Bouckaert et al. (2012) |
| Greek split          | > 2500.0                       | Bouckaert et al. (2012) |

## Tree samples

### IE-trees-v1

The control file IE-trees-v1/ie-v1.xml was made manually by Tiago Tresoldi, following as close as possible the model generated by `beastling`. The model was built in BEAUTi, following the parameters of the original beastling configuration. We use a Binary Covarion model for a coalescent tree with constant population. Missing data is encoded as `?`; we only used concepts that had at least 90% coverage across the doculects. Concepts were divided in four different partitions, each with its individual site model, with each partition holding roughly the same number of concepts each and concept divided by the cardinality of their corresponding sets of individual cognate sets (25%, 50%, 75%, and 100% percentiles). We used a chain length of 10^8 and a burn-in of 50%. The tree includes multimonophyletic constraints, as given in the corresponding Newick tree, and date calibrations for both tips and splits as given above.

## References

Bouckaert RR, Lemey P, Dunn M, Greenhill SJ, Alekseyenko AV, Drummond AJ, Gray RD, Suchard MA & Atkinson QD. 2012. Mapping the Origins and Expansion of the Indo-European Language Family. Science, 337(6097), 957-960.

Bouckaert R., Vaughan T.G., Barido-Sottani J., Duchêne S., Fourment M., Gavryushkina A., et al. (2019) BEAST 2.5: An advanced software platform for Bayesian evolutionary analysis. PLoS computational biology, 15(4), e1006650.

Chang W, Cathcart C, Hall D, & Garrett A. 2015. Ancestry-constrained phylogenetic analysis supports the Indo-European steppe hypothesis. Language, 91(1):194-244.

Maurits, Luke, Robert Forkel, Gereon A. Kaiping, and Quentin D. Atkinson. 2017. “BEASTling: A Software Tool for Linguistic Phylogenetics Using BEAST 2.” PLOS ONE 12 (8): e0180908. https://doi.org/10.1371/journal.pone.0180908.

<!--
vim:ft=markdown
-->