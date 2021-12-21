# Cryptic Conventions

 Please use English for all Cryptic-related GitHub posts (in issues, pull requests, commits, etc) and follow the conventions below to ensure a clear and uniform style.

## Branch Naming

The master (or main) branch contains the actual version. New commits to are only added via pull requests which requires two approvals. Learn more about [GitHub branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches).

**Feature branches** contain one or more commits to address one related feature or issue. Prefix your feature branch with `issue/issue-id` before you add the actual branch name. Example: `issue/\<id\>-\<add-my-feature\>`. To update any project dependencies, name your branch like `dependencies/\<dependencies-name\>`.

## Commit Messages

Write short (< 50 characters) **commit messages** in English and use the scheme `<message> (#<issue-id>)`. Do not use just `<em>bug fix</em>` but useful text. Hotfixes and merge commits.

The commit message that fixes any merge conflicts in your feature branch (after you have merged master into your branch) should be `Solved merge conflicts for #<pull-request-id>`.

### Merging Branches

To merge a feature branch into master, use the option **merge** (not squash or rebase) to create a merge commit.

## Issues and Pull Requests

- **Title**: Shortly summarize the content but avoid special characters.
- **Content/Description**: Add more information to the issue or pull request.

When submitting an issue or pull request, fill out all other information requested in these predefined templates:

- [Bug Report](https://github.com/cryptic-game/cryptic/blob/master/.github/ISSUE_TEMPLATE/BUG_REPORT.md)
- [Feature Request](https://github.com/cryptic-game/cryptic/blob/master/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.md)
- [Pull Request Template](https://github.com/cryptic-game/cryptic/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

## Release Versioning / Hotfixes

For releases, we follow [Semantic Versioning 2.0.0](https://semver.org/).

Heads (or Head Assistants) can create/approve hotfixes for severe/security-related issues to address quick fixes. Such commits should use the naming scheme: `Hotfix: <message>` (z.B. `Hotfix: Changed foo bar`). Create a new branch from a release-tag and name the new release as `<old-release-name>.x` - each hotfix for a release increases x by 1, e.g. `v0.3.1-pre-alpha.2`.

## Code Style

- Java: Follow the general [Java Code Conventions](https://www.oracle.com/technetwork/java/codeconventions-150003.pdf)
- Python: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some exceptions:
    - As Autoformatter, use [PyCharm](https://www.jetbrains.com/pycharm/) (preferred) or [black](https://github.com/python/black).
    - Max line length: 120 characters.
    - Remove unnecessary blank lines but keep one blank line at the end of each file.
    - Use typing except for obvious types (e.g. `foo = "bar"`).
- Angular: Follow the [Angular Coding Style Guide](https://angular.io/guide/styleguide).

### Naming variables and functions

Follow [grammar based naming conventions](https://dev.to/somedood/a-grammar-based-naming-convention-13jf) with some exceptions:
- Name functions using *snake\_case*.
- Do not use the *is-* prefix for *bool* typed variables.

Add any exceptions with `# noinspection PyPep8Naming` and a comment. <!-- check and change if required -->If classes are saved as variable, e.g. `self.Session: sessionmaker = sessionmaker(...)`.

We recommend [WebStorm ](https://www.jetbrains.com/webstorm/) (free for pupils/students) or [Visual Studio Code](https://code.visualstudio.com/) as development environment. Additionally, use [TSLint](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin) and [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig). For Webstorm, use [Karma](https://plugins.jetbrains.com/plugin/7287-karma).
