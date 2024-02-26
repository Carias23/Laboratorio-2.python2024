{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf2aaca7-4fac-4606-992b-85ff41f4bb7c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingrese un número mayor que 0:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factores: {1, 2}\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    # Solicitar al usuario que ingrese un número mayor que 0\n",
    "    numero = int(input(\"Ingrese un número mayor que 0: \"))\n",
    "\n",
    "    # Validar que el número sea mayor que 0\n",
    "    if numero <= 0:\n",
    "        print(\"Error: Debe ingresar un número mayor que 0.\")\n",
    "        return\n",
    "\n",
    "    # Inicializar el divisor y una lista para almacenar los factores\n",
    "    divisor = 1\n",
    "    factores = set()\n",
    "\n",
    "    # Encontrar los factores del número\n",
    "    while divisor <= numero:\n",
    "        if numero % divisor == 0:\n",
    "            factores.add(divisor)\n",
    "        divisor += 1\n",
    "\n",
    "    # Mostrar los factores encontrados\n",
    "    print(f\"Factores: {factores}\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c4ca032-a6a2-4627-b94f-5efe7aecebfa",
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
