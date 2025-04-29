import typer
from picker.commands.pick import pick

app = typer.Typer()
app.command()(pick)  # ← directly registers the command function

if __name__ == "__main__":
    app()
