"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

def main():
    try:
        # Verificar que haya exactamente 2 argumentos
        if len(sys.argv) != 3:
            raise ValueError
        
        # Convertir a números
        total_load = float(sys.argv[1])
        num_supports = float(sys.argv[2])

        # Verificar división por cero
        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
            return

        # Calcular carga por soporte
        load_per_support = total_load / num_supports

        # Mostrar resultado con 2 decimales
        print(f"Load per support point: {load_per_support:.2f} N")

    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")


if __name__ == "__main__":
    main()
# TODO: Implementar según README.md
