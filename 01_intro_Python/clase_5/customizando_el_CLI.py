import click


@click.command()
@click.option("--nombre", type=str, help="El nombre de la persona.")
@click.option("--edad", type=int, default=1, help="La edad de la persona.")
def me_llamo(nombre, edad):
    """Programa que arma una frase con nombre y edad."""
    click.echo(f"Hola, mi nombre es {nombre}, un gusto :)")
    click.echo(f"Tengo {edad} años")


if __name__ == "__main__":
    me_llamo()
