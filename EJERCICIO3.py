{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c35acc8-c668-4f87-bdfb-1c258a00c7dd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingrese el primer número (mayor):  9\n",
      "Ingrese el segundo número (menor):  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La suma de los números entre 9 y 5 es: 35\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    # Solicitar al usuario que ingrese dos números\n",
    "    num1 = int(input(\"Ingrese el primer número (mayor): \"))\n",
    "    num2 = int(input(\"Ingrese el segundo número (menor): \"))\n",
    "\n",
    "    # Validar que el primer número sea mayor que el segundo\n",
    "    if num1 <= num2:\n",
    "        print(\"Error: El primer número debe ser mayor que el segundo.\")\n",
    "        return\n",
    "\n",
    "    # Calcular la suma de los números comprendidos entre ambos\n",
    "    suma = 0\n",
    "    for i in range(num2, num1 + 1):\n",
    "        suma += i\n",
    "\n",
    "    # Mostrar la suma\n",
    "    print(f\"La suma de los números entre {num1} y {num2} es: {suma}\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70e3a777-284a-4ae7-a75f-679d9833711f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
