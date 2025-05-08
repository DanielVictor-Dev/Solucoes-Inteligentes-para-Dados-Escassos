{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07eff1b5-a7f3-4f18-97ad-559ed113b950",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.tree import DecisionTreeClassifier, plot_tree\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df = pd.read_csv('../data/dados_simulados.csv')\n",
    "le = LabelEncoder()\n",
    "\n",
    "for col in df.select_dtypes(include='object'):\n",
    "    df[col] = le.fit_transform(df[col])\n",
    "\n",
    "X = df.drop('Nível de Risco', axis=1)\n",
    "y = df['Nível de Risco']\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)\n",
    "\n",
    "clf = DecisionTreeClassifier(max_depth=5)\n",
    "clf.fit(X_train, y_train)\n",
    "\n",
    "y_pred = clf.predict(X_test)\n",
    "print(confusion_matrix(y_test, y_pred))\n",
    "print(classification_report(y_test, y_pred))\n",
    "\n",
    "plt.figure(figsize=(20,10))\n",
    "plot_tree(clf, feature_names=X.columns, class_names=le.classes_, filled=True)\n",
    "plt.savefig('../visuals/arvore_decisao.png')"
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
