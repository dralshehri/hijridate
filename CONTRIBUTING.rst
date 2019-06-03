Contributing
------------

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Reporting Issues
~~~~~~~~~~~~~~~~

An issue may be a simple comment, question, feature request, or bug report. When
`reporting an issue <https://github.com/dralshehri/hijri-converter/issues>`__,
please make sure to provide enough information to understand it. Depending on
the issue, you may want to include:

* Package version.
* Information about the operating system.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Don't forget to apply relevant labels to the newly created issue.

Development
~~~~~~~~~~~

You may want to make some kind of change to the code base (e.g. to fix a bug,
to add a new feature, to update documentation). The steps below explain how:

#. Announce your plan to the rest of the community **before you start**
   **working**. This announcement should be in the form of a (new) issue.
#. Wait until you get a feedback about your idea being a good idea.
#. If needed, fork the repository to your own Github profile and create your
   own feature branch off of the latest master commit. While working on your
   feature branch, make sure to stay up to date with the master branch by
   pulling in changes, possibly from the 'upstream' repository
   (follow the instructions
   `here <https://help.github.com/articles/configuring-a-remote-for-a-fork/>`__
   and `here <https://help.github.com/articles/syncing-a-fork/>`__).
#. Before coding on your local machine, make sure to run ``make install`` to
   create a virtual environment and install development dependencies. Then
   activate the environment by running ``source .venv/bin/activate``.
#. Make sure the existing tests still work by running ``make test``.
#. Add your own tests (if necessary) and check the code coverage by running
   ``make test-cov``.
#. Before committing changes, make sure to apply code styling by running
   ``make format``.
#. Update or expand the documentation.
#. Push your feature branch to (your fork of) the Hijri Converter repository
   on GitHub (you can follow the instructions
   `here <https://help.github.com/en/articles/pushing-to-a-remote/>`__).
#. Create the pull request, e.g. following the instructions
   `here <https://help.github.com/articles/creating-a-pull-request/>`__.

In case you feel like you've made a valuable contribution, but you don't know
how to write or run tests for it, or how to generate the documentation: don't
let this discourage you from making the pull request; I can help you! Just go
ahead and submit the pull request, but keep in mind that you might be asked to
append additional commits to your pull request.
