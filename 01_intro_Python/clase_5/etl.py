from time import sleep

print("¡Hola!")
print(__name__)

def process_data(data:str):
    print("Arrancando el procesamiento...")
    modified_data = "Estoy haciendo un ETL con " + data
    sleep(3)
    print("Lista la data.")
    return modified_data


def main():
    data = "datos de la web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__":
    main()
