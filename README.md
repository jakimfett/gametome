gametome
========

Repo for the Linux Game Tome project, working towards the resurrection of happypenguin.org

Join the discussion on the forum at [http://happypenguin.onkoistudios.com/](http://happypenguin.onkoistudios.com/), or on the freenode IRC at #gametome (or via the [web client](http://webchat.freenode.net/?channels=gametome&uio=d4) ).

The database dump can be downloaded from [http://happypenguin.onkoistudios.com/uploads/happypenguin_dump.tar.bz2](http://happypenguin.onkoistudios.com/uploads/happypenguin_dump.tar.bz2)

grigis attempt
--------------

For this I tried to focus on a more basic version. It uses Bootstrap so I want to later on try and skin it using michealbs sepia TLGT-inspired theme. Right now I'm more focused on functionality, so we can do usability testing as soon as possible.

What currently works:

* Registering/validating EMail/using federated/social auth/associating to multiple accounts
* Basic Bootstrap interface
* A working rich text editor
* Import of legact Game records:
    * Handling:
        * title, description, shortdescription, submittedby, createddate, updateddate, cost, version
        * Licence and capabilities is imported as tags
        * description is run through an HTML sanitizer
        * ratings are imported as reviews with no body (Not sure about this, should reviews and ratings be separate entities, or ratings ae reviews?)
    * Not Handling:
        * Image importing
        * approvals
        * company/author (want to create a new page for that)
        * 'other' -> not even sure what this is
* Import of legacy News records:
    * Handling:
        * headline,news,user,timestamp
        * extract category and short description from html blob
        * removed category/description/rating from html blob
        * run news through HTMl sanitizer
        * newstype and category imported as tags
    * Not Handling:
        * link to game
* Import of legacy Comments:
    * Handling:  
        * subjext, comment, user, timestamp
        * comment is run through an HTML sanitizer
        * sub-comments
    * Not Handling:
        * spam detection

What still needs to be done:

* Implementing Game & News pages and threaded comments
* Sanitized rich-text entry system
* Content rating system (to combat trolling)
* Spam detection
* Fulltext search (plan to use Haystack and Woosh)
* I18N and L10N
* Live data editing for your own content (or if you got given proxy rights) to make maintaining data easier
* Author/Company page
* A proper theme
* Usability testing

To get the initial data:

* Download bobz's database dump archive ~400 MB 
* Untar it to some handy location (I untarred it to ./data, so that there exists a directory ./data/screenshots)
* Download grigi's de-normalized JSON version of the DB. Unzip it to the same location. [GET IT HERE](http://happypenguin.onkoistudios.com/discussion/5/de-normalized-db#Item_2)

To get started:

* Setup a python environment (preferably a virtualenv)
* `pip install django-ckeditor django-taggit django-allauth` - install requirements
* `./manage.py syncdb` - default dev config uses a local sqlite database
* `./manage.py importhp` - import the legacy data
* `./manage.py runserver` - development server

Code-level priorities for the project:

* Dependancies should work in Python3 or have a in-progress plan to migrate to it
* Code should be kept as simple as possible, and have a reasonable amount of tests
* Care should be taken to keep an eye on performance


