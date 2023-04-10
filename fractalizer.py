#!/usr/bin/python3
import click
import koch
import mandelbrodt
import tree
import julia

@click.group()
def fractalizer():
    pass
fractalizer.add_command(koch.koch)
fractalizer.add_command(mandelbrodt.mandelbrodt)
fractalizer.add_command(tree.tree)
fractalizer.add_command(julia.julia)

if __name__ == '__main__':
    fractalizer()
