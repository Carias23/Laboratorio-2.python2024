{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75cf68d1-81c1-411b-8cc0-e78038e4cf79",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingrese el día de su fecha de nacimiento:  23\n",
      "Ingrese el mes de su fecha de nacimiento:  9\n",
      "Ingrese el año de su fecha de nacimiento:  1992\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Edad aproximada: 31 años, 5 meses y 10 días\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "def calcular_edad(fecha_nacimiento):\n",
    "    hoy = datetime.now()\n",
    "    edad = hoy - fecha_nacimiento\n",
    "    años = edad.days // 365\n",
    "    meses = (edad.days % 365) // 30\n",
    "    dias = (edad.days % 365) % 30\n",
    "    return años, meses, dias\n",
    "\n",
    "def main():\n",
    "    # Solicitar al usuario ingresar la fecha de nacimiento\n",
    "    dia = int(input(\"Ingrese el día de su fecha de nacimiento: \"))\n",
    "    mes = int(input(\"Ingrese el mes de su fecha de nacimiento: \"))\n",
    "    año = int(input(\"Ingrese el año de su fecha de nacimiento: \"))\n",
    "\n",
    "    # Obtener la fecha de nacimiento como un objeto datetime\n",
    "    fecha_nacimiento = datetime(year=año, month=mes, day=dia)\n",
    "\n",
    "    # Calcular la edad\n",
    "    años, meses, dias = calcular_edad(fecha_nacimiento)\n",
    "\n",
    "    # Mostrar la edad\n",
    "    print(f\"Edad aproximada: {años} años, {meses} meses y {dias} días\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ffc3f36-b33e-443c-b427-40a13ee1ac2c",
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
