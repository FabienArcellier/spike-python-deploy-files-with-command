#!/usr/bin/python
# coding=utf-8
import io
import json

import click
import os

from mycommand.utils import hello
import shutil

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


@click.group()
def cli():
    pass


@click.command('command1')
@click.option('--name')
def command1(name):
    hello_name = hello(name)
    print(hello_name)

@click.command('init')
def init():
    wd_path = os.getcwd()
    shutil.copy(SCRIPT_PATH + '/resources/configuration.json', wd_path + '/configuration.json')

@click.command('read')
def read():
    wd_path = os.getcwd()
    with io.open(wd_path + '/configuration.json') as fp:
        values = json.load(fp)
        print(values)

cli.add_command(command1)
cli.add_command(init)
cli.add_command(read)


if __name__ == '__main__':
    cli()
