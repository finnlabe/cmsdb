# coding: utf-8

"""
Common, analysis independent definition of the 2017 data-taking campaign
with datasets at NanoAOD tier in version 11, created with custom content at UHH.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those of MiniAOD input datasets in DAS (https://cmsweb.cern.ch/das).

Since this is a custom production, neither can LFNs be obtained through DAS (or dasgloclient), nor
can PFNs be located through the usual, central redirectors.

They are centrally saved at the dCache instance at DESY (e.g. dcache-door-cms04.desy.de) under
/pnfs/desy.de/cms/tier2/store/user/bwieders/nano_uhh_v11.
"""

from order import Campaign

#
# campaign
#

campaign_run2_2017_nano_L1nano = Campaign(
    name="run2_2017_nano_L1nano",
    id=22017112122,  
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2017,
        "version": 0,
        "custom": {
            "name": "run2_2017_nano_L1nano",
            "creator": "L1nano",
            "location": "/pnfs/desy.de/cms/tier2/store/user/flabe/L1nano",  # noqa
        },
    },
)

import cmsdb.processes as procs

# just a testing dataset, to understand the workflow
campaign_run2_2017_nano_L1nano.add_dataset(
    name="tt_l1nano",
    id=12345678, # whats this?
    processes=[procs.tt_sl],
    keys=[
        "tt",  # noqa
    ],
    n_files=1,
    n_events=1000,
)