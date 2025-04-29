import typer
from picker.commands import pick

app = typer.Typer()
app.add_typer(pick.app, name="pick")  # this registers `cherry-picker pick ...`

if __name__ == "__main__":
    app()
