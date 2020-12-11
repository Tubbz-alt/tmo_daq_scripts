# This should run on drp-neh-cmp007
import psana
import time
import threading
import numpy as np
from p4p.nt import NTScalar
from p4p.server import Server, StaticProvider
from p4p.server.thread import SharedPV


class PVAServer:
    def __init__(self):
        self.provider = StaticProvider('ttfex_provider')
        self.pvs = {}

        pv = SharedPV(nt=NTScalar('d'), initial=0.0)
        self.provider.add('DRP:ATM:CAM:01:Pva:FLTPOS', pv)
        self.pvs['FLTPOS'] = pv

    def read_timetool(self):
        while True:
            ds = psana.DataSource(shmem='tmo')
            for run in ds.runs():
                det = run.Detector('tmoopal2')
                for evt in run.events():
                    time.sleep(2.0)
                    yield {'FLTPOS', det.ttfex.fltpos(evt)}

    def run(self):
        with Server(providers=[self.provider]) as self.server:
           for data in self.read_timetool():
                for name, value in data.items():
                   self.pvs[name].post(value)

if __name__ == '__main__':

    server = PVAServer()

    try:
        server.run()
    except KeyboardInterrupt:
        pass

