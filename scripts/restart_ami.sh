#!/bin/bash
procmgr stop tmo.cnf ami-worker_0_0 ami-worker_0_1 ami-worker_0_2 ami-worker_0_3 ami-node_0 ami-manager ami-client
procmgr start tmo.cnf ami-worker_0_0 ami-worker_0_1 ami-worker_0_2 ami-worker_0_3 ami-node_0 ami-manager ami-client
