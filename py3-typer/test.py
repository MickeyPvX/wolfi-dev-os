import typer

def test(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    typer.run(test)
