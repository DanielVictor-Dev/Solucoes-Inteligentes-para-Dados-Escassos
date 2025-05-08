{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b298368-4186-40ed-9951-be7e7a30b7ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import IsolationForest\n",
    "\n",
    "clf_iso = IsolationForest(contamination=0.15)\n",
    "clf_iso.fit(X)\n",
    "\n",
    "scores = clf_iso.decision_function(X)\n",
    "preds = clf_iso.predict(X)\n",
    "df['Anomaly Score'] = scores\n",
    "df['Anomalia Detectada'] = preds\n",
    "\n",
    "# Salvar resultados\n",
    "viz = df[['Nível de Risco', 'Anomaly Score', 'Anomalia Detectada']]\n",
    "viz.to_csv('../visuals/comparativo_anomalias.csv', index=False)"
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
