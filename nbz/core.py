"""nbz is a typer-based wrapper around the incredible nbdev project."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['app', 'commands', 'console', 'nyi_commands', 'helper', 'with_spinner', 'add_nyi_command']

# %% ../nbs/00_core.ipynb 4
import types
from functools import wraps
import typer
from typing_extensions import Annotated
from fastcore.docments import *
from fastcore.script import *
from fastcore.test import *
from fastcore.utils import *
from rich.console import Console
from rich import print

# %% ../nbs/00_core.ipynb 6
from nbdev import cli, release, config, quarto, doclinks, merge, migrate, sync
from nbdev import clean as nbclean
from nbdev import test as nbtest
from .commands import new

# %% ../nbs/00_core.ipynb 7
app = typer.Typer(rich_markup_mode="markdown")

# %% ../nbs/00_core.ipynb 10
@app.callback(invoke_without_command=True)
def helper(ctx: typer.Context):
    """
    nbz is a typer-based wrapper around the incredible nbdev project.
    """
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())       

# %% ../nbs/00_core.ipynb 12
commands = {
    'bump_version': release.nbdev_bump_version,        
    'clean':nbclean.nbdev_clean,        
    'changelog': release.changelog,
    'conda': release.release_conda, 
    'create_config': config.nbdev_create_config,  
    'docs': quarto.nbdev_docs,
    'filter': cli.nbdev_filter,
    'fix': merge.nbdev_fix,
    'install': quarto.install,
    'install_hooks': nbclean.nbdev_install_hooks,
    'install_quarto': quarto.install_quarto,
    'merge': merge.nbdev_merge,
    'migrate': migrate.nbdev_migrate,    
    'new': new,
	'prepare': quarto.prepare,
	'preview': quarto.nbdev_preview,
    'proc_nbs': quarto.nbdev_proc_nbs,
    'pypi': release.release_pypi, 
	'readme': quarto.nbdev_readme,
    'release_both': release.release_both,
    'release_gh': release.release_gh,
    'release_git': release.release_git,       
    'requirements': release.write_requirements,
    'sidebar': quarto.nbdev_sidebar,
    'test': nbtest.nbdev_test,
    'trust': nbclean.nbdev_trust,
    'update': sync.nbdev_update,
    'update_license': cli.nbdev_update_license,
    'watch_export': cli.watch_export
}

# %% ../nbs/00_core.ipynb 18
def with_spinner(f):
    "Wraps a command with a spinner using rich.console.status"
    @wraps(f)
    def _inner(*args, **kwargs):
        with console.status("", spinner="dots") as status:          
            try:
                result = f(*args, **kwargs)
                return result
            except Exception as e:
                raise e
    return _inner

# %% ../nbs/00_core.ipynb 20
console = Console()
for fname,func in commands.items():

    # Remove call_parse so it doesn't conflict with typer
    func = getattr(func, '__wrapped__', func)
    
    # Wrap the function in a spinner
    func = with_spinner(func)    

    # dd to typer.app and 
    kwargs = dict(
        # Assign to panel
        rich_help_panel=getattr(func, 'rich_help_panel', func.__module__),
        no_args_is_help=getattr(func,'no_args_is_help',False)
    )
    func = app.command(**kwargs)(func)

    # Prep the annotations to map accurately to typer
    arguments = docments(func, full=True)
    
    for arg, meta in arguments.items():
        # This next line might be simplistic and could cause errors
        if meta['anno'] in (bool_arg, store_true): meta['anno'] = bool
        func.__annotations__[arg] = Annotated[meta['anno'], typer.Argument()]
    # Fix the name
    func.__name__ = fname

    # Save to the global names 
    globals()[fname] = func

# %% ../nbs/00_core.ipynb 23
# Not yet implemented
# TODO: fix store_true on these commands. 
nyi_commands = {
    'export': doclinks.nbdev_export,
    'export_cli': cli.nb_export_cli,
}

# %% ../nbs/00_core.ipynb 24
def add_nyi_command(fname):
    @app.command(rich_help_panel='Not yet implemented')
    def func():
        'Not yet implemented'
        print(f'[red][b]ERROR: {func.__doc__}[/b][/red]')
    func.__name__ = fname
    globals()[fname] = func

# %% ../nbs/00_core.ipynb 26
# Add NYI panel
for fname in nyi_commands.keys():
    add_nyi_command(fname)
