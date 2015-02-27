from malleefowl import config

from hummingbird.process import ESMValToolProcess
from hummingbird import esmvaltool

from malleefowl import wpslogging as logging
logger = logging.getLogger(__name__)

class ESMValToolMyDiagProcess(ESMValToolProcess):
    def __init__(self):
        ESMValToolProcess.__init__(self,
            identifier = "mydiag",
            title = "ESMValTool MyDiag",
            version = "0.1",
            abstract="Tutorial diagnostic used in the doc/toy-diagnostic-tutorial.pdf")

        self.variable = self.addLiteralInput(
            identifier="variable",
            title="Variable",
            abstract="",
            default="ta",
            type=type(''),
            minOccurs=1,
            maxOccurs=1,
            allowedValues=['ta']
            )

    def execute(self):
        self.show_status("starting", 0)

        constraints=esmvaltool.build_constraints(
            project="CMIP5",
            models=self.getInputValues(identifier='model'),
            variable=self.variable.getValue(),
            cmor_table=self.cmor_table.getValue(),
            experiment=self.experiment.getValue(),
            ensemble=self.ensemble.getValue())
        
        out, namelist, log_file, reference = esmvaltool.diag(
            name="mydiag",
            credentials=self.credentials.getValue(),
            constraints=constraints,
            start_year=self.start_year.getValue(),
            end_year=self.end_year.getValue(),
            output_format=self.output_format.getValue(),
            monitor=self.show_status  )
        
        self.show_status("done", 100)

        """
        PY  info: NAMELIST   = namelist.xml
        PY  info: WORKDIR    = /home/Shared/pingu/var/tmp/pywps-instanceTASv2H/workspace/work
        PY  info: CLIMODIR   = /home/Shared/pingu/var/tmp/pywps-instanceTASv2H/workspace/climo
        PY  info: PLOTDIR    = /home/Shared/pingu/var/tmp/pywps-instanceTASv2H/workspace/plots
        PY  info: REFERENCES = /home/Shared/pingu/var/tmp/pywps-instanceTASv2H/workspace/work/namelist.txt
        """

        self.output.setValue(out)
        self.namelist.setValue(namelist)
        self.log.setValue(log_file)
        self.reference.setValue(reference)
        

 