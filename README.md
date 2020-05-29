## Recipe website

### Contents
This repository contains the guts of our home recipe website - web presentation, and useful utilities needed to go from one to the other. Utilities that are required for Django are included here. Critically the database containing any contents is _not_ included

### Structure
For this first pass, ~~recipes are stored in the [Open Recipe Format](https://open-recipe-format.readthedocs.io/en/latest/) where possible.~~ The 'spec' isn't exactly widespread, so I've ~~taken some liberties here and there~~ basically thrown it out but kept useful bits. ~~The recipe format is specified [here](https://open-recipe-format.readthedocs.io/en/latest/topics/reference/orf.html). Nutritional information will be linked using the [associated format](https://open-recipe-format.readthedocs.io/en/latest/topics/reference/onf.html).~~ Attribution will always be given where possible.

_HEAVILY_ inspired by https://realpython.com/get-started-with-django-1/, used under the MIT license at https://github.com/realpython/materials/blob/master/LICENSE



The web interface will then store recipes using the Django database, and hopefully this will provide (1) a useful framework to learn Django, and (2) a good way to archive recipes around the house. (To be fair, the old 'noteboook and pen' method is pretty good, too...)
