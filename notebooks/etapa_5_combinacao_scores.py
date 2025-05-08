{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1faf6d9-9ff0-42b1-8e4d-0063f0d1327b",
   "metadata": {},
   "outputs": [],
   "source": [
    "conditions = [\n",
    "    (df['Nível de Risco'] == 'alto') | (df['Anomalia Detectada'] == -1),\n",
    "    (df['Nível de Risco'] == 'médio') & (df['Anomalia Detectada'] == 1),\n",
    "    (df['Nível de Risco'] == 'baixo') & (df['Anomalia Detectada'] == 1)\n",
    "]\n",
    "\n",
    "decisions = ['Rejeitar', 'Revisar', 'Aprovar']\n",
    "df['Decisão Final'] = np.select(conditions, decisions, default='Revisar')\n",
    "df.to_csv('../data/decisao_final.csv', index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
