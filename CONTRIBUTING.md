# Contributing

We appreciate all contributions to this project, whether they are simple questions or full-fledged pull requests.

Your contribution may fall into one of the following categories:

1. You have a question or an idea.
2. You believe you may have found a bug, including unexpected behavior.
3. You want to make changes to the codebase, such as fixing a bug, adding a new feature, or updating documentation.

Below are the steps to take for each category:

## Asking a question or suggesting an idea

1. Check the [Discussions](https://github.com/dralshehri/hijridate/discussions) section to see if someone else has already posted a similar question or idea.
2. If your search did not yield any relevant results, **start a new discussion** within the relevant category.

## Reporting a bug or an issue

1. Check the [Issues](https://github.com/dralshehri/hijridate/issues) section to see if someone else has already raised the same issue.
2. If your search did not yield any relevant results, **create a new issue**.
3. Ensure you provide enough information to help the community understand the cause and context of the problem. Depending on the issue, you may want to include:
   - The version number of the release causing the problem.
   - Detailed information about the use case and unexpected behavior.
   - Information about the operating system.
4. Apply relevant labels to the newly created issue.

## Making a change to the codebase or documentation

1. Make sure you are familiar with [forking a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) on GitHub.
2. Prepare your local machine by [installing Hatch](https://hatch.pypa.io/latest/install/).
3. After forking the project, run the command `hatch env create` to create the virtual environment.
4. Before committing changes, run the command `hatch run checks` to ensure all checks pass, including formatting, linting, typing, and tests with coverage.
5. Once you have pushed changes to your fork, you can create a pull request.

If you believe that you have made a significant contribution to this project but do not know how to write tests, run them, or generate documentation, do not let this discourage you from submitting a pull request. We are here to help you out! Simply submit the pull request, but keep in mind that you might be requested to add more commits to your pull request.
