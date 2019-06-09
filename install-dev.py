#!/usr/bin/env python
#!args install
import json
import sys
import click
from click import echo
from typing import Optional
from halo import Halo
from git import Repo
import subprocess
import requests
import os

BLACKLIST = [
    "sound",
    "python3-lib",
    "java-lib",
    "gamedesign",
    "website",
    "cryptic-term",
    "graphics",
    "cryptic",
    "frontend",
]


current_directory = os.path.dirname(os.path.abspath(__file__))
repository_directory = os.path.dirname(current_directory)


def progress(op_code, cur_count, max_count=None, message=""):
    # TODO I dont understand this, so...
    # https://gitpython.readthedocs.io/en/stable/reference.html?highlight=RemoteProgress#git.remote.RemoteProgress.update
    # ^ if someone wants to dig into that
    pass


def clone(url, path):
    if os.path.exists(path):
        return f"'{path}' already exists"
    Repo.clone_from(url, path, progress=progress)


def get_repos(debug=False):
    if not debug:
        response: requests.Response = requests.get(
            "https://api.github.com/orgs/cryptic-game/repos"
        )
        if response.status_code != 200:
            raise Exception(
                "Couldn't reach the GitHub API to download a list of all cryptic-game repositories. (Maybe try again later?)"
            )
        raw_repos = response.json()
    else:
        print("WARNING: debug is enabled")
        with open(os.path.join(current_directory, "repos.json"), "r") as f:
            raw_repos = json.load(f)
    # maybe this is redundant
    blacklist = ["cryptic-game/" + e for e in BLACKLIST]
    names = []
    for repo in raw_repos:
        name = repo["full_name"]
        if name not in blacklist:
            names.append(name)
    # remove the prefix again
    names = [e.replace("cryptic-game/", "") for e in names]
    return names


@click.group()
def cli():
    pass


def text(i, length, repo, *msg):
    return f"({i}/{length}) {repo}: {' '.join(msg)}"


def download_repo(_text, repo):
    from time import sleep

    path = os.path.join(repository_directory, repo)
    _text("Cloning repository into " + path)
    clone_result = clone("https://github.com/cryptic-game/" + repo + ".git", path)
    if clone_result is not None:
        _text(clone_result, special="warn")
        return False

    # assume that something is a *python* microservice, if:
    #  - the repository name starts with "cryptic-"
    #  - a folder with the name "app" exists in the root directory
    #  - a file with the path "app/app.py" exists
    if repo.startswith("cryptic-"):
        os.chdir(path)
        if os.path.isdir("app") and os.path.isfile("app/app.py"):
            os.chdir(os.path.join(path, "app"))
            _text("Installing dependencies")
            # TODO error checking
            subprocess.call(
                ["pipenv", "install"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            _text("Successfully installed", special="succeed")
            return

    _text("Successfully cloned", special="succeed")


@click.command()
@click.argument("repository", required=False, nargs=-1)
def install(repository: Optional[str]):
    # no explicit repositories given, which means install all
    available_repos = get_repos()
    if len(repository) == 0:
        repos = available_repos
    else:
        repos = []
        raw: str
        for raw in repository:
            if not raw.startswith("cryptic-game/"):
                raw = "cryptic-game/" + raw
            if raw not in available_repos:
                echo(
                    f"Omitting repository '{raw}' as it is not an available repository."
                )
            else:
                repos.append(raw)
    ok = 0

    for i, repo in enumerate(repos):
        spinner = Halo(text=text(i + 1, len(repos), repo, "Starting installation"))

        def _text(*msg, special=False):
            t = text(i + 1, len(repos), repo, *msg)
            if special == "succeed":
                spinner.succeed(t)
            elif special in ("error", "fail"):
                spinner.fail(t)
            elif special == "warn":
                spinner.warn(t)
            else:
                spinner.text = t

        spinner.start()
        download_result = download_repo(_text, repo)

        if download_result is None:
            ok += 1

    echo(f"Successfully cloned {ok} out of {len(repos)} repositories.")


cli.add_command(install)

if __name__ == "__main__":
    cli()
