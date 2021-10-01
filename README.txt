# Indo-European Good Enough Tree

This repository contains data and scripts for producing a Baysian phylogenetic tree sample of for the Indo-European family which is *good enough* for use in phylogenetic comparative methods. There are persistent rumours that something better will be available soon, but in the meantime, this is the best we can do.

Design principles

- The cognate coding is borrowed from Andrew Garrett's corrections of the IELex database (published in supplementary materials to Chang et al. 2015).
- Generated with standard BEAST2 (no customisation) using the beastling package (Maurits XXXX) to generate the control files. This means we cannot use the Chang et al 2015 notion of ancestry constraints (and there are theoretical and empirical reasons that make these controversial in any case)

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

## Clade constraints

Chang et al. 2015 use the following clade constraints:

Nuclear Indo-European: all languages other than Anatolian 
Inner Indo-European: all languages other than Anatolian and Tocharian 
Balto-Slavic: Baltic + Slavic Baltic: Old Prussian + East Baltic 
East Baltic: Latvian, Lithuanian Slavic: East + South + West Slavic 
West Slavic: Czech, Slovak, Polish, Upper Sorbian, Lower Sorbian 
East Slavic: Russian, Belarusian, Ukrainian 
South Slavic: Old Church Slavic, Serbian, Bulgarian, Macedonian, Slovenian 
Germanic: Gothic, North Germanic, West Germanic 
West Germanic: High German + English, Frisian, Dutch, Flemish, Afrikaans 
High German: Old High German, German, Swiss German, Luxembourgish 
English: Old English, Modern English 
North Germanic: East + West Scandinavian 
East Scandinavian: Danish, Swedish 
West Scandinavian: Old West Norse, Icelandic, Faroese, Norwegian 
Indo-Iranian: Indic + Iranian Indic: Vedic Sanskrit, Indo-Aryan 
Indo-Aryan: all the modern Indo-Aryan languages 
Iranian: Avestan + the Pashto group + the Persian group + all other Iranian languages 
Persian group: Persian, Tajik 
Pashto group: Pashto, Waziri Italo-Celtic: Italic + Celtic 
Celtic: British Celtic, Goidelic 
British Celtic: Cornish, Breton, 
Welsh Goidelic: Old Irish, Modern Irish, Scots Gaelic 
Italic: Latin + Romance 
Romance: Sardinian + Continental Romance 
Continental Romance: Eastern Romance + Italo-Western Romance 
Eastern Romance: Romanian, Arumanian 
Italo-Western Romance: all Romance varieties other than Sardinian and Eastern Romance 
Albanian: Arvanitika, Tosk 
Armenian: Classical Armenian, Modern Armenian 
Modern Armenian: Adapazar, Eastern Armenian 
Greek: Ancient Greek, Modern Greek

## Notes

beastling configuration seems to ignore the `sample_from_prior=True` setting in
the `[MCMC]` block. As a workaround, either (i) manually add
`sampleFromPrior="true"` to the attributes of the `<run` block in the xml
control file, or (ii) use the `-sampleFromPrior` option when you invoke `beast`
to do the analysis.

<!--
vim:ft=markdown
-->
