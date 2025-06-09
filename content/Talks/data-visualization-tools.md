Title: A Constellation of Data Visualization Tools
Date: 2022-06-23
Category: Talks
Tags: data-visualization, vega, vega-lite, altair
Slug: 2022/06/23/data-visualization-tools

I gave a short talk today called *A Constellation of Data Visualization Tools: Vega, Vega-Lite, and Altair*.

The first part of the talk was a brief history of data visualization tools.
I described how the ideas in Leland Wilkinson's *The Grammar of Graphics* are related to
those in ggplot2;
and those in D3.js, Vega, Vega-Lite, and Altair.

The second part of the talk was a demonstration of Vega, Vega-Lite, and Altair.
Using the editor and the examples,
I showed
that the JSON objects of a Vega specification are transformed into WebGL or SVG graphics by the runtime;
that the JSON objects of a Vega-Lite specification are transformed into the JSON objects of a Vega specification by the runtime;
and that the Python objects produced by Altair are serialized into the JSON objects of a Vega-Lite specification.

The third part of the talk related Vega, Vega-Lite, and Altair to the [Bennett Institute][] and [OpenSAFELY][].
Vega and Vega-Lite specifications are well suited to manual (human) and automated (machine) output checking.
They can be themed,
so a house style can be developed by a designer and applied by a researcher.
Finally, they have expressive power and are effective:
the former means they are capable of generating a large variety and quantity of ideas;
the latter means they perform well,
when compared to other notations,
on the *cognitive dimensions of notations* framework.

[Bennett Institute]: https://www.bennett.ox.ac.uk/
[OpenSAFELY]: https://www.opensafely.org/
