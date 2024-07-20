import sys, os

import logging

from . import simulationStepBase

class potentialEnergyMeasurement(simulationStepBase):
    """
    Component name: potentialEnergyMeasurement
    Component type: simulationStep

    Author: Pablo Ibáñez-Freire
    Date: 18/10/2023

    """

    availableParameters = {"outputFilePath","potentials"}
    requiredParameters  = {"outputFilePath"}
    availableSelections = {"selection"}
    requiredSelections  = set()

    def __init__(self,name,**params):
        super().__init__(_type = self.__class__.__name__,
                         _name = name,
                         availableParameters = self.availableParameters,
                         requiredParameters  = self.requiredParameters,
                         availableSelections = self.availableSelections,
                         requiredSelections  = self.requiredSelections,
                         **params)

        ############################################################
        ############################################################
        ############################################################

        parameters = {}

        parameters["outputFilePath"]  = params["outputFilePath"]

        if "potentials" in params:
            parameters["interactorsList"] = params["potentials"]

        simulationStep = {
            name:{
              "type":["ThermodynamicMeasure","InteractorsListEnergyMeasure"],
              "parameters":{**parameters}
            }
        }

        ############################################################

        self.setGroup("selection")
        self.setSimulationStep(simulationStep)



