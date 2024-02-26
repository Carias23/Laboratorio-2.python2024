{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bc28201e-fb44-4acd-bdfe-d896651c462d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingresa el número de segundos:  5871\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Horas: 1 Minutos: 37 Segundos: 51\n"
     ]
    }
   ],
   "source": [
    "def segundos_a_horas_minutos_segundos(segundos):\n",
    "    horas = segundos // 3600\n",
    "    segundos_restantes = segundos % 3600\n",
    "    minutos = segundos_restantes // 60\n",
    "    segundos = segundos_restantes % 60\n",
    "    print(\"Horas:\", horas, \"Minutos:\", minutos, \"Segundos:\", segundos)\n",
    "\n",
    "def main():\n",
    "    segundos = int(input(\"Ingresa el número de segundos: \"))\n",
    "    segundos_a_horas_minutos_segundos(segundos)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "575576b2-0b78-4361-8885-a523ac24c8f7",
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
