# -*- coding: utf-8 -*-

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsProject

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'affiche_infos_projet_dialog_base.ui'))


class AfficheInfosProjetDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(AfficheInfosProjetDialog, self).__init__(parent)

        self.setupUi(self)
        self.btnFermer.clicked.connect(self.ferme)
        self.chargeInfos()

    def chargeInfos(self):
        self.tbInfos.clear()
        couches = QgsProject.instance().mapLayers()
        for couche in couches.values():
            if not couche.name()=="OpenStreetMap":
                self.tbInfos.append("Nom: {}, RS: {}, Src: {}".format(couche.name(), couche.crs().description(), couche.source()))

    def ferme(self):
        self.close()