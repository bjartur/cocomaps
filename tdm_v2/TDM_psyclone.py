"""
25.01.18
Author 
    david@iiim.is

About
The task dialog(ue) manager [TDM] to psyclone setup. The manger is initialized
within this function and controlled via psyclone with messaging. 
"""

import TDM
import cmsdk2

global api
api = None


def PsyCrank(apilink):
    api = cmsdk2.PsyAPI.fromPython(apilink)
    name = api.getModuleName()

    # Initialize the TDM by calling an instance of object TDM
    _TDM = TDM.TDM()

    # TODO: Add functionality and connectors to the psycrank

    while api.shouldContinue():
        msg = None
        msg = api.wautForNewMessage(20)

        if _TDM.check_for_person():
            _TDM.start_at("greet")




