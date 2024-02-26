{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "43e3b95c-8a77-4ca4-9beb-ccea26846890",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingrese la calificación de la evaluación:  40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nota INSUFICIENTE\n",
      "Diferencia para aprobar: 31.0\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    # Solicitar al usuario que ingrese la calificación\n",
    "    calificacion = float(input(\"Ingrese la calificación de la evaluación: \"))\n",
    "\n",
    "    # Definir la tabla de mensajes según la calificación\n",
    "    if calificacion < 50:\n",
    "        mensaje = \"Nota INSUFICIENTE\"\n",
    "    elif calificacion <= 60:\n",
    "        mensaje = \"REGULAR\"\n",
    "    elif calificacion <= 70:\n",
    "        mensaje = \"BIEN\"\n",
    "    elif calificacion <= 90:\n",
    "        mensaje = \"MUY BIEN\"\n",
    "    elif calificacion <= 100:\n",
    "        mensaje = \"SOBRESALIENTE\"\n",
    "    else:\n",
    "        mensaje = \"Nota no válida\"\n",
    "\n",
    "    # Mostrar el mensaje correspondiente\n",
    "    print(mensaje)\n",
    "\n",
    "    # Calcular la diferencia si la calificación es insuficiente\n",
    "    if calificacion < 71:\n",
    "        diferencia = 71 - calificacion\n",
    "        print(f\"Diferencia para aprobar: {diferencia}\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98dbb821-50c7-4da4-b88a-4aaaad5f048a",
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
