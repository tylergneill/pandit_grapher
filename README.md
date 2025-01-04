# Pandit Grapher

Graphs person-work and work-work relationships in the [Pandit Prosophographical Database of Indic Texts](https://www.panditproject.org/).

This can be useful both for exploring certain persons or works of interest and for more quickly finding Pandit items in need of improvement.

# Web app

Currently deployed at https://pandit-grapher-poc.dharma.cl/

# Offline mode

It's also possible to use the backend code locally to produce graph data for use with e.g. [Gephi](https://gephi.org/).
Resulting graphs are created in memory, (optionally) drawn to the screen with `networkx`, and also (optionally) output for Gephi.
This makes it feasible to visualize the entire graph at once, among other things.
More details, see <a href="https://github.com/tylergneill/pandit_grapher/tree/main/offline_mode.md">offline_mode.md</a>.

# Feedback, License

Get in touch! Let me know if this is useful, whether you'd like changes, etc. 
And do please share and share alike: licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).