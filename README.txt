# Indo-European Good Enough Tree

This repository contains data and scripts for producing a Baysian phylogenetic tree sample of for the Indo-European family which is *good enough* for use in phylogenetic comparative methods. There are persistent rumours that something better will be available soon, but in the meantime, this is the best we can do.

Design principles

- The cognate coding is borrowed from Andrew Garrett's corrections of the IELex database (published in supplementary materials to Chang et al. 2015).
- Generated with standard BEAST2 (no customisation). This means we cannot use the Chang et al 2015 notion of ancestry constraints (and there are theoretical and empirical reasons that make these controversial in any case).
- Ultimately we will offer control files generated using the beastling package (Maurits et al. 2017), which would make it very easy for users to change data and model settings; unfortunately we have found some bugs in the current iteration of beastling which makes it unsuitable. 

The "Broad data set":

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

## Tree samples

### IE-trees-v1

The control file IE-trees-v1/ie-v1.xml was made manually by Tiago Tresoldi. The model was built in BEAUTi, following the parameters of the original beastling configuration. We use a Binary Covarion model for a coalescent tree with constant population. Missing data is encoded as `?`; we only used concepts that had at least 90% coverage across the doculects. Concepts were divided in four different partitions, each with its individual site model, with each partition holding roughly the same number of concepts each and concept divided by the cardinality of their corresponding sets of individual cognate sets (25%, 50%, 75%, and 100% percentiles). We used a chain length of 10^8 and a burn-in of XXX %. The tree includes multimonophyletic constraints, as given in the corresponding Newick tree, and date calibrations for both tips and splits as follows:

(list of calibrations)

## References

Maurits, Luke, Robert Forkel, Gereon A. Kaiping, and Quentin D. Atkinson. 2017. “BEASTling: A Software Tool for Linguistic Phylogenetics Using BEAST 2.” PLOS ONE 12 (8): e0180908. https://doi.org/10.1371/journal.pone.0180908.

<!--
vim:ft=markdown
-->
