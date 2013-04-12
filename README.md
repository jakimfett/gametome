gametome
========

Repo for the Linux Game Tome project, working towards the resurrection of happypenguin.org

Join the discussion on the forum at [http://happypenguin.onkoistudios.com/][http://happypenguin.onkoistudios.com/], or on the freenode IRC at #gametome (or via the [web client][http://webchat.freenode.net/?channels=gametome&uio=d4]).

The database dump can be downloaded from [http://happypenguin.onkoistudios.com/uploads/happypenguin_dump.tar.bz2][http://happypenguin.onkoistudios.com/uploads/happypenguin_dump.tar.bz2]

grigis attempt
--------------

For this I tried to focus on a more basic version. It uses Bootstrap so I want to later on try and skin it using michealbs sepia TLGT-inspired theme. Right now I'm more focused on functionality, so we can do usability testing as soon as possible.

What currently works:
* Registering/validating EMail/using federated/social auth/associating to multiple accounts
* Basic Bootstrap interface
* A working rich text editor
* Importing of most of the legacy TLGT data into models (accessible only through the admin interface right now)

What still needs to be done:
* Implementing Game & News pages and threaded comments
* Sanitation of user-entered rich text (plan to use html5lib)
* Content rating system (to combat trolling)
* Spam detection
* Fulltext search (plan to use Haystack and Woosh)
* I18N and L10N
* Live data editing for your own content (or if you got given proxy rights) to make maintaining data easier
* Author/Company page
* A proper theme
* Usability testing

To get the initial data:
1. Download bobz's database dump archive ~400 MB 
2. Untar it to some handy location (I untarred it to ./data, so that there exists a directory ./data/screenshots)
3. Download grigi's de-normalized JSON version of the DB. Unzip it to the same location. [GET IT HERE](http://happypenguin.onkoistudios.com/discussion/5/de-normalized-db#Item_2)


