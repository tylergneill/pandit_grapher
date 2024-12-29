# Pandit Grapher

Graphs person-work and work-work relationships in the [Pandit Prosophographical Database of Indic Texts](https://www.panditproject.org/).

This can be useful both for exploring certain persons or works of interest and for more quickly finding Pandit items in need of improvement.

# Web app

Currently deployed at https://pandit-grapher-poc.dharma.cl/

# Requirements

For the web app, simply use a modern browser.

It's also possible to use the backend code locally to produce graph data for use with e.g. [Gephi](https://gephi.org/). See requirements files for needed Python (3) libraries.
Resulting graphs are created in memory, (optionally) drawn to the screen with `networkx`, and also (optionally) output for Gephi.
More details on this are available <a href="https://github.com/tylergneill/pandit_grapher/tree/v2/local_use_manual.md">here</a> (caveat: needs updating!)

# Feedback, License

Get in touch! Let me know if this is useful, whether you'd like changes, etc. 
And do please share and share alike: licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).