# Cryptic Conventions

Follow these conventions to ensure a clear and uniform style. 

In general, please use English for all Cryptic-related GitHub posts (in issues, pull requests, commits, etc).

## Branches

- **master**: Contains the actual version. New commits are only added via pull request merges.
- **issue/\<id\>-\<name\>**: Feature branches contain one or more commits to address the related issue (e.g. `issue/42-add-foo-bar`).
- **dependencies/\<dependencies-name\>**: Branches to update dependencies. 

Any submitted pull request requires two approvals (from Quality Management and the department's Head (Assistant).

## Templates (issues/pull requests)

- [Bug Report](https://github.com/cryptic-game/cryptic/blob/master/.github/ISSUE_TEMPLATE/BUG_REPORT.md)
- [Feature Request](https://github.com/cryptic-game/cryptic/blob/master/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.md)
- [Pull Request Template](https://github.com/cryptic-game/cryptic/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

Some notes for issues and pull requests:  

- **Issue/Pull Request title**: Shortly summarizes the content. Avoid special characters.
- **Issue/ Pull Request content**: Adds more information for the issue/pull request. Fill out all fields predefined by the issue template. In pull requests, add an issue id/link.
- **Commit Messages**: Use the scheme `<message> (#<issue-id>)`. Use English for the message. The message must be short (< 50 characters) and contain useful text. Do not use just `<em>bug fix</em>`.Execeptions are hotfixes and merge commits.
- **Merge Commits**: For commits from a feature branch into master, use the merge option, not squash or rebase. 
- **Merge Conflicts**: Fix any merge conflicts in a feature branch (which can appear when you want to merge into master) by merging master into your feature branch. The commit message should be named `Solved merge conflicts for #<pull-request-id>`.

## Release Versioning / Hotfixes

For releases, we follow [Semantic Versioning 2.0.0](https://semver.org/).

Heads (or Head Asistants) can create/approve hotfixes for severe/security-related issues to address quick fixes. Such commits should use the naming scheme: `Hotfix: <message>` (z.B. `Hotfix: Changed foo bar`). Create a new branch from a release-tag and name the new release as `<old-release-name>.x` - each hotfix for a release increases x by 1, e.g. `v0.3.1-pre-alpha.2`.

## Code Style

- Java: Follow the general [Java Code Conventions](https://www.oracle.com/technetwork/java/codeconventions-150003.pdf)
- Python: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some exceptions:
    - As Autoformatter, use [PyCharm](https://www.jetbrains.com/pycharm/) (preferred) or [black](https://github.com/python/black).
    - Max line length: 120 characters. 
    - Remove unnecessary blank lines but keep one blank line at the end of each file.
    - Use typing except for obvious types (e.g. `foo = "bar"`)
- Angular: Follow the [Angular Coding Style Guide](https://angular.io/guide/styleguide). 

Naming conventions for variables and functions:  

Follow [grammar based naming conventions](https://dev.to/somedood/a-grammar-based-naming-convention-13jf) with some exceptions: 
- Name functions using *snake\_case*
- Do not use the *is-* prefix for *bool* typed variables. 

Add any exceptions with `# noinspection PyPep8Naming` and a comment. <!-- check and change if required -->If classes are saved as variable, e.g. `self.Session: sessionmaker = sessionmaker(...)`.

We recommend WebStorm (free for pupils and students) or Visual Studio Code as development environment. Additionally, use [TSLint](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin) and [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig). For Webstorm, use [Karma](https://plugins.jetbrains.com/plugin/7287-karma).
